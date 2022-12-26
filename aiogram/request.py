from dotenv import load_dotenv
import asyncio, os, requests

load_dotenv()

url = "https://ocitkowski.pythonanywhere.com/api/v1/notes/"

TOKEN_API = os.getenv('TOKEN_API')
BearerTOKEN_API = f"Bearer {TOKEN_API}"
authorization = {"Authorization": BearerTOKEN_API}
params1 = {'limit': '10', 'offset': '10'}
params2 = {'limit': '10', 'offset': '15'}

TOKEN_API = '82603ae1dd2d9c22a63309297103a261b1923369'


class GetDataByURL:
    def __init__(self, url, params):
        self.url = url
        self.params = params
        self.authorization = self.__set_authorization()
        self.notes = []

    def __set_authorization(self):
        BearerTOKEN_API = f"Bearer {os.getenv('TOKEN_API')}"
        self.authorization = {"Authorization": BearerTOKEN_API}
        return self.authorization

    async def print_data(self, delay):
        await asyncio.sleep(delay)
        response = requests.get(self.url, headers=self.authorization, params=self.params).json()
        self.notes = response['results']
        # for i in response['results']:
        #     print(i)

    async def asyncio_get(self):
        task = asyncio.create_task(self.print_data(1))
        return await task


if __name__ == '__main__':
    gd1 = GetDataByURL(url, params1)
    gd2 = GetDataByURL(url, params2)

    asyncio.run(gd1.asyncio_get())
    asyncio.run(gd2.asyncio_get())

    for i in gd1.notes:
        print(i)

