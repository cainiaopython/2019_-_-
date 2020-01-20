import requests
from requests import ConnectionError,ConnectTimeout
from pyquery import PyQuery as pq
from pprint import pprint
from collections import OrderedDict
from common.costTime import count_running_time


class Spider:
    def __init__(self):
        self.count=1
        self.headers = {
            'Cookie': 'DICT_UGC=be3af0da19b5c5e6aa4e17bd8d90b28a|; '
                      'webDict_HdAD=%7B%22req%22%3A%22http%3A//dict.youdao.com%'
                      '22%2C%22width%22%3A960%2C%22height%22%3A240%2C%22showtime%22%'
                      '3A5000%2C%22fadetime%22%3A500%2C%22notShowInterval%22%3A3%'
                      '2C%22notShowInDays%22%3Afalse%2C%22lastShowDate%22%3A%22Mon%'
                      '20Nov%2008%202010%22%7D; ___rl__test__cookies=1515809612366;'
                      ' _ntes_nnid=7c7071e6ff37a1f321a28ebd3450279f,1503241340929;'
                      ' OUTFOX_SEARCH_USER_ID_NCOO=1630604769.092356;'
                      ' OUTFOX_SEARCH_USER_ID=-224682605@10.169.0.76;'
                      ' JSESSIONID=abcr9OlYVoIM8dOeXsTdw',
            'Host': 'dict.youdao.com',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
        }
        self.base_url='http://dict.youdao.com/w/eng'


    def get_url(self,word):
        return '{}/{}/'.format(self.base_url, word)

    def download_html(self,word):
        '''
        download the html text
        :param word: word
        :return: 
        '''

        # url = '{}/{}/'.format(self.base_url, word)
        try:
            res = requests.get(self.get_url(word), headers=self.headers)
            self.count+=1
            if res.status_code == 200:
                return res.text
            else:
                print ('Fetch url failed ,error code :{}'.format(r.status_code))

        except ConnectTimeout as e:
            print('Get url:{} timeout'.format(url))

        except ConnectionError as e:
            print('Connect url:{} error'.format(url))

        except Exception as e:
            print(e)

    def crawl_each(self, word):
        '''
        crawl the word from youdao.com
        :param word: word
        :return: 
        '''
        output = OrderedDict()
        info = dict()
        url = '{}/{}/'.format(self.base_url,word)

        print('{}th. Fetch:{}...'.format(self.count, url))

        html_text=self.download_html(word)
        if not html_text:
            return

        info=self.decode_html(html_text)


        output['Word'] = word
        return dict(output, **info)


    def decode_html(self, html_text):
        doc=pq(html_text)
        proc_text = ''
        for pro in doc.items('.baav .pronounce'):
            proc_text += pro.text()

        desc_text = ''
        for li in doc.items('#phrsListTab .trans-container ul li'):
            desc_text += li.text()

        word_groups = set()
        for word_group in doc.items('#wordGroup .wordGroup'):
            word_groups.add(word_group.text())

        return {'Proc': proc_text, 'Desc': desc_text}


@count_running_time
def main():
    crawl=Spider()
    words = ['china', 'english', 'temperaments']*10
    res=[crawl.crawl_each(w) for w in words]
    pprint(res)

if __name__=='__main__':
    main()

