import sys
import tldextract
from requests import *
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import threading
from colorama import Fore

def get_domain(url):
    extracted = tldextract.extract(str(url))
    domain = "{}.{}".format(extracted.domain, extracted.suffix)
    return str(domain)

def get_redirected_site(url):
    try:
        response = get(url, allow_redirects=False)
        if response.status_code == 301 or response.status_code == 302:
            redirected_url = response.headers['Location']
            parsed_url = urlparse(redirected_url)
            return parsed_url.netloc
        else:
            return None
    except exceptions.RequestException:
        return None

def check(link, domain):
    try:
        response = get(url=link)
    except:
        return "[Error]"
    if str(response.status_code) == "404":
        domain_link = get_domain(link)
        if str(domain) in str(domain_link):
            return None
        else:
            return str(link)
    else:
        return None

def find_urls(url):
    try:
        response = get(url)
    except Exception as error:
        url = "https://"+str(url)
        try:
            response = get(url)
        except:
            print("Invalid URL")
            sys.exit()
    soup = BeautifulSoup(response.text, 'html.parser')
    urls = []
    for url in soup.find_all(href=True):
        url = url.get('href')
        if str(url) == "None":
            continue
        else:    
            urls.append(url)
    return urls

def progress():
    try:
        url = str(sys.argv[1])
    except:
        url = input("Enter URL: "+Fore.MAGENTA)
        
    domain=get_domain(url)
    urls = find_urls(url)
    urls_broken = []
    urls_error = []
    urls_redirected = []
    for link in urls:
        if str(link) == "":
            continue
        else:
            if str(link[0]) == "/":
                continue
            else: 
                redirected_site = get_redirected_site(link)
                if redirected_site:
                    link = str(redirected_site)
                    domain_link = get_domain(link)
                    if str(domain) in str(domain_link):
                        continue
                    else:
                        urls_redirected.append(str(redirected_site))
                response = check(link, domain)
                if str(response) == "[Error]":
                    s = str(link)
                    link = "https://" + str(link)
                    response = check(link, domain)
                    if str(response) == "[Error]":
                        if str(s[0]) == '#':
                            continue
                        else:
                            urls_error.append(str(s))
                            continue
                    else:
                        if response:
                            urls_broken.append(str(link))
                        else:
                            continue
                else:
                    if response:
                        urls_broken.append(str(link))
                    else:
                        continue

    data = Fore.GREEN+str(len(urls))+Fore.WHITE+" Links; "+Fore.RED+str(len(urls_broken))+Fore.WHITE+" Broken links; "+Fore.BLUE+str(len(urls_redirected))+Fore.WHITE+" Redirect link; "+Fore.YELLOW+str(len(urls_error))+Fore.WHITE+" Error"
    print(Fore.WHITE+"Total URLs: {};".format(data))
    if urls_broken:
        for i in urls_broken:
            print(Fore.RED+"[Broken] "+Fore.WHITE+str(i))
    if urls_redirected:
        for i in urls_redirected:
            print(Fore.BLUE+"[Redirect] "+Fore.WHITE+str(i))
    if urls_error:
        for i in urls_error:
            print(Fore.YELLOW+"[Error] "+Fore.WHITE+str(i))

x = threading.Thread(target=progress)
x.start()