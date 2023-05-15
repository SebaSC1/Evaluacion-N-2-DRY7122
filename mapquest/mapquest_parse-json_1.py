import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "Santiago, Chile"
dest = "Ovalle, Chile"
key = "Z14rQ09nqscAqKG4IvM9WaLZfMdvOIbT"

url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest}) 


json_data = requests.get(url).json()
print(json_data)
