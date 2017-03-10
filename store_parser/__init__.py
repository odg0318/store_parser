import urllib2
from bs4 import BeautifulSoup

def parse_googleplay(url):
    response = urllib2.urlopen(url)
    html = response.read().decode('utf-8')

    soup = BeautifulSoup(html, 'html.parser')

    name = soup.find_all('div', {'class' : 'document-title'})[0].get_text().strip()
    author = soup.find_all('a', {'class' : 'document-subtitle primary'})[0].get_text().strip()
    description = '\n'.join(soup.find_all('div', {'class' : 'show-more-content'})[0].strings).strip()
    icon_url = soup.find_all('img', {'class' : 'cover-image'})[0].get('src').strip()

    return {
        'name': name,
        'author': author,
        'description': description,
        'icon_url': icon_url
    }

def parse_appstore(url):
    response = urllib2.urlopen(url)
    html = response.read().decode('utf-8')

    soup = BeautifulSoup(html, 'html.parser')

    name = soup.find('div', {'id' : 'title'}).find('h1').get_text().strip()
    author = soup.find('div', {'id' : 'title'}).find('h2').get_text().strip()
    description = soup.find('div', {'class' : 'product-review'}).find('p').get_text().strip()
    icon_url = soup.find('div', {'class' : 'lockup product application'}).find('a').find('div').find('img')['src']

    return {
        'name': name,
        'author': author,
        'description': description,
        'icon_url': icon_url
    }
