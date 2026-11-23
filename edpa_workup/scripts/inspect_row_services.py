import requests

urls = [
    "https://gis.franklincountyohio.gov/hosting/rest/services/Engineer/CadastralFramework/MapServer?f=pjson",
    "https://apps.lickingcounty.gov/arcgis/rest/services/TaxMapWeb/TAXMAPWEB/MapServer?f=pjson",
]
for url in urls:
    try:
        response = requests.get(url, timeout=40)
        print("URL", response.url, "status", response.status_code, "bytes", len(response.content))
        data = response.json()
        print("layers", [(layer["id"], layer["name"]) for layer in data.get("layers", [])])
        print("tables", [(table["id"], table["name"]) for table in data.get("tables", [])])
    except Exception as error:
        print(type(error).__name__, str(error))
