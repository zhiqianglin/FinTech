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

def getBusinessCat(client, businessName):
    response = client.get_business(businessName)
    
    print(response)
    

def returnInfo(query_results):
    itemDict = defaultdict(dict)

    for item in query_results.businesses:
        itemDict[item.name]['rating'] = item.rating
        itemDict[item.name]['categories'] = item.categories
        itemDict[item.name]['image_url'] = item.image_url
    return itemDict

if __name__=="__main__":
    client = getClient()
    cll = getLocation()
    userTerm = 'Chinese'
    userRadius = 1000
    params = {'term': userTerm, 'radius_filter': userRadius}
    response = client.search(cll, **params)
    itemDict = returnInfo(response)
    
    for bus in itemDict:
        print(bus, itemDict[bus])

    businessName = 'FIVE GUYS'
    businessName = 'yelp-san-francisco'
    getBusinessCat(client, businessName)
