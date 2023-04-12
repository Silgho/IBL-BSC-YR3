import requests

apiToken = 'YOUR_API_TOKEN'
apiUrl = 'https://api.binary.com'

def getLastDigit(contractId):
    return int(str(contractId)[-1])

def getEvenContracts():
    contractsUrl = f"{apiUrl}/contracts_for"
    headers = {'Content-Type': 'application/json', 'x-api-token': apiToken}
    response = requests.get(contractsUrl, headers=headers).json()
    evenContracts = [contract for contract in response['contracts'] if getLastDigit(contract['contract_id']) % 2 == 0]
    return evenContracts

def calculate_next_stake(previous_loss, martingale_factor):
    return previous_loss * martingale_factor

def place_trade(contractId, stake, profitTarget):
    buyUrl = f"{API_URL}/buy"
    headers = {'Content-Type': 'application/json', 'x-api-token': apiToken}
    data = {
        'price': stake,
        'amount': profitTarget,
        'contract_id': contractId,
        'basis': 'stake',
        'duration': 5,
        'duration_unit': 't',
        'currency': 'USD'
    }
    response = requests.post(buyUrl, headers=headers, json=data).json()
    return response

martingalEFactor = 2
initialStake = 1

while True:
    evenContracts = getEvenContracts()
    if not evenContracts:
        print("No even last digit contracts available.")
        break
    contractId = evenContracts[0]['contract_id']
    stake = initialStake
    while True:
        profitTarget = stake * 3
        tradeResult = place_trade(contractId, stake, profitTarget)
        if tradeResult['error']:
            print(f"Error: {tradeResult['error']['message']}")
            break
        elif tradeResult['buy']['payout'] == 0:
            loss = stake
            stake = calculate_next_stake(loss, martingalEFactor)
            print(f"Trade lost. Next stake amount: {stake}")
        else:
            print(f"Trade won. Profit: {tradeResult['buy']['payout']}")
            break