import requests

def get_exchange():
    url = 'https://api.exchangeratesapi.io/latest'
    r=requests.get(url)
    print(f'Status Code: {r}')
    response_dict=r.json();
    exchange_rate=response_dict.get('rates')
    if 'USD' in exchange_rate:
        return exchange_rate['USD'];
    else:
        return;
#get_excange()
dollars=int(input('How Many Dollars Do You Have?$'))
rate=get_exchange()
for i in range(dollars):
    pounds_plain=rate / dollars
    pounds=round(pounds_plain, 5)
print(pounds)