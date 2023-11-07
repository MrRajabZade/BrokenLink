import sys
import tldextract
from requests import *
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from rich.progress import Progress

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
            return "[#]"
        else:
            return link
    else:
        return "[#]"

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

try:
    url = str(sys.argv[1])
except:
    url = input("Enter url: ")
with Progress(transient=True) as progress:
    check1 = progress.add_task("Check", total=3)

    while not progress.finished:
        domain=get_domain(url)
        progress.update(check1, advance=1)
        urls = find_urls(url)
        progress.update(check1, advance=1)
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
                    if str(response) == "[#]":
                        continue
                    else:
                        if str(response) == "[Error]":
                            s = str(link)
                            link = "https://" + str(link)
                            response = check(link, domain)
                            if str(response) == "[Error]":
                                urls_error.append(str(s))
                            else:
                                domain_link = get_domain(link)
                                if str(domain) in str(domain_link):
                                    continue
                                else:
                                    urls_broken.append(str(link))
                        else:
                            domain_link = get_domain(link)
                            if str(domain) in str(domain_link):
                                continue
                            else:
                                urls_broken.append(str(link))

        progress.update(check1, advance=1)
data = "{} Links; {} Broken links; {} Redirect link; {} Error".format(str(len(urls)), str(len(urls_broken)), str(len(urls_redirected)), str(len(urls_error)))
print("Total URLs: {};".format(data))
try:

    file1 = open("Result.txt", "x")
except FileExistsError:
    file1 = open("Result.txt", "w")
if urls_broken:
    for i in urls_broken:
        file1.write("[Broken] "+str(i)+"\n")
if urls_redirected:
    for i in urls_redirected:
        file1.write("[Redirect] "+str(i)+"\n")
if urls_error:
    for i in urls_error:
        file1.write("[Error] "+str(i)+"\n")
file1.close()