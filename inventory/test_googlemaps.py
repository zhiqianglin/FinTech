import googlemaps
import requests
import json
from collections import defaultdict

def returnInfo(query_results):
    itemDict = defaultdict(dict)

    for item in query_results['results']:
        itemDict[item['name']]['type'] = item['types']
        try:
            itemDict[item['name']]['price_level'] = item['price_level']
        except:
            itemDict[item['name']]['price_level'] = 'unknown'
        try:
            itemDict[item['name']]['rating'] = item['rating']
        except:
            itemDict[item['name']]['rating'] = 'unknown'
        #print(item['name'], itemDict[item['name']]['type'])

    return itemDict

def getLocation():
    send_url = 'http://freegeoip.net/json'
    r = requests.get(send_url)
    j = json.loads(r.text)
    lat = j['latitude']
    lon = j['longitude']
    print(lat, lon)
    return(lat, lon)
    
        
def getMerchants(oType, radius):
    (lat, lon) = getLocation()
    myKey = 'AIzaSyDhJNXil5LRFaNO5s-qA6JpMg84i7oXzcw'
    gmaps = googlemaps.Client(key=myKey)
    places_results = gmaps.places(query = 'restaurant', location=(lat, lon), radius=1000, open_now=True)
    return returnInfo(places_results)


if __name__=='__main__':
    merchantDict = getMerchants("Restaurants", 1000)
    for item in merchantDict:
        print(item, merchantDict[item])

