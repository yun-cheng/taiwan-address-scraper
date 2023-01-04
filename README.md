# Taiwanese Addresses Scraper

## File Structure

```text
├── src/
│   ├── common/
│   │   ├── captcha_helpers.py
│   │   ├── driver_helpers.py
│   │   └── request_helpers.py
│   ├── s0_process_town_data/
│   │   ├── helpers.py
│   │   └── process_town_data.ipynb
│   └── s1_scrape_addresses/
│       ├── helpers.py
│       └── scrape_addresses.ipynb
├── data/
│   ├── raw/
│   │   ├── captcha/
│   │   │   └── xxxxxxxx.jpg
│   │   └── town/
│   │       └── mapdata202211291014/
│   │           └── TOWN_MOI_1111118.dbf
│   ├── interim/
│   ├── processed/
│   │   └── town/
│   │       ├── town.csv
│   │       └── town_221129.csv
│   ├── external/
│   │   └── query_data.txt
│   └── temp/
│       └── screenshot.png
├── references/
├── results/
│   └── address_221201.csv
├── .devcontainer/
├── .rstudio_config/
├── .vscode/
├── .dockerignore
├── .env
├── .gitignore
├── docker-compose.yml
├── README.md
└── requirements.txt
```
