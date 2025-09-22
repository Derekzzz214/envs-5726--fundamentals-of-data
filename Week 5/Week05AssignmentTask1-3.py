from pathlib import Path
import json
import csv

json_path = Path(r"C:\Users\张周延\Downloads\Trase_CIV_Cocoa_SupplyChain_Data.json")

with open(json_path) as f:
    data = json.load(f)

records = data["cote_divoire_cocoa_v1_1_1"]["data"]

data_headers = [
    "trader_group",
    "country_of_destination",
    "cocoa_deforestation_15_years_total_exposure",
    "cocoa_net_emissions_15_years_total"
]
data_table = []
for record in records:
    trader_group = record["supply_chain_data"]["trader_group"]
    country_of_destination = record["supply_chain_data"]["country_of_destination"]
    cocoa_deforestation_15_years_total_exposure = record["cocoa_data"]["cocoa_deforestation_15_years_total_exposure"]
    cocoa_net_emissions_15_years_total = record["cocoa_data"]["cocoa_net_emissions_15_years_total"]
    data_table.append([trader_group, country_of_destination, cocoa_deforestation_15_years_total_exposure, cocoa_net_emissions_15_years_total])

output_path = Path(r"C:\Users\张周延\PycharmProjects\envs-5726--fundamentals-of-data\Week 5\Trase_CIV_Cocoa_SupplyChain_Data.csv")
with open(output_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(data_headers)
    writer.writerows(data_table)


trader_summary_dict = {}
country_summary_dict = {}
for record in records:
    trader = record["supply_chain_data"]["trader_group"]
    country = record["supply_chain_data"]["country_of_destination"]

    deforestation = float(record["cocoa_data"]["cocoa_deforestation_15_years_total_exposure"])
    emissions = float(record["cocoa_data"]["cocoa_net_emissions_15_years_total"])

    if trader not in trader_summary_dict:
        trader_summary_dict[trader] = {
            "cocoa_deforestation_list": [deforestation],
            "cocoa_net_emissions_list": [emissions]
        }
    else:
        trader_summary_dict[trader]["cocoa_deforestation_list"].append(deforestation)
        trader_summary_dict[trader]["cocoa_net_emissions_list"].append(emissions)

    if country not in country_summary_dict:
        country_summary_dict[country] = {
            "cocoa_deforestation_list": [deforestation],
            "cocoa_net_emissions_list": [emissions]
        }
    else:
        country_summary_dict[country]["cocoa_deforestation_list"].append(deforestation)
        country_summary_dict[country]["cocoa_net_emissions_list"].append(emissions)

trader_output = Path(r"C:\Users\张周延\PycharmProjects\envs-5726--fundamentals-of-data\Week 5\Trader_Summary_JSON.json")
country_output = Path(r"C:\Users\张周延\PycharmProjects\envs-5726--fundamentals-of-data\Week 5\Country_Summary_JSON.json")

with open(trader_output, "w") as json_file:
    json.dump(trader_summary_dict, json_file, sort_keys=True)

with open(country_output, "w") as json_file:
    json.dump(country_summary_dict, json_file, sort_keys=True)


def summarize(records, group_key, value_key, output_csv):
    summary_dict = {}

    for record in records:
        if group_key == "trader_group":
            group = record["supply_chain_data"]["trader_group"]
        elif group_key == "country_of_destination":
            group = record["supply_chain_data"]["country_of_destination"]

        value = float(record["cocoa_data"][value_key])

        if group not in summary_dict:
            summary_dict[group] = value
        else:
            summary_dict[group] += value

    max_sum = max(summary_dict.values())

    filtered = {}
    for k, v in summary_dict.items():
        if v>= 0.1*max_sum:
            filtered[k] = v

    with open(output_csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["group_key", f"total_{value_key}"])
        for k, v in filtered.items():
            writer.writerow([k, v])

summarize(records, "trader_group", "cocoa_deforestation_15_years_total_exposure","Trader_Sum_Deforestation.csv")
summarize(records, "trader_group", "cocoa_net_emissions_15_years_total","Trader_Sum_Emissions.csv")
summarize(records, "country_of_destination", "cocoa_deforestation_15_years_total_exposure","Country_Sum_Deforestation.csv")
summarize(records, "country_of_destination", "cocoa_net_emissions_15_years_total","Country_Sum_Emissions.csv")


