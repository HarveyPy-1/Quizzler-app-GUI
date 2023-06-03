import requests

parameters = {
    "amount": 10,
    "type": 'boolean'
}

response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()
question_data = [data["results"][i] for i in range(0, 10)]

