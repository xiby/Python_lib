import io
import sys
import urllib.request
import requests
from bs4 import BeautifulSoup

sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
url="http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-recent7-0-0-1-1"         #京东图书排行榜网页
data=requests.get(url)
data=BeautifulSoup(data.decode('gb2312','ignore'),'html5lib')
print(data.find_all('li'))