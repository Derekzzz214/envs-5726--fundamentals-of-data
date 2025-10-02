import csv
with open(r"C:\Users\张周延\Downloads\EJScreen_BlockGroup_SocialVulnerability.csv", newline="") as f:
    reader = csv.reader(f)
    target_headers = next(reader)
    target_table = [row for row in reader]
with open(r"C:\Users\张周延\Downloads\EJSCREEN_BlockGroup_Hazards.csv", newline="") as f:
    reader = csv.reader(f)
    join_headers = next(reader)
    join_table = [row for row in reader]

unique_id_name_target = 'ID_SOCVUL'
unique_id_name_join = 'ID_HAZ'

join_dict = {}
for row in join_table:
    unique_id = row[join_headers.index(unique_id_name_join)]
    join_dict[unique_id] = row
target_dict = {}
for row in target_table:
    unique_id = row[target_headers.index(unique_id_name_target)]
    target_dict[unique_id] = row

joined_headers = target_headers + join_headers
outer_joined_table = []
for target_row in target_table:
    unique_id = target_row[target_headers.index(unique_id_name_target)]
    if unique_id in join_dict:
        join_row = join_dict[unique_id]
    else:
        join_row = [None] * len(join_headers)
    outer_joined_table.append(target_row + join_row)

for unique_id in join_dict:
    if unique_id not in target_dict:
        join_row = join_dict[unique_id]
        target_row = [None] * len(target_headers)
        outer_joined_table.append(target_row + join_row)

with open(r"C:\Users\张周延\PycharmProjects\envs-5726--fundamentals-of-data\Week 6\FullOuterJoin_Task1.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(joined_headers)
    writer.writerows(outer_joined_table)


id_socvul_index = joined_headers.index('ID_SOCVUL')
id_haz_index = joined_headers.index('ID_HAZ')
total_rows = len(outer_joined_table)

vaild_socvul = 0
for row in outer_joined_table:
    if row[id_socvul_index]:
        vaild_socvul += 1

valid_haz = 0
for row in outer_joined_table:
    if row[id_haz_index]:
        valid_haz += 1

print(f"There are {vaild_socvul} valid ID_SOCVUL out of {total_rows} total joined rows")
print(f"There are {valid_haz} valid ID_HAZ out of {total_rows} total joined rows")


target_id_index = target_headers.index("ID_SOCVUL")
target_id_set = set([row[target_id_index] for row in target_table])

join_id_index = join_headers.index("ID_HAZ")
join_id_set = set([row[join_id_index] for row in join_table])

inner_ids = target_id_set.intersection(join_id_set)
inner_count = len(inner_ids)
total_rows = len(outer_joined_table)

print(f"There are {inner_count} inner joined rows of {total_rows} total Block Groups")