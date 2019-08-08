import requests
from bs4 import BeautifulSoup as bs
import re

def pars(url):
    headers = {'accept': '*/*',
               'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
    result = []
    session = requests.Session()
    request = session.get(url, headers=headers)
    if request.status_code == 200:
        soup = bs(request.content, 'lxml')
        links = soup.find_all('a', attrs={'class': ['b-advItem', 'b-advItem_pinned']})
        for a in links:
            hrefs = a['href']
            result.append(hrefs)
    return result

def parsMore(url):
    headers = {'accept': '*/*',
               'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
    result = []
    session = requests.Session()
    request = session.get(url, headers=headers)
    if request.status_code == 200:
        soup = bs(request.content, 'lxml')
        links = soup.find_all('a', attrs={'class': ['b-advItem', 'b-advItem_pinned']})
        for a in links:
            hrefs = a['href']
            items = session.get(hrefs, headers=headers)
            if items.status_code == 200:
                item = bs(items.content, 'lxml')
                s = item.find('h1', attrs={'class': ['b-title', 'b-title_type_h1']}).text
                title = ' '.join(s.split())
                p = item.find('div', attrs={'class': 'b-text_color_red'}).text
                price = ' '.join(p.split())
                m = item.find('div', attrs={'data-triggers-container': 'true',
                                            'class': 'b-media-cont b-media-cont_relative'}).text
                ms = ''.join(m.split('\n')[0])
                media = re.findall('[А-Я][^А-Я]*', ms)
                del media[3]
                del media[3]
                info = {'title': title,
                        'price': price,
                        'info': media}
                result.append(info)

    return result
