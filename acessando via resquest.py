import json
import requests
r = requests.get("http://api.reddit.com/controversial?limit=5")
if r.status_code == 200:
    print(True)
    json_data = json.loads(r.content)
    print (json_data['data']['children'][1]['data']['title']['score'])
