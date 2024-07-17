# LinkedIn Data Scraping

This project uses Selenium to scrape data from LinkedIn profiles. The script automates the process of logging into LinkedIn, searching for profiles, and extracting information about individuals.

## Installation

First, install the necessary dependencies:

```bash
pip install selenium pandas warnings
```

## Usage

To run the script, use the following command:

```bash
python main.py
```

## Input Details

When prompted, provide the following details:

1. The name of the person you want to extract data about.
2. Your Gmail ID.
3. Your LinkedIn password.

## Output

The script generates an output file named `linkedin_data.csv` with the following columns:

1. Person Name
2. Job Title
3. Person Image (Link)
4. Location

## Example

```bash
python main.py
```

You will be prompted to enter the name, your Gmail ID, and your LinkedIn password. After the script runs, you will find the `linkedin_data.csv` file in the same directory.

---
