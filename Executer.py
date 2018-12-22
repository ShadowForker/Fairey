import whois
import pandas as pd

def MainExecuter(urlList):
    result=pd.DataFrame()
    for url in urlList:
        whoisInfo=getWhois(url)
        result.join(pd.DataFrame(whoisInfo,index=result.index))
    print (result)
    


def getWhois(url):
    return whois.whois("google.com")
    
