from dotenv import load_dotenv
import asyncio, os, requests

load_dotenv()

url = "https://ocitkowski.pythonanywhere.com/api/v1/notes/"
TOKEN_API = os.getenv('TOKEN_API')
BearerTOKEN_API = f"Bearer {TOKEN_API}"
authorization = {"Authorization": BearerTOKEN_API}
choise_metod = ["GET", "POST", "PATCH", "DEL"]

post_data = {
    "id": 1154,
    "owner": 6,
    "source": 12,
    "text": "SHTuIlKSjEzooooooooscKrycsAUhh555hhh",
    "comment": "Phone appear ahead soldier summer individual step late especially back555hhhh.",
    "key": 12,
    "status": "A",
    "date_update": "2022-12-23"
}


class NotesAPIByURL:
    def __init__(self, url, metod, params=None, json=None, delay=0):
        self.url = url
        self.params = params
        self.authorization = self.__set_authorization()
        self.response = None
        self.metod = metod
        self.delay = delay
        self.json = json

        asyncio.run(self.__asyncio_get_notes())

    def __str__(self):
        return self.metod

    def __set_authorization(self):
        BearerTOKEN_API = f"Bearer {os.getenv('TOKEN_API')}"
        self.authorization = {"Authorization": BearerTOKEN_API}
        return self.authorization

    async def _get_notes(self):
        await asyncio.sleep(self.delay)
        response = requests.get(self.url, headers=self.authorization, params=self.params).json()
        self.response = response

    async def _post_notes(self):
        await asyncio.sleep(self.delay)
        response = requests.post(self.url, headers=self.authorization, json=self.json).json()
        self.response = response

    async def _patch_notes(self):
        await asyncio.sleep(self.delay)
        url_whis_id = self.__add_id_for_url()
        response = requests.patch(url_whis_id,  headers=self.authorization, json=self.json).json()
        self.response = response

    async def _del_notes(self):
        await asyncio.sleep(self.delay)
        url_whis_id = self.__add_id_for_url()
        response = requests.delete(url_whis_id, headers=self.authorization).json()
        self.response = response

    def __add_id_for_url(self):
        return f'{self.url}{self.json["id"]}/'
        pass

    async def __asyncio_get_notes(self):
        if self.metod == choise_metod[0]:
            task = asyncio.create_task(self._get_notes())
        elif self.metod == choise_metod[1]:
            task = asyncio.create_task(self._post_notes())
        elif self.metod == choise_metod[2]:
            task = asyncio.create_task(self._patch_notes())
        elif self.metod == choise_metod[3]:
            task = asyncio.create_task(self._del_notes())
        else:
            # task = asyncio.create_task(self.__post_notes)
            pass

        return await task


if __name__ == '__main__':
    params1 = {'limit': '10', 'offset': '10'}
    params2 = {'limit': '10', 'offset': '15'}

    # gd1 = NotesAPIByURL(url, params=params1, metod=choise_metod[0])
    gd2 = NotesAPIByURL(url, metod=choise_metod[1], json=post_data)
    gd3 = NotesAPIByURL(url, metod=choise_metod[2], json=post_data)
    gd4 = NotesAPIByURL(url, metod=choise_metod[3], json=post_data)
    # print(post_data['id'])
    print(gd2.response['id'])
    print(gd3.response)
    print(gd4.response)

