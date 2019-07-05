import requests
import bs4
from bs4 import BeautifulSoup
import re

def getHTMLText(url,kv):
    try:
##        kv={"wd":keywords}
        r = requests.get(url,params=kv,timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def seachResultList(rlist, html):
    soup = BeautifulSoup(html, "html.parser")
    divs=soup.find_all('div',attrs={'class':'c-tools'},limit=2)
    for i in divs:
        try:
            datatools=i.attrs['data-tools']
            name=eval(datatools)['title']
            url=eval(datatools)['url']
            rlist.append([name,url])
        except:
            continue
        
def printResultList(rlist):
    trlt="{:4}\t{:10}\t{:20}"
    print(trlt.format("No.","name","url"))
    count=0
    for k in rlist:
        count=count+1
        print(trlt.format(count,k[0],k[1]))

def main():
    url="http://www.baidu.com/s"
    infolist=[]
    fpath=r"/Users/wuxi/Desktop/brand_keyword.txt"
    file = open(fpath)
    lines = file.readlines()
    for line in lines:
        line=line.strip('\n')
        kv={"wd":line}

        html=getHTMLText(url,kv)
        seachResultList(infolist, html)
    printResultList(infolist)
main()
    
    
