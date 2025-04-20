## UP 2023 Electoral Rolls

We scrape electoral rolls from https://ceouttarpradesh.nic.in/rollpdf/rollpdf.aspx

We split scraping into two steps:

1. [harvesting all the links](01-up-scrape-pdf-links.ipynb) --- CSV with links to the pdf is [here](data/)
2. [downloading the pdfs](02-download_pdf.py)

The PDFs are posted to https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/OG47IV

## 🔗 Adjacent Repositories

- [in-rolls/parse_searchable_rolls](https://github.com/in-rolls/parse_searchable_rolls) — Parse Searchable Electoral Rolls
- [in-rolls/mnrega_social](https://github.com/in-rolls/mnrega_social) — MNREGA Social Audit Data
- [in-rolls/delim_raj](https://github.com/in-rolls/delim_raj) — Digitized Rajasthan GP Delimitation Files
- [in-rolls/electoral_rolls](https://github.com/in-rolls/electoral_rolls) — PDFs of Indian Electoral Rolls
- [in-rolls/local_elections_kerala](https://github.com/in-rolls/local_elections_kerala) — Kerala Local Government Seat Reservation Data and Winner Attributes
