import inventory.libs.test_tsys
import operator
import inventory.libs.test_yelp as test_yelp
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
    merchantsAll = defaultdict(dict)
    for cat in categories:
        merchantsNearby = test_yelp.returnInfo(cat, userRadius)
        for merc in merchantsNearby:
            merchants.add(merc)
            merchantsAll.update({merc:merchantsNearby[merc]})
    return list(merchants), merchantsAll

def rewardMap(rewardFile):
    rewardDict = defaultdict(dict)
    df = pd.read_csv(rewardFile, dtype={'accountId':object})
    for index, row in df.iterrows():
        rewardDict[(row['pod'],row['accountId'])]['Event'] = row['Event']
        rewardDict[(row['pod'],row['accountId'])]['start_time'] = row['start_time']
        rewardDict[(row['pod'],row['accountId'])]['end_time'] = row['end_time']
        # Call tsys api here to translate rewardsEarned to money value
        rewardDict[(row['pod'],row['accountId'])]['rewardsEarned'] = row['rewardsEarned']
    return rewardDict

def getSim(str1, str2):
    return SequenceMatcher(None, str1, str2).ratio()
    
def getOffer(merchant, categoryMap, accountID):
    merchantsNoffer = []
    for merc in merchant:
        for key in categoryMap:
            if getSim(key[0], merc) >= 0.8 and str(key[1]) == accountID:
                 merchantsNoffer.append(key)
    return merchantsNoffer


def find_category(df, userid):
    dfi=df[df["accountId"]==userid]
    places=[]
    for index, row in dfi.iterrows():
        places.append((row["merchant"],row["postalCode"]))
        
    catList = test_yelp.getCategory_new(places)
    freq = {x:catList.count(x) for x in catList}
    return freq
                                    

if __name__=="__main__":
    df = pd.read_csv("transactionhistory.csv", dtype={'accountId':object}, header=0)
    accountID = '19920223'
    freq = find_category(df, accountID)
    sortedFreq = sorted(freq.items(), key=operator.itemgetter(0), reverse=True)
    categories = [item[0] for item in sortedFreq][:3]
    print("Recommended categories:", categories)
    
    '''
    # Uncomment this part to use API to retrieve 
    headers = {"Authorization":"Bearer 51132146540652",
               "Content-Type": "application/json",
               "Accept":"application/json"}
    accountID = '00000010001'
    
    # These returned categories are then used to make csv data file
    categories = returnCat(accountID, headers)
    print(categories)
    '''

    rewardFile = 'rewards.csv'
    categoryMap = rewardMap(rewardFile)
    
    merchant, merchantDict = getNearbys(categories)
    print("Corresponding nearby merchants:", merchant)
    merchantNoffer = getOffer(merchant, categoryMap, accountID)
    for merc in merchantNoffer:
        print("Name:", merc[0], "rating:", merchantDict[merc[0]]['rating'], "imageurl:", merchantDict[merc[0]]['image_url'], "Offer:", categoryMap[merc]['rewardsEarned'])
