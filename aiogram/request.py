import requests
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN_API = os.getenv('TOKEN_API')
url = "https://ocitkowski.pythonanywhere.com/api/v1/notes/"

BearerTOKEN_API = f"Bearer {TOKEN_API}"
authorization = {"Authorization": BearerTOKEN_API}
payload = {'limit': '10', 'offset': '10'}

if __name__ == '__main__':

    for i in requests.get(url=url, params=payload, headers=authorization):
        print(i)
