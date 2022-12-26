from dotenv import load_dotenv
import asyncio, time, os, requests

load_dotenv()

url = "https://ocitkowski.pythonanywhere.com/api/v1/notes/"

TOKEN_API = os.getenv('TOKEN_API')
BearerTOKEN_API = f"Bearer {TOKEN_API}"
authorization = {"Authorization": BearerTOKEN_API}
params = {'limit': '10', 'offset': '10'}

# params = {}
# params.limit = '10'
# params.offset = '10'
# params.Authorization = BearerTOKEN_API


TOKEN_API = '82603ae1dd2d9c22a63309297103a261b1923369'


# async def main():
#     task_1 = asyncio.create_task(my_function_sec(1))
#     task_2 = asyncio.create_task(my_function_sec(5))
#
#     await task_1
#     await task_2


if __name__ == '__main__':
    # for i in range(10):
        # asyncio.run(main())
    response = requests.get(url, headers=authorization, params=params).json()

    print(response)


# class GetDataByURL:
#     def __init__(self, url, params):
#         self.TOKEN_API = os.getenv('TOKEN_API')
#         self.url = url
#         self.params = params
#
#     async def asyncio_get(self):
#         task = asyncio.create_task(requests.get(self.url, headers={self.authorization, params}))
#         return await task
