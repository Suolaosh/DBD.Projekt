import requests
import json
base_url = 'http://smartdp.applinzi.com/php/postwind.php'

data = {
    'time': '1',
    'state': '2',
    #'friends': ['zhang3', 'li4']
}
response = requests.post(base_url, data=data)
#response = requests.post(f'{base_url}post', data=json.dumps(data))
print(response.text)

