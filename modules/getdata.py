from bs4 import BeautifulSoup
from urllib.request import urlopen
from datetime import datetime
import re
date = datetime.today().strftime("%Y-%m-%d")

def getCommitData(member):
    response = urlopen('https://github.com/'+member)
    soup = BeautifulSoup(response, 'html.parser')
    for data in soup.find_all(class_='day'):
        if(data["data-date"] == date):
            return int(data["data-count"])

def getContribution(allMember):
    rankInfo = dict()
    for i in range(len(allMember)):
        response = urlopen('https://github.com/'+allMember[i])
        soup = BeautifulSoup(response, 'html.parser')
        for data in soup.find_all(class_='f4 text-normal mb-2'):
            score = 0
            if(re.findall("\d", data.get_text(" ", strip=True))):
                score = re.findall("\d+", data.get_text(" ", strip=True))
                rankInfo[allMember[i]] = str(score[0])
   # Rankdata = getRank(rankInfo)
    return rankInfo

def getContribution_one(member):
    response = urlopen('https://github.com/'+member)
    soup = BeautifulSoup(response, 'html.parser')
    for data in soup.find_all(class_='f4 text-normal mb-2'):
        score = 0
        if(re.findall("\d", data.get_text(" ", strip=True))):
            score = re.findall("\d+", data.get_text(" ", strip=True))
            return str(score[0])


#tier System
def getRank(rankInfo):
    tier = ['bronze','sliver','gold','platinum','master']
    rtntier = dict()
    member_key = list(rankInfo.keys())
    for name in member_key:
        tier_cnt = 5
        if int(rankInfo[name]) < 100:
            cnt =1
            for i in range(int(rankInfo[name])):
                if cnt% 20 == 0:
                    tier_cnt = tier_cnt -1
                cnt = cnt +1
            rtntier[name]=tier[0] + str(tier_cnt)
        elif 100<=int(rankInfo[name]) and int(rankInfo[name])<=500:
            cnt =1
            for i in range(100,int(rankInfo[name])+1):
                if cnt% 100 == 0:
                    tier_cnt = tier_cnt -1
                cnt = cnt +1
            rtntier[name]=tier[1] + str(tier_cnt)
        elif 500<int(rankInfo[name]) and int(rankInfo[name])<=1000:
            cnt =1
            for i in range(501,int(rankInfo[name])+1):
                if cnt% 100 == 0:
                    tier_cnt = tier_cnt -1
                    print(tier_cnt)
                cnt = cnt +1

            rtntier[name]=tier[2] + str(tier_cnt)
            
        elif 1000<int(rankInfo[name]) and int(rankInfo[name])<=5000:
            cnt =1
            for i in range(1001,int(rankInfo[name])+1):
                if cnt% 1000 == 0:
                    tier_cnt = tier_cnt -1
                cnt = cnt +1
            rtntier[name]=tier[3] + str(tier_cnt)
        elif 5000< int(rankInfo[name]):
            rtntier[name]=tier[4] + str(tier_cnt)
    return rtntier
def getRank_one(score):
    tier = ['bronze','sliver','gold','platinum','master']
    tier_cnt = 5
    rtntier = str()
    if int(score) < 100:
        cnt =1
        for i in range(int(score)):
            if cnt% 20 == 0:
                tier_cnt = tier_cnt -1
            cnt = cnt +1
        rtntier=tier[0] + str(tier_cnt)
    elif 100<=int(score) and int(score)<=500:
        cnt =1
        for i in range(100,int(score)+1):
            if cnt% 100 == 0:
                tier_cnt = tier_cnt -1
            cnt = cnt +1
        rtntier=tier[1] + str(tier_cnt)
    elif 500<int(score) and int(score)<=1000:
        cnt =1
        for i in range(501,int(score)+1):
            if cnt% 100 == 0:
                tier_cnt = tier_cnt -1
                print(tier_cnt)
            cnt = cnt +1

        rtntier=tier[2] + str(tier_cnt)
        
    elif 1000<int(score) and int(score)<=5000:
        cnt =1
        for i in range(1001,int(score)+1):
            if cnt% 1000 == 0:
                tier_cnt = tier_cnt -1
            cnt = cnt +1
        rtntier=tier[3] + str(tier_cnt)
    elif 5000< int(score):
        rtntier=tier[4] + str(tier_cnt)
    return rtntier