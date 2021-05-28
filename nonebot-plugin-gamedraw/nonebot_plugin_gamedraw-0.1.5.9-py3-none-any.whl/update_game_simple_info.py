import aiohttp
from .config import DRAW_PATH
from asyncio.exceptions import TimeoutError
from bs4 import BeautifulSoup
from .util import download_img
from urllib.parse import unquote
import bs4

try:
    import ujson as json
except ModuleNotFoundError:
    import json

headers = {'User-Agent': '"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)"'}


async def update_simple_info(url: str, game_name: str) -> 'dict, int':
    try:
        with open(DRAW_PATH + f'{game_name}.json', 'r', encoding='utf8') as f:
            data = json.load(f)
    except (ValueError, FileNotFoundError):
        data = {}
    try:
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(url, timeout=7) as response:
                soup = BeautifulSoup(await response.text(), 'lxml')
                divs = get_char_divs(soup, game_name)
                for div in divs:
                    type_lst = get_type_lst(div, game_name)
                    index = 0
                    for char_lst in type_lst:
                        contents = get_char_lst_contents(char_lst, game_name)
                        for char in contents:
                            data = await retrieve_char_data(char, game_name, data, index)
                        index += 1
    except TimeoutError:
        return {}, 999
    with open(DRAW_PATH + f'{game_name}.json', 'w', encoding='utf8') as wf:
        wf.write(json.dumps(data, ensure_ascii=False, indent=4))
    return data, 200


# 获取所有包含需要图片的divs
def get_char_divs(soup: bs4.BeautifulSoup, game_name: str) -> bs4.element.ResultSet:
    if game_name == 'pcr':
        return soup.find_all('div', {'class': 'tabbertab'})
    if game_name == 'azur':
        return soup.find_all('div', {'class': 'resp-tabs'})


# 拿到所有类型
def get_type_lst(div: bs4.element.Tag, game_name: str):
    if game_name in ['pcr', 'azur']:
        return div.find('div', {'class': 'resp-tabs-container'}).find_all('div', {'class': 'resp-tab-content'})


# 获取所有角色div
def get_char_lst_contents(char_lst: bs4.element.Tag, game_name: str):
    contents = []
    # print(len(char_lst.find_all('tr')))
    if game_name == 'pcr':
        contents = char_lst.contents
    if game_name == 'azur':
        contents = char_lst.find('table').find('tbody').contents[-1].find('td').contents
    return [x for x in contents if x != '\n']


azur_type = {
    '0': '驱逐',
    '1': '轻巡',
    '2': '重巡',
    '3': '超巡',
    '4': '战巡',
    '5': '战列',
    '6': '航母',
    '7': '航站',
    '8': '轻航',
    '9': '重炮',
    '10': '维修',
    '11': '潜艇',
    '12': '运输',
}


# 整理数据
async def retrieve_char_data(char: bs4.element.Tag, game_name: str, data: dict, index: int = 0) -> dict:
    member_dict = {}
    if game_name == 'pcr':
        member_dict = {
            '头像': unquote(char.find('img', {'class': 'img-kk'})['src']),
            '名称': char.find('a')['title'],
            '星级': 3 - index}
    if game_name == 'azur':
        char = char.find('td').find('div')
        avatar_img = char.find('a').find('img')
        try:
            member_dict['头像'] = unquote(str(avatar_img['srcset']).split(' ')[-2])
        except KeyError:
            member_dict['头像'] = unquote(str(avatar_img['src']).split(' ')[-2])
        member_dict['名称'] = str(avatar_img['alt'])[: str(avatar_img['alt']).find('头像')]
        star = char.find('div').find('img')['alt']
        if star == '舰娘头像外框普通.png':
            star = 1
        elif star == '舰娘头像外框稀有.png':
            star = 2
        elif star == '舰娘头像外框精锐.png':
            star = 3
        elif star == '舰娘头像外框超稀有.png':
            star = 4
        elif star == '舰娘头像外框海上传奇.png':
            star = 5
        elif star in ['舰娘头像外框最高方案.png', '舰娘头像外框决战方案.png', '舰娘头像外框超稀有META.png']:
            star = 6
        member_dict['星级'] = star
        member_dict['类型'] = azur_type[str(index)]
    await download_img(member_dict['头像'], game_name, member_dict['名称'])
    data[member_dict['名称']] = member_dict
    print(f'{member_dict["名称"]} is update...')
    return data
