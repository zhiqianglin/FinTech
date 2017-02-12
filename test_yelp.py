from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
from collections import defaultdict
import io
import json
import requests

def getClient():
    with io.open('config_secret.json') as cred:
        creds = json.load(cred)
        auth = Oauth1Authenticator(**creds)
        client = Client(auth)
    return client

def getLocation():
    send_url = 'http://freegeoip.net/json'
    r = requests.get(send_url)
    j = json.loads(r.text)
    lat = j['latitude']
    lon = j['longitude']
    return str(lat)+','+str(lon)

def getCategory_new(business):
    client = getClient()
    category = []
    for item in business:
        location = item[1]
        params = {'term': item[0], 'limit': 1}
        response = client.search(location, **params)
        for item in response.businesses:
            for cat in item.categories:
                category.append(cat.name)
    return category



def getCategory(business):
    client = getClient()
    category = set()
    for name in business:
        location = business[name]
        params = {'term': name, 'limit': 1}
        response = client.search(location, **params)
        for item in response.businesses:
            for cat in item.categories:
                category.add(cat.name)
    return list(category)
    

def returnInfo(userTerm, userRadius=1000):
    client = getClient()
    cll = getLocation()
    params = {'term': userTerm, 'radius_filter': userRadius}
    response = client.search(cll, **params)
    itemDict = defaultdict(dict)

    for item in response.businesses:
        itemDict[item.name]['rating'] = item.rating
        itemDict[item.name]['categories'] = item.categories
        itemDict[item.name]['image_url'] = item.image_url
    return itemDict

if __name__=="__main__":
    userTerm = 'Chinese'
    itemDict = returnInfo(userTerm)
    
    for bus in itemDict:
        print(bus, itemDict[bus])
    business = {"five guys":'30269'}
    getCategory(business)
