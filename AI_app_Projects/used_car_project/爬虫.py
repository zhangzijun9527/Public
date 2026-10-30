import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

def craw_quotes():
    url = "http://quotes.toscrape.com/"
    headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/156.0.0.0 Safari/537.36 Edg/156.0.0.0'
    }

    print(f'正在请求网页:{url}')

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f'网页获取失败，状态码：{response.status_code}')
        return

    print('网页获取成功')

    soup = BeautifulSoup(response.text, 'html.parser')

    quote_elements = soup.find_all('div', class_='quote')
    all_data = []

    for element in quote_elements:
        text = element.find('span', class_='text').text
        author = element.find('small',class_='author').text

        all_data.append({
            '名言': text,
            '作者': author
        })
    print(f'成功抓取到{len(all_data)}条数据')

    df = pd.DataFrame(all_data)
    df.to_csv('quotes_data.csv', index=False,encoding='utf-8-sig')
    print('数据成功保存')

if __name__ == '__main__':
    craw_quotes()
    time.sleep(2)