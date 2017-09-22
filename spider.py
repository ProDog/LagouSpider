# coding=utf-8
#pip install bs4
#pip install requests

import urllib
import requests
from bs4 import BeautifulSoup
def main():
    headers={
        'User-Agent': 'Mozilla/5.0(WindowsNT10.0;Win64;x64) AppleWebKit/537.36(KHTML, like Gecko)Chrome/61.0.3163.79 Safari/537.36',
        'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
        'host':'www.lagou.com',
        'Cookie': 'user_trace_token = 20170825172024 - bacd1a4b - 2255 - 4654 - b457 - 515c631734ea;LGUID = 20170825172033 - a5538dab - 8976 - 11e7 - 8ed1 - 5254005c3644;X_HTTP_TOKEN = b1de8b4a133489968a90c6eace00b223;showExpriedIndex = 1;showExpriedCompanyHome = 1;showExpriedMyPublish = 1;hasDeliver = 43;TG - TRACK - CODE = search_code;index_location_city = % E5 % 85 % A8 % E5 % 9B % BD;login = false;unick = "";_putrc = "";JSESSIONID = ABAAABAAADEAAFI69018E2C5FCF41EFD7EB90825DF1DA5B;_gid = GA1.2.306486117.1506009766; _gat = 1;_ga = GA1.2.728564437.1503652829;Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6 = 1503652829, 1503927880, 1504702487, 1506009766;Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6 = 1506012702;LGSID = 20170922000246 - 4f1481fa - 9ee6 - 11e7 - 9219 - 5254005c3644;LGRID = 20170922005142 - 255c58f4 - 9eed - 11e7 - a097 - 525400f775ce;SEARCH_ID = 88c191cf0a45466aa247475560583f64',
        'X - Anit - Forge - Code': '0',
        'X - Anit - Forge - Token': None,
        'X - Requested - With': 'XMLHttpRequest'
    }
    result=requests.get('https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false',headers=headers)
    print(result.content.decode('utf-8'))
if __name__ == '__main__':
    main()



