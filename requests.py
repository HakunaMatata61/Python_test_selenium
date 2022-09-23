import requests

url = "https://auth.timetta.com/connect/token"

payload='client_id=external&scope=all%20offline_access&grant_type=password&username={{NesterovA@test-task.ru}}&password={{gG9NfM}}'
headers = {}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

