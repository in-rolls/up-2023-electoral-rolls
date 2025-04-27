## UP 2023 Electoral Rolls

We scrape electoral rolls from https://ceouttarpradesh.nic.in/rollpdf/rollpdf.aspx

We split scraping into two steps:

1. [harvesting all the links](01-up-scrape-pdf-links.ipynb) --- CSV with links to the pdf is [here](data/)
2. [downloading the pdfs](02-download_pdf.py)

The PDFs are posted to https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/OG47IV

## 🔗 Adjacent Repositories

- [in-rolls/parse_searchable_rolls](https://github.com/in-rolls/parse_searchable_rolls) — Parse Searchable Electoral Rolls
- [in-rolls/electoral_rolls](https://github.com/in-rolls/electoral_rolls) — PDFs of Indian Electoral Rolls
- [in-rolls/local_elections_kerala](https://github.com/in-rolls/local_elections_kerala) — Kerala Local Government Seat Reservation Data and Winner Attributes
- [in-rolls/local_elections_up](https://github.com/in-rolls/local_elections_up) — UP Local Election Data --- GP and ULB. Seat reservation, winner, and candidates for some elections
- [in-rolls/local_elections_bihar](https://github.com/in-rolls/local_elections_bihar) — Candidate Info. + Valid Votes Won by Cands. in the 2016 Bihar Panchayat Elections
