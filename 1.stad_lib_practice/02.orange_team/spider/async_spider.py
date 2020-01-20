import aiohttp
import asyncio
import time
from pyquery import PyQuery as pq

async def decode_html(html_content):
    doc=pq(html_content)
    des=''
    for li in doc.items("#phrsListTab .trans-container ul li"):
        des+=li.text()
    return des

async def fetch(session, word):
    url='http://dict.youdao.com/w/eng/{}'.format(word)
    async with session.get(url) as response:
        return {'word':word,'data':await response.text()}


async def main(words):
    async with aiohttp.ClientSession() as session:
        tasks=[fetch(session, word) for word in words]
        res_list = await asyncio.gather(*tasks)
        for index,each in enumerate(res_list):
            print (index+1,each['word'],'->',await(decode_html(each['data'])))



def run_as_asyncio(words):
    asyncio.run(main(words=words))


if __name__ == '__main__':
    words = ['china', 'english', 'temperaments'] * 100
    run_as_asyncio(words)

