from dotenv import load_dotenv
import asyncio, os, requests

load_dotenv()

url = "https://ocitkowski.pythonanywhere.com/api/v1/notes/"
TOKEN_API = os.getenv('TOKEN_API')
BearerTOKEN_API = f"Bearer {TOKEN_API}"
authorization = {"Authorization": BearerTOKEN_API}

post_data = {
    "id": 1165,
    "owner": 6,
    "source": 12,
    "text": "SHTuIlKSjEzooooooooscKrycsAUhh555hhh",
    "comment": "Phone appear ahead soldier summer individual step late especially back555hhhh.",
    "key": 12,
    "status": "A",
    "date_update": "2022-12-23"
}


class APIByURL:
    def __init__(self, url, delay=0):
        self.url = url
        self.authorization = self._set_authorization()
        self.delay = delay
        self.response = None

    def _set_authorization(self):
        BearerTOKEN_API = f"Bearer {os.getenv('TOKEN_API')}"
        self.authorization = {"Authorization": BearerTOKEN_API}
        return self.authorization

    async def _get_response(self):
        pass

    async def asyncio_get_task(self):
        pass


class GetMixin:

    async def _get_response(self, params):
        await asyncio.sleep(self.delay)
        response = requests.get(self.url, headers=self.authorization, params=params).json()
        self.response = response

    async def asyncio_get_task(self, params):
        task = asyncio.create_task(self._get_response(params))
        return await task


class GetByURL(GetMixin, APIByURL):
    def __str__(self):
        return f'GET -- {self.url}'


if __name__ == '__main__':

    params1 = {'limit': '10', 'offset': '10'}
    params2 = {'limit': '10', 'offset': '15'}


    get_notes = GetByURL(url=url)

    asyncio.run(get_notes.asyncio_get_task(params=params1))

    print(get_notes.response['results'])

