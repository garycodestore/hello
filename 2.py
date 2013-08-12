import sys, urllib2, re

#url = "http://www.weather.com.cn/html/weather/101210501.shtml"
url = "http://gd.weather.com.cn/"
fd = urllib2.urlopen(url)
html = fd.read()
fd.close()

reg = '<a title=.*?>(.*?)</a>.*?<span>(.*?)</span>.*?<b>(.*?)</b>';
weather = re.compile(reg).findall(html)
print weather


