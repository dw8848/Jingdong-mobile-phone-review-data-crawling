import requests

class Jdcomment_spider(object):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
    }
    def __init__(self, file_name='1'):
        self.fp = open(f'./{file_name}.txt', 'w', encoding='utf-8')
        print(f'正在打开文件{file_name}.txt文件!')
    def parse_one_page(self, url):
        response = requests.get(url, headers=self.headers)
        js_data = response.json()
        comments_list = js_data['comments']
        for comment in comments_list:
            goods_id = comment.get('id')
            nickname = comment.get('nickname')
            score = comment.get('score')
            productSize = comment.get('productSize')
            productColor = comment.get('productColor')
            creationTime = comment.get('creationTime')
            content = comment.get('content')
            content = ','.join(content.split('\n'))
            print(content)
            self.fp.write(f'{goods_id},{nickname},{score},{productSize},{productColor},{creationTime},{content}\n')
    def parse_max_page(self):
        for page_num in range(99):
            new_url = f'https://club.jd.com/comment/productPageComments.action?productId=100011386554&score=0&sortType=5&page={page_num}&pageSize=10&isShadowSku=0&rid=0&fold=1'
            print(f'正在获取第{page_num}页')
            self.parse_one_page(url=new_url)
    def close_files(self):
        self.fp.close()
        print('爬虫结束，关闭文件！')
if __name__ == '__main__':
    jd_spider = Jdcomment_spider()
    jd_spider.parse_max_page()
    jd_spider.close_files()
