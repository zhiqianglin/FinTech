import yaml

def cody(category):
    merchantDict = yaml.load(open('inventory/libs/merchantDict2.yml'))
    merchantNoffer = yaml.load(open('inventory/libs/merchantNoffer2.yml'))
    categoryMap = yaml.load(open('inventory/libs/categoryMap2.yml'))
    # for merc in merchantNoffer:
    #     print("Name:", merc[0], "rating:", merchantDict[merc[0]]['rating'], "imageurl:", merchantDict[merc[0]]['image_url'], "Offer:", categoryMap[merc]['rewardsEarned'])
    return merchantNoffer, merchantDict, categoryMap



merchantNoffer, merchantDict, categoryMap = cody("Restaurants")



for key in merchantNoffer:
	print(key[0])
	print(merchantDict[key[0]]['image_url'])