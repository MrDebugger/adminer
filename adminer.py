import requests
from urllib.parse import urlparse
import time
file='url.txt'
urls=[url for url in open(file).read().splitlines() if url]

admins=[admin for admin in open("admin.txt").read().splitlines() if admin]
found = open('found.txt','a')
for url in urls:
    print("[=] Testing:",urlparse(url).netloc)
    for admin in admins:
        if not urlparse(url).scheme:
            url = 'http://'+url
        elif not urlparse(url).netloc:
            print("[-] Invalid URL:",url)
            break
        if url[-1] == '/':
            link = url + admin
        else:
            link = url + '/' + admin
        try:
        	resp=requests.get(link, headers={"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox"})
        except:
        	print("[-] Error loading site:",link)
        	continue
        if resp:
            print('[+] Admin Found:', link)
            found.write(link+'\n')
        elif resp.status_code==404:
            print ('[-] Admin not found:', link)
        else:
        	print("[-] Unknown Code:",resp.status_code,'for url:',link)
found.close()
print("[+] Check found.txt for admin panels")
print("[+] Adminer Completed")