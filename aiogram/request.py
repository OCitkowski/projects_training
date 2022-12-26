from dotenv import load_dotenv
import asyncio, os, requests

load_dotenv()

url = "https://ocitkowski.pythonanywhere.com/api/v1/notes/"
TOKEN_API = os.getenv('TOKEN_API')
BearerTOKEN_API = f"Bearer {TOKEN_API}"
authorization = {"Authorization": BearerTOKEN_API}
choise_metod = ["GET", "POST", "DEL", "PATCH"]

post_data = {
    "id": 0,
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
        self.notes = []
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
        self.notes = response['results']

    async def __post_notes(self):
        await asyncio.sleep(self.delay)
        response = requests.post(self.url, headers=self.authorization, json=self.json).json()
        for i in response:
            print(i)
        # self.notes = response['results']

    async def __asyncio_get_notes(self):
        if self.metod == choise_metod[0]:
            task = asyncio.create_task(self._get_notes())
        elif self.metod == choise_metod[1]:
            task = asyncio.create_task(self.__post_notes())
        elif self.metod == choise_metod[2]:
            pass
        elif self.metod == choise_metod[3]:
            pass
        else:
            # task = asyncio.create_task(self.__post_notes)
            pass

        return await task


if __name__ == '__main__':

    params1 = {'limit': '10', 'offset': '10'}
    params2 = {'limit': '10', 'offset': '15'}

    # gd1 = NotesAPIByURL(url, params=params1, metod=choise_metod[0])
    gd2 = NotesAPIByURL(url, metod=choise_metod[1], json=post_data)

    # for i in gd1.notes:
    #     print(i)
