import requests
from bs4 import BeautifulSoup
from random import choice

def get_proxies():
	url = "https://github.com/clarketm/proxy-list/blob/master/proxy-list.txt"
	r = requests.get(url)
	soup = BeautifulSoup(r.content, "html.parser").find_all("td", {"class":"blob-code blob-code-inner js-file-line"})
	proxies = [proxy.text for proxy in soup]
	return proxies



def get_working_proxies(proxies=get_proxies()):
	for proxy in proxies:
		try:
			print(proxy)
			r = requests.get("https://www.google.com", proxies=proxy, timeout=2)
			if r.status_code == 200:
				working_proxies.append(proxy)
		except:
			pass
		else:
			pass
		finally:
			pass
		
	return working_proxies

print(get_working_proxies())