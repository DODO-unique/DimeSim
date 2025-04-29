import requests
import time
count=0
url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=inr"
while True:
    response = requests.get(url)

    print("Fetching data", end="")

    for _ in range(3):
        time.sleep(1)
        print(".", end="", flush=True)

    print()
    data=response.json()
    print(data)

    count+=1
    if count == 10:
        break

    time.sleep(10)