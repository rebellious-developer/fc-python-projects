#!/usr/bin/env python3
"""
Scrapes data from Wikipedia using Beautiful Soup in Python and then extracts specific information and formats it for output.

Requirements:
- The beautifulsoup4 library should be used for web scraping.
- The requests library should be used to fetch the webpage content.
- The program should scrape the Wikipedia page for the list of largest companies in the US by revenue:
  * Url: https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue
- The program should extract the table containing the list of companies, including their rank, name, industry, revenue, and other relevant details.
- The extracted data should be cleaned and formatted into a Pandas DataFrame.
- Output should be displayed in a readable tabular format using Pandas.
"""

import re

import pandas as pd
import requests
from bs4 import BeautifulSoup


def fetch_webpage(url) -> str:
    """Fetches the webpage content from the given URL via the requests library."""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Raise an error for bad responses
    return response.text


def fetch_largest_us_companies_dataset() -> pd.DataFrame:
    """Fetches and processes the largest companies dataset from Wikipedia. End result is a Pandas DataFrame containing the data."""

    url = "https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue"

    try:
        webpage_content = fetch_webpage(url)
    except requests.RequestException as e:
        raise Exception(f"Error fetching the webpage at '{url}': {e}")

    soup = BeautifulSoup(webpage_content, "html.parser")
    table = soup.find("table", {"class": "wikitable"})

    if not table:
        raise Exception("Could not find the table on the webpage.")

    rows = table.find_all("tr")
    if not rows:
        raise Exception("No rows found in the table.")

    # Extract and clean table headings
    table_headings = [th.get_text(strip=True) for th in rows[0].find_all("th")]
    for i in range(len(table_headings)):
        # Attempt to create a valid column name formatted according to lower_snake_case
        heading = table_headings[i]
        heading = heading.strip().lower().replace(" ", "_")
        heading = re.sub(r"\W", "_", heading).strip("_")

        # Empty heading case
        if heading == "":
            heading = f"column_{i + 1}"

        table_headings[i] = heading

    table_data = []
    for i in range(1, len(rows)):
        cols = rows[i].find_all(["td", "th"])
        cols = [col.get_text(strip=True) for col in cols]

        # If the number of columns matches the number of headings, add the row to the data
        if len(cols) == len(table_headings):
            table_data.append(cols)

    ds = pd.DataFrame(table_data, columns=table_headings)
    return ds


def main():
    pd.set_option("display.max_rows", None)
    print("Web Scraping: Largest Companies in the US by Revenue\n")
    try:
        df = fetch_largest_us_companies_dataset()
        print(df.to_string(index=False))
    except Exception as e:
        print(f"ERROR: {e}")
        return


if __name__ == "__main__":
    main()
