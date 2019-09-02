import requests
from bs4 import BeautifulSoup
from lxml import html
from requests.compat import quote_plus


def ins(name):
    features=[]
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}
    instructables='https://www.instructables.com/howto/{}'
    instractables_id="https://www.instructables.com"
    final_url = instructables.format(quote_plus(name))
    response = requests.get(final_url,headers=headers)
    soup = BeautifulSoup(response.content, features='html.parser')
    try:
    	found=soup.findAll('div',attrs={'class':'desktop-search-feed-ible'})
    except:
    	return features
    for i in range(len(found)):
        aa=found[i].find('a')
        ID=aa['href']
        final_id=instractables_id+ID
        if aa:
        	img=aa.find('img')
        	if img:
        		img_name=img['alt'].lower()
        		img_url=img['data-src']
        	else:
        		img_name=None
        		img_url=None
        else:
        	final_id=None
        
        features.append((img_name,img_url,final_id))
    return features