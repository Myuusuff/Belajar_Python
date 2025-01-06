import requests

def get_public_ip():
    # Menggunakan API ipinfo.io untuk mendapatkan IP publik
    url = "https://ipinfo.io/json"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        print(f"IP Publik: {data['ip']}")
        print(f"Lokasi: {data['city']}, {data['region']}, {data['country']}")
    else:
        print(f"Error: {response.status_code}")

get_public_ip()
