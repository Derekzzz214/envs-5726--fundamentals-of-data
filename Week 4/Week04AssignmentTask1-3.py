from pathlib import Path
sec_folder = Path(r"C:\Users\张周延\Downloads\SEC_EDGAR_10K")

headers = ["Company Name", "Year", "Count Sustainability", "Count AI"]
sec_table = []

ticker_to_name = {
    "amzn": "Amazon",
    "goog": "Google",
    "msft": "Microsoft",
    "nvda": "NVIDIA",
}

for file_path in sec_folder.glob("*.html"):
    file_name = file_path.stem
    ticker = file_name.split("-")[0]
    date_str = file_name[-8:]

    company_name = ticker_to_name[ticker]
    year = int(date_str[:4])

    with open(file_path, "r", encoding="utf-8", errors="ignore") as html_file:
        text = html_file.read().upper()

    count_sus = text.count("SUSTAINABILITY")
    count_ai = text.count("ARTIFICIAL INTELLIGENCE")
    sec_table.append([company_name, year, count_sus, count_ai])

print(headers)
for row in sec_table[:10]:
    print(row)

def get_average_by_company(headers, table, column_name_to_average, company_name):

    col_index = headers.index(column_name_to_average)
    company_col_index = headers.index("Company Name")

    values = []
    for row in table:

        if row[company_col_index] == company_name:
            values.append(row[col_index])

    if len(values) > 0:
        return sum(values) / len(values)
    else:
        return 0

for company_name in ['NVIDIA', 'Microsoft', 'Google', 'Amazon']:
    for column_name_to_average in ['Count Sustainability', 'Count AI']:
        column_average = get_average_by_company(headers=headers,
                                               table=sec_table,
                                               column_name_to_average=column_name_to_average,
                                               company_name=company_name)
        print(f'The average of {column_name_to_average} for {company_name} is {column_average}')

import csv
companies = ["NVIDIA", "Microsoft", "Google", "Amazon"]

for company in companies:
    company_table = []
    for row in sec_table:
        if row[0] == company:
            company_table.append(row)

    with open(Path(fr"C:\Users\张周延\Downloads\SEC_10K_{company}_Metrics.csv"), "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(company_table)
