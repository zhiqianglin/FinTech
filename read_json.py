import json

merchantDict = json.load(open("merchants.json"))
for item in merchantDict:
    print(item, merchantDict[item])
