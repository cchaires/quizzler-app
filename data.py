import requests

URL = "https://opentdb.com/api.php"
PARAMETERS = {
    "amount": 15,
    "type": "boolean",
    "category": 18,
}
response = requests.get(url=URL, params=PARAMETERS)
response.raise_for_status()
data = response.json()
cleaned_data = {k: v for k, v in data.items() if k == 'results'}
question_data = cleaned_data['results']
