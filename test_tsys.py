import requests

def getTransactions(accountID, headers):
    url = "https://beta.tsysapi.com/sandbox/transaction/"+accountID+"/current"
    resp = requests.get(url, headers=headers)
    print(resp.json())
    for item in resp.json()['transactions']:
        print('{} {}'.format(item['merchant']['name'], item['amount']['value']))
    return resp

def getRewardsValue(accountID, rewardsValue, headers):
    url = "https://beta.tsysapi.com/sandbox/rewards/"+accountID+'/convert/rewards/'+rewardsValue
    resp = requests.get(url, headers=headers)
    print(resp)
    return resp.json()['dollarValue']

def getRewardBalance(accountID, headers):
    url = "https://beta.tsysapi.com/sandbox/rewards/"+accountID+"/earn/event"
    resp = requests.get(url, headers=headers)
    print(resp)
    return resp.json()['balance']
    
if __name__=="__main__":
    headers = {"Authorization":"Bearer 51132146540652",
               "Content-Type": "application/json",
               "Accept":"application/json"}
    accountID = '00000010001'
    getTransactions(accountID, headers)
    totalRewards = getRewardBalance(accountID, headers)
    print('Reward total:', totalRewards)
    rewardValue = getRewardsValue(accountID, totalRewards, headers)
    print('Reward value:', rewardValue)
    
