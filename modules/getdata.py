from bs4 import BeautifulSoup
from urllib.request import urlopen
from datetime import datetime

def getCommitData(member):
    date = datetime.today().strftime("%Y-%m-%d")
    response = urlopen('https://github.com/'+member)
    soup = BeautifulSoup(response, 'html.parser')
    for data in soup.find_all(class_='day'):
        if(data["data-date"] == date):
            return int(data["data-count"])