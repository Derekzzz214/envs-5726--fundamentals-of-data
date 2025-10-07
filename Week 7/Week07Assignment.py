#Task1
import urllib
import requests
import csv
from pprint import pprint

fema_hazard_zones_url = "https://hazards.fema.gov/arcgis/rest/services/public/NFHL/MapServer/28/query"

input_path  = r"C:\Users\张周延\Downloads\USEIA_Petroleum_Refineries_By_Nearest_Major_City.csv"
output_path = r"C:\Users\张周延\PycharmProjects\envs-5726--fundamentals-of-data\Week 7\USEIA_Petroleum_Refineries_FEMA_Zones.csv"

with open(input_path, 'r', encoding='utf-8') as infile:
    reader = csv.reader(infile)
    header = next(reader)
    refinery_data = list(reader)

header.append("FEMA_Hazard_Zone")

with open(output_path, 'w', newline='', encoding='utf-8') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(header)

    for row in refinery_data:
        lat = row[-5]
        lon = row[-4]

        query = {
            'geometry': f'{lon},{lat}',
            'inSR': '4326',
            'geometryType': 'esriGeometryPoint',
            'spatialRel': 'esriSpatialRelIntersects',
            'outFields': 'ZONE_SUBTY',
            'returnGeometry': 'false',
            'f': 'json'
        }

        encoded_query = urllib.parse.urlencode(query)
        fema_request_url = fema_hazard_zones_url + '?' + encoded_query

        fema_response = requests.get(fema_request_url).json()

        if "features" in fema_response and len(fema_response["features"]) > 0:
            zone = fema_response["features"][0]["attributes"].get("ZONE_SUBTY", "No Data")
            if not zone:
                zone = "No Data"
        else:
            zone = "No Data"

        row.append(zone)
        writer.writerow(row)
        pprint({"Latitude": lat, "Longitude": lon, "FEMA_Hazard_Zone": zone})

print("Task 1 completed successfully.")
print(f"Output saved to: {output_path}")

#Task2
osrm_output_path = r"C:\Users\张周延\PyCharmProjects\envs-5726--fundamentals-of-data\Week 7\USEIA_Petroleum_Refineries_FEMA_Zones_DriveDuration.csv"

with open(output_path, 'r', encoding='utf-8') as infile:
    reader = csv.reader(infile)
    header = next(reader)
    refinery_data = list(reader)

header.append("DriveDuration_Seconds")

def get_drive_duration(lat1, lon1, lat2, lon2):
    osrm_url = f"https://router.project-osrm.org/route/v1/driving/{lon1},{lat1};{lon2},{lat2}?overview=false&steps=false"
    data = requests.get(url = osrm_url).json()
    duration = data["routes"][0]["duration"]
    return duration

with open(osrm_output_path, 'w', newline='', encoding='utf-8') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(header)

    for row in refinery_data:
        lat1 = row[header.index("Latitude")]
        lon1 = row[header.index("Longitude")]
        lat2 = row[header.index("NearestMajorCity_Latitude")]
        lon2 = row[header.index("NearestMajorCity_Longitude")]

        duration = get_drive_duration(lat1, lon1, lat2, lon2)

        row.append(duration)
        writer.writerow(row)

        print(f"{lat1},{lon1} → {lat2},{lon2}: {duration}s")

print(f"Output saved to: {osrm_output_path}")
