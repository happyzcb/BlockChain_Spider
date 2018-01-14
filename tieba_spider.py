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

def get_content(url):
    comments = []
    html = get_html(url)
    soup = BeautifulSoup(html,'lxml')
    liTags = soup.find_all('li',attrs={'class':' j_thread_list clearfix'})
    for li in liTags:
        comment = {}
        try:
            comment['title'] = li.find('a',attrs={'class':'j_th_tit'}).text.strip()
            comment['link'] = "http://tieba.baidu.com/" + li.find('a',attrs={'class':'j_th_tit'})['href']
            comment['name'] = li.find('span',attrs={'class':'tb_icon_author'}).text.strip()
            comment['time'] = li.find('span',attrs={'class':'pull-right is_show_create_time'}).text.strip()
            comment['replyNum'] = li.find('span',attrs={'class':'threadlist_rep_num center_text'}).text.strip()
            comments.append(comment)
        except:
            print('something is wrong!')

    return comments

def SaveToFile(dict):
    '''
    Save the result to local file
    :param dict:
    :return:
    '''
    with open('TTBT.txt','a+') as f:
        for comment in dict:
            f.write('标题： {} \t 链接： {} \t 发帖人： {} \t 发帖时间：{} \t 回复数量：{} \n'.format(
                comment['title'], comment['link'], comment['name'], comment['time'], comment['replyNum']))

        print('Current page finished!')

def main(base_url,deep):
    url_list = []
    for i in range(0,deep):
        url_list.append(base_url + '&pn=' + str(50 * i))
    print('Already download all pages. Now processing information...')

    for url in url_list:
        content = get_content(url)
        SaveToFile(content)
    print('Process done! All information have been saved to local file.')

if __name__ == '__main__':
    base_url = 'http://tieba.baidu.com/f?kw=%E7%94%9F%E6%B4%BB%E5%A4%A7%E7%88%86%E7%82%B8'
    deep = 2
    main(base_url,deep)

