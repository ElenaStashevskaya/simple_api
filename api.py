#GET, POST, PUT, DELETE
import requests
from base_data import *


def get_posts():
    response = requests.get(URL_POSTS)
    for element in response.json():
        print(element)
# get_posts()

def create_post():
    response = requests.post(url=URL_POSTS, headers=headers, json=body)
    print(response.status_code)
    print(response.json())
# create_post()

def get_one_post():
    response = requests.get(URL_POST)
    print(response.json())
# get_one_post()

def update_post():
    response = requests.put(url=URL_POST, headers=headers, json=body)
    print(response.status_code)
    print(response.json())
# update_post()

def delete_post():
    response = requests.delete(url=URL_POST, headers=headers, json=body)
    print(response.status_code)
    print(response.json())
delete_post()
