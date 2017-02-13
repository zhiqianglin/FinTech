from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import redirect
from inventory.models import Restaurant
import inventory.test_googlemaps as gmap
from inventory.libs import *
from inventory.libs import getCatFromTrans as GT
import pandas as pd
import operator
import yaml


import json
 
# def cody(category):
#     df = pd.read_csv("inventory/libs/transactionHistory.csv", dtype={'accountId':object}, header=0)
#     accountID = '19920223'
#     freq = GT.find_category(df, accountID)
#     sortedFreq = sorted(freq.items(), key=operator.itemgetter(0), reverse=True)
#     categories = [item[0] for item in sortedFreq][:3]
#     print("Recommended categories:", categories)
    
#     '''
#     # Uncomment this part to use API to retrieve 
#     headers = {"Authorization":"Bearer 51132146540652",
#                "Content-Type": "application/json",
#                "Accept":"application/json"}
#     accountID = '00000010001'
    
#     # These returned categories are then used to make csv data file
#     categories = returnCat(accountID, headers)
#     print(categories)
#     '''

#     rewardFile = 'inventory/libs/rewards.csv'
#     categoryMap = GT.rewardMap(rewardFile)
    
#     merchant, merchantDict = GT.getNearbys(categories)
#     print("Corresponding nearby merchants:", merchant)
#     merchantNoffer = GT.getOffer(merchant, categoryMap, accountID)
#     for merc in merchantNoffer:
#         print("Name:", merc[0], "rating:", merchantDict[merc[0]]['rating'], "imageurl:", merchantDict[merc[0]]['image_url'], "Offer:", categoryMap[merc]['rewardsEarned'])
#     return merchantNoffer, merchantDict, categoryMap

def cody(category):
    merchantDict = yaml.load(open('inventory/libs/merchantDict.yml'))
    merchantNoffer = yaml.load(open('inventory/libs/merchantNoffer.yml'))
    categoryMap = yaml.load(open('inventory/libs/categoryMap.yml'))
    # for merc in merchantNoffer:
    #     print("Name:", merc[0], "rating:", merchantDict[merc[0]]['rating'], "imageurl:", merchantDict[merc[0]]['image_url'], "Offer:", categoryMap[merc]['rewardsEarned'])
    return merchantNoffer, merchantDict, categoryMap


def index(request):
    return render(request, 'inventory/index.html')


def cody2(category):
    merchantDict = yaml.load(open('inventory/libs/merchantDict2.yml'))
    merchantNoffer = yaml.load(open('inventory/libs/merchantNoffer2.yml'))
    categoryMap = yaml.load(open('inventory/libs/categoryMap2.yml'))
    # for merc in merchantNoffer:
    #     print("Name:", merc[0], "rating:", merchantDict[merc[0]]['rating'], "imageurl:", merchantDict[merc[0]]['image_url'], "Offer:", categoryMap[merc]['rewardsEarned'])
    return merchantNoffer, merchantDict, categoryMap

# def result(request):

#     category = "Restaurants"
#     # merchantDict = gmap.getMerchants(category, 1000)
#     # merchantDict = read_json.getDict()
#     merchantDict = json.load(open("./inventory/merchants.json"))

#     #{resName: pricelevel, type, rating}
#     allRes = []
#     for key in merchantDict:
#         if not Restaurant.objects.filter(name=key).exists():
#             if merchantDict[key]['price_level'] == 'unknown':
#                 merchantDict[key]['price_level'] = -1
#             if merchantDict[key]['rating'] == 'unknown':
#                 merchantDict[key]['price_level'] = -1
#             res = Restaurant.create(key, merchantDict[key]['type'],
#             merchantDict[key]['price_level'] , "Fastfood", "Restaurant", merchantDict[key]['rating'])
#             res.save()
#         # allRes.append(res)
#         else:
#             allRes.append(Restaurant.objects.get(name=key[0]))

#     # allRes = Restaurant.objects.all()
#     print(len(allRes))
#     return render(request, 'inventory/result.html', {
#         'restaurants': allRes,
#         })


def result(request):


    category = "Restaurants"
    # merchantDict = gmap.getMerchants(category, 1000)
    # merchantDict = read_json.getDict()
    merchantNoffer, merchantDict, categoryMap = cody(category)

    #{resName: pricelevel, type, rating}
    allRes = []

    url = ['https://s3-media3.fl.yelpcdn.com/bphoto/LR_uqc0lIgxuBqSDHqlcQA/ls.jpg', 'https://s3-media1.fl.yelpcdn.com/bphoto/a7T6AlphbNszK97FjA7ALQ/ls.jpg',
    'https://s3-media3.fl.yelpcdn.com/bphoto/fryLmvAyxVPHfQfAIZfThg/ms.jpg', 'https://s3-media1.fl.yelpcdn.com/bphoto/pb8tg3wfAnHmosX8mjFpAg/ms.jpg', 
    'https://s3-media3.fl.yelpcdn.com/bphoto/CPXnOesDOA-d_1V9qnC67g/ms.jpg']
    idx = 0
    for key in merchantNoffer:
        if not Restaurant.objects.filter(name=key[0]).exists():
            if merchantDict[key[0]]['rating'] == 'unknown':
                merchantDict[key[0]]['rating'] = -1

            res = Restaurant.create(key[0], categoryMap[key]['rewardsEarned'], 
                merchantDict[key[0]]['rating'], url[idx], url[idx])
            print("aqaaaaaa")
            print(merchantDict[key[0]]['image_url'])
        # res = cls(name = name, offer = offer,   
        #   rating = rating, image = image)
            res.save()
            allRes.append(res)

        # allRes.append(res)
        else:
            allRes.append(Restaurant.objects.get(name=key[0]))
        idx += 1
    # for ()
    return render(request, 'inventory/result.html', {
        'restaurants': allRes,
        })

def result2(request):


    category = "Restaurants"
    # merchantDict = gmap.getMerchants(category, 1000)
    # merchantDict = read_json.getDict()
    merchantNoffer, merchantDict, categoryMap = cody2(category)

    #{resName: pricelevel, type, rating}
    allRes = []

    url = ['https://s3-media3.fl.yelpcdn.com/bphoto/LR_uqc0lIgxuBqSDHqlcQA/ls.jpg', 'https://s3-media1.fl.yelpcdn.com/bphoto/a7T6AlphbNszK97FjA7ALQ/ls.jpg',
    'https://s3-media3.fl.yelpcdn.com/bphoto/fryLmvAyxVPHfQfAIZfThg/ms.jpg', 'https://s3-media1.fl.yelpcdn.com/bphoto/pb8tg3wfAnHmosX8mjFpAg/ms.jpg', 
    'https://s3-media3.fl.yelpcdn.com/bphoto/CPXnOesDOA-d_1V9qnC67g/ms.jpg']
    idx = 0
    for key in merchantNoffer:
        if not Restaurant.objects.filter(name=key[0]).exists():
            if merchantDict[key[0]]['rating'] == 'unknown':
                merchantDict[key[0]]['rating'] = -1

            # res = Restaurant.create(key[0], categoryMap[key]['rewardsEarned'], 
            #     merchantDict[key[0]]['rating'], merchantDict[key[0]]['image_url'], merchantDict[key]['image_url'])
            res = Restaurant.create(key[0], categoryMap[key]['rewardsEarned'], 
                merchantDict[key[0]]['rating'], 'https://s3-media2.fl.yelpcdn.com/bphoto/TSO8RHXJIwFlt6mB8moZsw/ms.jpg', url[idx])
            print(merchantDict[key[0]]['image_url'])
        # res = cls(name = name, offer = offer,   
        #   rating = rating, image = image)
            res.save()
            allRes.append(res)

        # allRes.append(res)
        else:
            allRes.append(Restaurant.objects.get(name=key[0]))
        idx += 1
    # for ()
    return render(request, 'inventory/result2.html', {
        'restaurants': allRes,
        })


def restaurant_detail(request, id):
    # return HttpResponse('<p>I am in the restaurant_view with id {0}</p>'.format(id))
    try:
        res = Restaurant.objects.get(id=id)
    except:
        raise Http404('This restaurant doet not exist')
    return render(request, 'inventory/restaurant_detail.html', {
        'restaurant': res,
        })


# def dothing():


#   category = "Restaurants"
#   # merchantDict = gmap.getMerchants(category, 1000)
#   # merchantDict = read_json.getDict()
#   merchantDict = json.load(open("./inventory/merchants.json"))

#   #{resName: pricelevel, type, rating}
#   allRes = []
#   for key in merchantDict:
#       if not Restaurant.objects.filter(name=key).exists():
#           if merchantDict[key]['price_level'] == 'unknown':
#               merchantDict[key]['price_level'] = -1
#           if merchantDict[key]['rating'] == 'unknown':
#               merchantDict[key]['price_level'] = -1
#           res = Restaurant.create(key, merchantDict[key]['type'],
#           merchantDict[key]['price_level'] , "Fastfood", "Restaurant", merchantDict[key]['rating'])
#           res.save()
#       # allRes.append(res)
#       else:
#           allRes.append(Restaurant.objects.get(name=key))
#   return allRes


def dothing():


    category = "Restaurants"
    # merchantDict = gmap.getMerchants(category, 1000)
    # merchantDict = read_json.getDict()
    merchantNoffer, merchantDict, categoryMap = cody(category)

    #{resName: pricelevel, type, rating}
    allRes = []

    for key in merchantNoffer:
        if not Restaurant.objects.filter(name=key[0]).exists():
            if merchantDict[key[0]]['rating'] == 'unknown':
                merchantDict[key[0]]['rating'] = -1

            res = Restaurant.create(key[0], categoryMap[key]['rewardsEarned'], 
                merchantDict[key[0]]['rating'], merchantDict[key[0]]['image_url'])
            print(merchantDict[key[0]]['image_url'])
        # res = cls(name = name, offer = offer,   
        #   rating = rating, image = image)
            res.save()
        # allRes.append(res)
        else:
            allRes.append(Restaurant.objects.get(name=key[0]))

    return allRes




    # for key in merchantDict:
    #   if not Restaurant.objects.filter(name=key).exists():
    #       if merchantDict[key]['price_level'] == 'unknown':
    #           merchantDict[key]['price_level'] = -1
    #       if merchantDict[key]['rating'] == 'unknown':
    #           merchantDict[key]['price_level'] = -1
    #       res = Restaurant.create(key, merchantDict[key]['type'],
            

    #       merchantDict[key]['price_level'] , "Fastfood", "Restaurant", merchantDict[key]['rating'])
    #       res.save()
    #   # allRes.append(res)
    #   else:
    #       allRes.append(Restaurant.objects.get(name=key))
    # return allRes



# def search(request):
#   if (request.method == "POST"):
#           # return render(request, 'inventory/search.html', {'form': form})
#       form = PostForm(request.POST)
#       res = form.save()
#       res.save()
#       # return redirect('result.html')
#       allRes = dothing()
#       return render(request, 'inventory/result.html', {'restaurants': allRes})
#   else:
#       form = PostForm()
#       return render(request, 'inventory/search.html', {'form': form})

