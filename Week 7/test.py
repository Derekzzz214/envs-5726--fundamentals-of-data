from pprint import pprint
import requests

epqs_url = ('https://epqs.nationalmap.gov/v1/json?'
            'x=-75.19128&y=39.95140&units=Feet&wkid=4326&includeDate=False')

response = requests.get(url=epqs_url)
result = response.json()

pprint(result, width=30)
