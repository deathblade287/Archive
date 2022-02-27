import requests

status_code = 0

while status_code != 200:
    import requests
    url = 'http://worldagnetwork.com/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    result = requests.get(url, headers=headers)
    status_code = result.status_code
    print(status_code)
