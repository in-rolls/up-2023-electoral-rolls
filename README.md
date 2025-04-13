## UP 2023 Electoral Rolls

We scrape electoral rolls from https://ceouttarpradesh.nic.in/rollpdf/rollpdf.aspx

We split scraping into two steps:

1. [harvesting all the links](01-up-scrape-pdf-links.ipynb) --- CSV with links to the pdf is [here](data/)
2. [downloading the pdfs](02-download_pdf.py)

The PDFs are posted to https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/OG47IV
