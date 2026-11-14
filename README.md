# DATA 430 Project 3: Web Scraping and Multi-Format Output

## Project Overview

This project implements a Python web scraper that collects quotes from [Quotes to Scrape](https://quotes.toscrape.com/).

The scraper automatically follows pagination links, extracts quote information, and exports the collected records into four different file formats: CSV, plain text, JSON, and YAML.

The project demonstrates web scraping, HTML parsing, data transformation, file handling, and responsible request management.

## Technologies Used

- Python 3.12
- Requests — retrieves webpage content
- BeautifulSoup4 — parses HTML and extracts quote data
- PyYAML — generates YAML output
- Python standard libraries — CSV, JSON, datetime, pathlib, time, and urllib.parse

## Project Structure

```text
Project 3/
├── scraper.py
├── requirements.txt
├── README.md
├── .gitignore
└── output/
    ├── quotes.csv
    ├── quotes.txt
    ├── quotes.json
    └── quotes.yaml
```

## Installation

Python 3.8 or later is required.

1. Clone the GitHub repository and navigate to the project directory.
2. Create a virtual environment:

   ```bash
   python3 -m venv .venv
   ```

3. Activate the environment on macOS or Linux:

   ```bash
   source .venv/bin/activate
   ```

4. Install the required dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

## Running the Scraper

Execute the following command from the project directory:

```bash
python scraper.py
```

The script runs without command-line arguments or configuration changes.

It automatically creates the `output/` directory if necessary and writes all four output files.

Existing output files are overwritten on each run.

## Data Collection

The scraper begins at the first page of the website and follows each available next-page link until no additional pages remain.

Each quote record contains five fields:

- **quote:** Quote text with surrounding quotation marks removed
- **author:** Name of the quote's author
- **tags:** Complete list of tags associated with the quote
- **page:** Page number where the quote was found
