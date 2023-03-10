import os
import pandas as pd
import mapply
import requests
from twocaptcha import TwoCaptcha
from anticaptchaofficial.imagecaptcha import *

from bs4 import BeautifulSoup
import json

TOKEN_2CAPTCHA = '<PUT TOKEN HERE>'
TOKEN_ANTI_CAPTCHA = '<PUT TOKEN HERE>'

OUTPUT_DIR = './pdf'

mapply.init(
    n_workers=32,
    chunk_size=50,
    max_chunks_per_worker=0,
    progressbar=True
)

def download_file_by_2captcha(url, fn):
    retry = 0
    while retry < 5:
        try:
            s = requests.Session()
            r = s.get(url, timeout=10)
            print(r.status_code)
            soup = BeautifulSoup(r.content, 'html.parser')
            viewstate = soup.find('input', {'id': '__VIEWSTATE'})['value']
            viewstategenerator = soup.find('input', {'id': '__VIEWSTATEGENERATOR'})['value']
            eventvalidation = soup.find('input', {'id': '__EVENTVALIDATION'})['value']
            r = s.get("https://ceouttarpradesh.nic.in/rollpdf/CImage.aspx", timeout=10)
            print(r.status_code)
            cfn = fn.replace('pdf', 'jpg')
            with open(cfn, 'wb') as f:
                f.write(r.content.split(b'\r\n\r\n')[0])
            solver = TwoCaptcha(TOKEN_2CAPTCHA)        
            captcha = solver.normal(cfn, caseSensitive=1)
            with open(cfn.replace('jpg', 'json'), 'w') as f:
                f.write(json.dumps(captcha))
            data = {'__VIEWSTATE': viewstate,
                    '__VIEWSTATEGENERATOR': viewstategenerator,
                    '__EVENTVALIDATION': eventvalidation,
                    'ctl00$ContentPlaceHolder1$txtimgcode': captcha['code'],
                    'ctl00$ContentPlaceHolder1$Button1': 'View/Download'
                }
            r = s.post(url, data, timeout=10)
            print(r.status_code)
            if len(r.content) < 20000 and r.content.find(b'InValid Captcha') != -1:
                print('Wrong captcha', captcha)
                solver.report(captcha['captchaId'], False)
            else:
                with open(fn, 'wb') as f:
                    f.write(r.content)
                solver.report(captcha['captchaId'], True)
                break
        except Exception as e:
            print(e)
        retry += 1


def download_file_by_anticaptcha(url, fn):
    retry = 0
    while retry < 5:
        try:
            s = requests.Session()
            r = s.get(url, timeout=10)
            print(r.status_code)
            soup = BeautifulSoup(r.content, 'html.parser')
            viewstate = soup.find('input', {'id': '__VIEWSTATE'})['value']
            viewstategenerator = soup.find('input', {'id': '__VIEWSTATEGENERATOR'})['value']
            eventvalidation = soup.find('input', {'id': '__EVENTVALIDATION'})['value']
            r = s.get("https://ceouttarpradesh.nic.in/rollpdf/CImage.aspx", timeout=10)
            print(r.status_code)
            cfn = fn.replace('pdf', 'jpg')
            with open(cfn, 'wb') as f:
                f.write(r.content.split(b'\r\n\r\n')[0])
            solver = imagecaptcha()
            solver.set_verbose(1)
            solver.set_key(TOKEN_ANTI_CAPTCHA)
            # Specify softId to earn 10% commission with your app.
            # Get your softId here: https://anti-captcha.com/clients/tools/devcenter
            solver.set_soft_id(0)
            text = solver.solve_and_return_solution(cfn, case=True)
            if text != 0:
                captcha = {'code': text}
            else:
                captcha = {'code': '',
                           'error_code': solver.error_code}
            with open(cfn.replace('jpg', 'json'), 'w') as f:
                f.write(json.dumps(captcha))
            data = {'__VIEWSTATE': viewstate,
                    '__VIEWSTATEGENERATOR': viewstategenerator,
                    '__EVENTVALIDATION': eventvalidation,
                    'ctl00$ContentPlaceHolder1$txtimgcode': captcha['code'],
                    'ctl00$ContentPlaceHolder1$Button1': 'View/Download'
                }
            r = s.post(url, data, timeout=10)
            print(r.status_code)
            if len(r.content) < 20000 and r.content.find(b'InValid Captcha') != -1:
                print('Wrong captcha', captcha)
                solver.report_incorrect_image_captcha()
            else:
                with open(fn, 'wb') as f:
                    f.write(r.content)
                break
        except Exception as e:
            print(e)
        retry += 1


def download(r):
    url = r['ElectorRollPdf']
    fn = os.path.join(OUTPUT_DIR, '%s_%d_%d.pdf' % (r['District'], r['AC_Number'], r['Part_Number']))
    if not os.path.exists(fn):
        print(url, fn)
        download_file_by_anticaptcha(url, fn)

#df = pd.read_csv('up-elector-roll.csv', usecols=['District', 'AC_Number', 'Part_Number', 'ElectorRollPdf'], nrows=5)
df = pd.read_csv('up-elector-roll.csv', usecols=['District', 'AC_Number', 'Part_Number', 'ElectorRollPdf'])
print(df)

df.mapply(lambda r: download(r), axis=1)
