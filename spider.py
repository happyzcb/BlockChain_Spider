from bs4 import BeautifulSoup
import requests

def get_html(url):
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "ERROR"

def get_content(url):
    comments = []
    html = get_html(url)
    soup = BeautifulSoup(html,'lxml')
    liTags = soup.find_all('li',attrs={'class':'j_thread_list clearfix'})
    for li in liTags:
        comment = {}
        try:
            comment['title'] = li.find('a',attrs={'class':''})