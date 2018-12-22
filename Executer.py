import whois
import pandas as pd

def MainExecuter(urlList):
    result=pd.DataFrame.from_dict(getWhois(urlList[0]))
    for url in urlList[1:]:
        whoisInfo=getWhois(url)
        result.join(pd.DataFrame(whoisInfo,index=result.index))
    print (result)
    


def getWhois(url):
    return whois.whois("google.com")
    
