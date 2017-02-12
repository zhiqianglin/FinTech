import test_tsys
import test_yelp
from difflib import SequenceMatcher
import pandas as pd
from collections import defaultdict

def returnCat(accountID, headers):
    # returns dictionary in {place name: zip code} format
    places = {}
    resp = test_tsys.getTransactions(accountID, headers)
    for item in resp.json()['transactions']:
        places[item['merchant']['name']] = item['merchant']['address']['postalCode']
    categories = set()
    print(places)
    catList = test_yelp.getCategory(places)
    for cat in catList:
        categories.add(cat)
    return list(categories)
    
def getNearbys(categories, userRadius=1000):
    merchants = set()
    for cat in categories:
        merchantsNearby = test_yelp.returnInfo(cat, userRadius)
        for merc in merchantsNearby:
            merchants.add((merc))
    return list(merchants)

def rewardMap(rewardFile):
    rewardDict = defaultdict(dict)
    df = pd.read_csv(rewardFile)
    for index, row in df.iterrows():
        rewardDict[row['pod']]['Event'] = row['Event']
        rewardDict[row['pod']]['start_time'] = row['start_time']
        rewardDict[row['pod']]['end_time'] = row['end_time']
        # Call tsys api here to translate rewardsEarned to money value
        rewardDict[row['pod']]['rewardsEarned'] = row['rewardsEarned']
    return rewardDict

def getSim(str1, str2):
    return SequenceMatcher(None, str1, str2).ratio()
    
def getOffer(merchant, categoryMap):
    merchantsNoffer = []
    for merc in merchant:
        for cat in categoryMap:
            if getSim(merc, cat) >= 0.8:
                print(merc, cat, getSim(merc, cat))
                merchantsNoffer.append(cat)
    return merchantsNoffer

if __name__=="__main__":
    headers = {"Authorization":"Bearer 51132146540652",
               "Content-Type": "application/json",
               "Accept":"application/json"}
    accountID = '00000010001'
    
    # These returned categories are then used to make csv data file
    categories = returnCat(accountID, headers)
    print(categories)

    rewardFile = 'rewards.csv'
    categoryMap = rewardMap(rewardFile)
    print(categoryMap)
    
    merchant = getNearbys(categories)
    merchantNoffer = getOffer(merchant, categoryMap)

    for merc in merchantNoffer:
        print(merc, categoryMap[merc]['rewardsEarned'])
    print(merchantNoffer)
    

