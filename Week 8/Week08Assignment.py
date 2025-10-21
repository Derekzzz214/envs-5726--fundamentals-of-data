#Task1
from pathlib import Path
from typing import List
import csv
from collections import namedtuple

csv_path: Path = Path(r"C:\Users\张周延\Downloads\IOM_Rohingya_WASH_Survey.csv")

with open(csv_path, 'r', encoding='utf-8-sig') as csv_file:
    reader: csv.reader = csv.reader(csv_file)
    headers: List[str] = next(reader)

    g_headers: List[str] = [col for col in headers if col.startswith('G')]

    SurveyRecord = namedtuple(typename='SurveyRecord', field_names=g_headers)

    survey_record_table: List[SurveyRecord] = []

    g_indices = [headers.index(col) for col in g_headers]

    for row in reader:
        g_values = [row[i] for i in g_indices]
        survey_record = SurveyRecord(*g_values)
        survey_record_table.append(survey_record)

print(survey_record_table[0])

#Task2
from datalib import convert_yesno_to_binary
binary_survey_table = convert_yesno_to_binary(survey_record_table)
print(binary_survey_table[0])

#Task3
from datalib import get_categories
print(get_categories(table=binary_survey_table, category_column='G1_1'))

#Task4
from datalib import get_categories, map_categories_to_numbers
mapping_dicts = {}

for col in binary_survey_table[0]._fields:
    unique_values = get_categories(binary_survey_table, col)

    str_values = []
    for v in unique_values:
        if isinstance(v, str):
            str_values.append(v)

    if str_values:
        mapping_dicts[col] = {}
        index = 1

        for val in str_values:
            mapping_dicts[col][val] = index
            index += 1

numeric_survey_table = map_categories_to_numbers(binary_survey_table, mapping_dicts)
print(mapping_dicts["G1_1"])
print(numeric_survey_table[0])

#Task5
from datalib import get_non_numeric_values
get_non_numeric_values(binary_survey_table)

#Task7
#Step1
import pandas as pd
import numpy as np
df = pd.DataFrame.from_records(
    data=numeric_survey_table,
    columns=numeric_survey_table[0]._fields
)
print(df.head())

#Step2
corr = df.corr()
print(corr)

#Step3
df = df.drop(columns=df.columns[df.std() == 0])
corr = df.corr()
m = ~(corr.mask(np.eye(len(corr), dtype=bool)).abs() > 0.95).any()
print(df.columns[m])

#Step4
raw = corr.loc[m, m]
print(raw)
clean_df = df.loc[:, m]
print(clean_df.head())

