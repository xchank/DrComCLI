#!/usr/bin/env python3

import urllib.request
import urllib.parse
import sys


def login(username, password):
    data = {
        'DDDDD': username,  
        'upass': password,  
        '0MKKey': r'登　录',
        'v6ip': ''
    }

    url = 'http://192.168.168.168/0.htm'
    header = {
        'Host': '192.168.168.168',
        'Connection': 'keep-alive',
        'Content-Length': '53',
        'Cache-Control': 'max-age=0',
        'Origin': 'http://192.168.168.168',
        'Upgrade-Insecure-Requests': '1',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'DNT': '1',
        'Referer': 'http://192.168.168.168/0.htm',
        'Accept-Encoding': 'gzip, deflate'
    }

    data = urllib.parse.urlencode(data).encode('gb2312')
    request = urllib.request.Request(url, headers=header, data=data)
    page = urllib.request.urlopen(request).read()  
    page = page.decode('gb2312')
    if len(page) == 3942:
        print('Success.')
    else:
        print('Fail.')

    # 3942 -> ok
    # 5696 -> error

def logout():
    url = 'http://192.168.168.168/F.htm'
    request = urllib.request.Request(url)
    page = urllib.request.urlopen(request).read()
    page = page.decode('gb2312')
    print('Success.')



if __name__ == "__main__":
    option = sys.argv[1]
    if option == 'login':
        login(sys.argv[2], sys.argv[3])
    elif option == 'logout':
        logout()
