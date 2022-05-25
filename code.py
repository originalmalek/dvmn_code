import os
import requests
from dotenv import load_dotenv


def add_item_to_cart(access_token):
    headers = {
        'Authorization': access_token,
        'Content-Type': 'application/json',
    }

    json_data = { "data": { "id": "8389cff3-6e22-4ab7-b06b-ee814b9c3900", "type": "cart_item", "quantity": 1 } }

    response = requests.post('https://api.moltin.com/v2/carts/abcd/items', headers=headers, json=json_data)
    print(response.json())



def get_cart(access_token):
    headers = {
        'Authorization': access_token,
    }

    response = requests.get('https://api.moltin.com/v2/carts/abcd', headers=headers)
    response.raise_for_status()
    print(response.json())


def get_products(access_token):
    headers = {
        'Authorization': access_token,
    }

    response = requests.get('https://api.moltin.com/pcm/products', headers=headers)
    response.raise_for_status()
    print(response.json())


def get_access_token(ep_client_id, ep_client_secret):
    data = {
        'client_id': ep_client_id,
        'client_secret': ep_client_secret,
        'grant_type': 'client_credentials',
    }

    response = requests.post('https://api.moltin.com/oauth/access_token', data=data)
    response.raise_for_status()
    return response.json()['access_token']


def main():
    load_dotenv()
    ep_store_id = os.getenv('EP_STORE_ID')
    ep_client_id = os.getenv('EP_CLIENT_ID')
    ep_client_secret = os.getenv('EP_CLIENT_SECRET')

    access_token = get_access_token(ep_client_id, ep_client_secret)
    get_products(access_token)
    add_item_to_cart(access_token)
    get_cart(access_token)


if __name__ == '__main__':
    main()
