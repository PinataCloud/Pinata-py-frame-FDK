import requests
import os

def send_post_request(requestBody):
    url = "https://api.pinata.cloud/farcaster/frames/interactions"
    payload = {
        "frame_id": "Your Unique Frame ID as a String",
        "data": requestBody
    }
    headers = {
        "Authorization": f"Bearer {os.environ.get('PINATA_JWT')}",
        "Content-Type": "application/json"
    }
    response = requests.post(url, json=payload)
    return response.json()