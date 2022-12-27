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
        self.metod = None

        asyncio.run(self._asyncio_data())

    def __str__(self):
        return self.metod

    def _set_authorization(self):
        BearerTOKEN_API = f"Bearer {os.getenv('TOKEN_API')}"
        self.authorization = {"Authorization": BearerTOKEN_API}
        return self.authorization

    async def _data(self):
        pass

    async def _asyncio_data(self):
        task = asyncio.create_task(self._data())
        return await task


class GetAPIMixin:

    async def get_data(self):
        await asyncio.sleep(self.delay)
        response = requests.get(self.url, headers=self.authorization, params=self.params).json()
        self.response = response

    async def _asyncio_data(self):
        task = asyncio.create_task(self.get_data())
        return await task


class NotesAPIByURL:
    def __init__(self, url, metod, params=None, id=None, json=None, delay=0):
        self.url = url
        self.params = params
        self.authorization = self.__set_authorization()
        self.response = None
        self.metod = metod
        self.delay = delay
        self.json = json
        self.id = id

        asyncio.run(self.__asyncio_get_data())

    def __str__(self):
        return self.metod

    def __set_authorization(self):
        BearerTOKEN_API = f"Bearer {os.getenv('TOKEN_API')}"
        self.authorization = {"Authorization": BearerTOKEN_API}
        return self.authorization

    async def _get_data(self):
        await asyncio.sleep(self.delay)
        response = requests.get(self.url, headers=self.authorization, params=self.params).json()
        self.response = response

    async def _post_data(self):
        await asyncio.sleep(self.delay)
        response = requests.post(self.url, headers=self.authorization, json=self.json).json()
        self.response = response

    async def _patch_data(self):
        await asyncio.sleep(self.delay)
        url_whis_id = self.__add_id_for_url(self.id)
        response = requests.patch(url_whis_id, headers=self.authorization, json=self.json).json()
        self.response = response

    async def _del_data(self):
        await asyncio.sleep(self.delay)
        url_whis_id = self.__add_id_for_url(self.id)
        response = requests.delete(url_whis_id, headers=self.authorization).json()
        self.response = response

    def __add_id_for_url(self, id=None):
        if id == None:
            return f'{self.url}{self.json["id"]}/'
        else:
            return f'{self.url}{id}/'

    async def __asyncio_get_data(self):
        if self.metod == choise_metod[0]:
            task = asyncio.create_task(self._get_data())
        elif self.metod == choise_metod[1]:
            task = asyncio.create_task(self._post_data())
        elif self.metod == choise_metod[2]:
            task = asyncio.create_task(self._patch_data())
        elif self.metod == choise_metod[3]:
            task = asyncio.create_task(self._del_data())
        else:
            # task = asyncio.create_task(self.__post_notes)
            pass

        return await task


if __name__ == '__main__':
    params1 = {'limit': '10', 'offset': '10'}
    params2 = {'limit': '10', 'offset': '15'}

    gd1 = NotesAPIByURL(url, params=params1, metod=choise_metod[0])
    gd2 = NotesAPIByURL(url, metod=choise_metod[1], json=post_data)
    id = gd2.response['id']
    gd3 = NotesAPIByURL(url, metod=choise_metod[2], id=id)
    gd4 = NotesAPIByURL(url, metod=choise_metod[3], json=post_data)

    print(f"{gd1} // {gd1.response} // {gd1}")
    print(f"{gd2} // {gd2.response} // {gd2}")
    print(f"{gd3} // {gd3.response} // {gd3}")

    print(f"{gd4} // {gd4.response} // {gd4}")
