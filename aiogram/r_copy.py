from dotenv import load_dotenv
import asyncio, os, requests

load_dotenv()

url = "https://ocitkowski.pythonanywhere.com/api/v1/notes/"
TOKEN_API = os.getenv('TOKEN_API')
BearerTOKEN_API = f"Bearer {TOKEN_API}"
authorization = {"Authorization": BearerTOKEN_API}


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


class PostMixin:

    async def _get_response(self, json):
        await asyncio.sleep(self.delay)
        response = requests.post(self.url, headers=self.authorization, json=json).json()
        self.response = response

    async def asyncio_get_task(self, json):
        task = asyncio.create_task(self._get_response(json))
        return await task


class PatchMixin:

    def __add_id_for_url(self, id=None):
        return f'{self.url}{id}/'

    async def _get_response(self, json, id):
        await asyncio.sleep(self.delay)
        url = self.__add_id_for_url(id)
        response = requests.patch(url, headers=self.authorization, data=json).json()
        self.response = response

    async def asyncio_get_task(self, json, id):
        task = asyncio.create_task(self._get_response(json, id))
        return await task


class DelMixin:

    def __add_id_for_url(self, id=None):
        return f'{self.url}{id}/'

    async def _get_response(self, id):
        await asyncio.sleep(self.delay)
        url = self.__add_id_for_url(id)
        response = requests.delete(url, headers=self.authorization)
        self.response = response

    async def asyncio_get_task(self, id):
        task = asyncio.create_task(self._get_response(id))
        return await task


class GetByURL(GetMixin, APIByURL):
    def __str__(self):
        return f'GET by -- {self.url}'


class PostByURL(PostMixin, APIByURL):
    def __str__(self):
        return f'POST by -- {self.url}'


class PatchByURL(PatchMixin, APIByURL):
    def __str__(self):
        return f'Patch by -- {self.url}'


class DelByURL(DelMixin, APIByURL):
    def __str__(self):
        return f'Delete by -- {self.url}'


if __name__ == '__main__':
    # ***********************************************************************
    params1 = {'limit': '1', 'offset': '1'}
    params2 = {'limit': '10', 'offset': '15'}

    get_notes = GetByURL(url=url)
    asyncio.run(get_notes.asyncio_get_task(params=params1))
    print(f'// {get_notes}//  {get_notes.response["results"]} ')
    # ***********************************************************************
    post_data_json = {
        "id": 0,
        "owner": 6,
        "source": 12,
        "text": "S555hhh",
        "comment": "Phone appear ahead soldier summer individual step late especially back555hhhh.",
        "key": 12,
        "status": "A",
        "date_update": "2022-12-23"
    }

    post_notes = PostByURL(url=url)
    asyncio.run(post_notes.asyncio_get_task(json=post_data_json))
    print(f'// {post_notes} // {post_notes.response["id"]} // {post_notes.response} ')
    # ***********************************************************************
    patch_data_json = {
        "id": 1165,
        "owner": 6,
        "source": 12,
        "text": "S555h0000hh",
        "comment": "Phone appear ahead soldier summer individual step late especially back555hhhh.",
        "key": 12,
        "status": "A",
        "date_update": "2022-12-23"
    }

    patch_notes = PatchByURL(url=url)
    asyncio.run(patch_notes.asyncio_get_task(json=patch_data_json, id=post_notes.response["id"]))
    print(f'// {patch_notes} // {patch_notes.response} ')

    # ***********************************************************************

    delete_notes = DelByURL(url=url)
    asyncio.run(delete_notes.asyncio_get_task(id=post_notes.response["id"]))
    print(f'// {delete_notes} // {delete_notes.response} ')

    # ***********************************************************************
