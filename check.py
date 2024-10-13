import requests
import threading

start = input("Press Enter To Start")

goodproxy = 0
valid_proxy = f"Valid proxy: {goodproxy}"

with open ("proxy.txt","r") as file:
	proxies = [line.strip() for line in file.readlines()]


def checking(proxy, URL):
    try:
        s = requests.session()
        s.proxies = {'http':proxy,'https':proxy} 
        s.headers = {'user-agents':  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                                        '(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
        aa = s.get(URL,timeout=5)
        if aa.status_code == 200:
            global goodproxy
            goodproxy += 1
            print(f"Proxy {proxy.strip()} is valid")
        else:
        	print(f"Proxy {proxy.strip()} failed with status code: {aa.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Proxy {proxy.strip} failed:{e}")
        
for proxy in proxies:
        checking(proxy,'http://goggle.com')
print(f"Total good proxies:{goodproxy}")
        
        
        
        
     
                                      
	