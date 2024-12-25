import requests
import json
import time

#log to txt file
def log(txt):
    f = open('glacierelig.txt', "a")
    f.write(txt + '\n')
    f.close()

with open('addrlist.txt', 'r') as file:
    try:
        local_data = file.read().splitlines()
        for addrlist in local_data:
            url = f"https://p0.onebitdev.com/glacier-airdrop/api/check-whitelist?address={addrlist}"
            headers = {
                "Content-Type": "application/json",
                "Origin": "https://reward.glacier.io",
                "Referer": "https://reward.glacier.io/",
                "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0"
            }

            response = requests.get(url, headers=headers)
            data = response.json().get('data', {})
            is_elig = data.get('eligible')
            is_amount = data.get('max_buy')
            amount = int(is_amount) / (10**18)
            if 0 == is_elig:
                print(f'address {addrlist} not elig!')
            else:
                print(f'address {addrlist} elig!')
                print(f'with amount : {amount}')
                print(f'------------------------------------')
                # log(f'address {addrlist}')
                # log(f'data {data}')
                # log(f'------------------------------------')
    except requests.exceptions.RequestException as e:
        print(f'Error: str(e)')