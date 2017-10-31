import bs4 as bs
import urllib.request
url=urllib.request.urlopen('http://ekonomi.haber7.com/ekonomi/haber/451145-1998den-2010a-kisibasi-milli-gelir').read()
sayfa=bs.BeautifulSoup(url,'lxml')
sayfa2=sayfa.findAll('pre')
for i in sayfa2:
        print(i.text)
    
    
    
