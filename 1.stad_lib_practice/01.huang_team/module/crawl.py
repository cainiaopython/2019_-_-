from pyquery import PyQuery as pq
from collections import OrderedDict,defaultdict
from pprint import pprint
import requests


class CrawlMovie:
    def __init__(self):
        self._header={
                'Cookie': '__mta=244044474.1563534488980.1576931667966.1576931671706.29; _lxsdk_cuid=16c09eaf2c6c8-04fab8080fbf41-37607c04-fa000-16c09eaf2c632; uuid_n_v=v1; uuid=9F808010238611EAB6C37B103D7A83022271946CE0904ED3AC0BAE97361C04D0; _csrf=b1054e9036a1ccc9c92cdf232ea32c832423aa388d2f9f8457c4da21beb49db9; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1576887174; _lxsdk=9F808010238611EAB6C37B103D7A83022271946CE0904ED3AC0BAE97361C04D0; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; __mta=244044474.1563534488980.1576930070258.1576931650188.27; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1576931671; _lxsdk_s=16f28c2c987-dfa-213-1b1%7C%7C1',
                'Host': 'maoyan.com',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36'
                }

        self._url='https://maoyan.com/board/4'

    def html_load(self,url):
        """
        
        :param url: movie url
        :return: movie html content
        """

        try:
            res=requests.get(url,headers=self._header)
            if res.status_code==200:
                return res.text
            else:
                return None

        except Exception as e :
            print (e)
            return None

    def parse_html(self,html_content):
        """
        
        :param html_content: movie html content
        :return: movie info as dict
        """

        doc=pq(html_content)
        items=doc('.board-item-main').items()
        output=[]
        for item in items:
            # print (item)
            movie=defaultdict(lambda :'')
            try:
                movie['movie_name']=item('.name').text()
                movie['movie_release_time']=item('.star').text()
                movie['movie_star']=item('.releasetime').text()
                output.append(movie)
            except Exception as e:
                print ('parse html content failed ,error:{}'.format(e))


        return output

    def crawl(self,pages=100):
        """
        crawl the movie url 
        :return: iter movies
        """

        urls=['{}?offset={}'.format(self._url,page) for page in range(0,pages,10)]

        out=[]
        for url in urls:
            html=self.html_load(url)
            movies=self.parse_html(html)
            out.extend(movies)

        return out


if __name__=='__main__':
    movie=CrawlMovie()
    movies=movie.crawl()
    pprint(movies)



