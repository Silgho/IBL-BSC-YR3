import requests

API_TOKEN = 'YOUR_API_TOKEN'
API_URL = 'https://api.binary.com'

# Utility function to get last digit of a contract id
def get_last_digit(contract_id):
    return int(str(contract_id)[-1])

# Function to get list of available contracts that have an even last digit
def get_even_contracts():
    contracts_url = f"{API_URL}/contracts_for"
    headers = {'Content-Type': 'application/json', 'x-api-token': API_TOKEN}
    response = requests.get(contracts_url, headers=headers).json()
    even_contracts = [contract for contract in response['contracts'] if get_last_digit(contract['contract_id']) % 2 == 0]
    return even_contracts

# Function to calculate the next stake amount based on the previous loss
def calculate_next_stake(previous_loss, martingale_factor):
    return previous_loss * martingale_factor

# Function to place a trade on an even last digit contract with a 300% profit target
def place_trade(contract_id, stake, profit_target):
    buy_url = f"{API_URL}/buy"
    headers = {'Content-Type': 'application/json', 'x-api-token': API_TOKEN}
    data = {
        'price': stake,
        'amount': profit_target,
        'contract_id': contract_id,
        'basis': 'stake',
        'duration': 5,
        'duration_unit': 't',
        'currency': 'USD'
    }
    response = requests.post(buy_url, headers=headers, json=data).json()
    return response

# Define the martingale factor and initial stake amount
MARTINGALE_FACTOR = 2
INITIAL_STAKE = 1

# Main trading loop
while True:
    even_contracts = get_even_contracts()
    if not even_contracts:
        print("No even last digit contracts available.")
        break
    contract_id = even_contracts[0]['contract_id']
    stake = INITIAL_STAKE
    while True:
        profit_target = stake * 3
        trade_result = place_trade(contract_id, stake, profit_target)
        if trade_result['error']:
            print(f"Error: {trade_result['error']['message']}")
            break
        elif trade_result['buy']['payout'] == 0:
            loss = stake
            stake = calculate_next_stake(loss, MARTINGALE_FACTOR)
            print(f"Trade lost. Next stake amount: {stake}")
        else:
            print(f"Trade won. Profit: {trade_result['buy']['payout']}")
            break