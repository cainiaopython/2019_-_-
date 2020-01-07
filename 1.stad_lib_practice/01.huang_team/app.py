from module.crawl import CrawlMovie
from handle_files.save_json import HandleJson
from handle_files.save_csv import HandleCSV
from pprint import pprint


def write_data(data,type='json'):
    if type=='json':
        handleJson=HandleJson()
        handleJson.write_json(data)
    elif type=='csv':
        handleCsv=HandleCSV()
        handleCsv.write_csv(data)


if __name__=='__main__':

    crawlMovie=CrawlMovie()
    data=crawlMovie.crawl()
    pprint(data)

    if not data:
        print ('Crawl failed!')
    else:
        write_data(data,type='csv')

