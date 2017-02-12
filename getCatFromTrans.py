import test_tsys
import test_yelp

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
    

if __name__=="__main__":
    headers = {"Authorization":"Bearer 51132146540652",
               "Content-Type": "application/json",
               "Accept":"application/json"}
    accountID = '00000010001'
    places = returnCat(accountID, headers)
    print(places)
    
