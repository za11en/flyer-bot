import requests
from datetime import datetime
import os

# 1. Get current date for the API
today = datetime.now().strftime('%Y-%m-%d')
url = f"https://metrodigital-apim.azure-api.net/api/flyers/659/en?date={today}"

headers = {
    "ocp-apim-subscription-key": "0defd42b9de9412488327864774fbfca",
    "banner": "62015981ed29a2a604a206b4",
    "x-api-version": "3.0"
}

def download_flyer():
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()

        if data.get('flyers'):
            pdf_url = data['flyers'][0]['pdf']
            print(f"Downloading flyer from: {pdf_url}")
            
            # Download the actual PDF content
            pdf_data = requests.get(pdf_url).content
            
            # Save it to the repo folder
            with open("latest_flyer.pdf", "wb") as f:
                f.write(pdf_data)
            print("Flyer saved successfully.")
        else:
            print("No flyer found for today.")
    except Exception as e:
        print(f"Error: {e}")
        exit(1)

if __name__ == "__main__":
    download_flyer()