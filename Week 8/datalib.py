#Task2
from typing import List, Any, Dict

def convert_yesno_to_binary(table: List[tuple]) -> List[tuple]:

    RecordClass = type(table[0])
    converted_table: List[RecordClass] = []

    for row in table:
        row_values = list(row)
        new_values: List[Any] = []

        for value in row_values:
            if value == 'Yes':
                new_values.append(1)
            elif value in ('No', '', 'Do not know'):
                new_values.append(0)
            else:
                new_values.append(value)

        new_row = RecordClass(*new_values)
        converted_table.append(new_row)

    return converted_table

#Task3
def get_categories(table: List[tuple], category_column: str) -> set:

    column_values = [getattr(row, category_column) for row in table]
    unique_values = set(column_values)
    return unique_values

#Task4
def map_categories_to_numbers(table: List[tuple], mapping_dicts: Dict[str, Dict[str, int]]) -> List[tuple]:

    RowClass = type(table[0])
    converted_table: List[RowClass] = []

    for row in table:
        row_data = row._asdict()
        for column, mapping in mapping_dicts.items():
            value = row_data.get(column)
            if isinstance(value, str) and value in mapping:
                row_data[column] = mapping[value]
            elif value == 0 or value == '' or value is None:
                row_data[column] = 0
        converted_table.append(RowClass(**row_data))

    return converted_table

#Task5
def get_non_numeric_values(table):

    for i in range(len(table)):
        row = table[i]

        for col, value in row._asdict().items():

            if not isinstance(value, (int, float, complex)):
                print(f"Row {i} Column {col}: {value}")


