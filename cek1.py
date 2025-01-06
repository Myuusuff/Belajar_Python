import requests

response = requests.get("https://api.ipify.org?format=json")
data = response.json()

print(f"IP Publik Anda: {data['ip']}")
