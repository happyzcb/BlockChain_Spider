from bs4 import BeautifulSoup
import bs4
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

def print_reslut(url):
    html = get_html(url)
    soup = BeautifulSoup(html)
    match_list = soup.find_all('div',attrs={'class':'matchmain_bisai_qukuai'})
    for match in match_list:
        time = match.find('div',attrs={'class':'whenm'}).text.strip()
        teamname = match.find_all('span',attrs={'class':'team_name'})
        if(type(teamname[0].string) == bs4.element.Comment):
            teamname_1 = '暂无队名'
        else:
            teamname_1 = teamname[0].string

        team1_support_level = match.find('span',)