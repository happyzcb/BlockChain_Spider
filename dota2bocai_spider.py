from bs4 import BeautifulSoup
import requests

def get_html(url):
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status()
        # r.encoding = r.apparent_encoding
        r.encoding = 'utf-8'
        return r.text
    except:
        return "ERROR"

