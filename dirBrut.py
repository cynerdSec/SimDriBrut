import requests
def bruteFun(url):
    try:
        return requests.get("http://"+url)
    except requests.exceptions.ConnectionError:
        pass
try:
    target_url = input("[*] Enter Targert url : ")
    wordlist_file = "common.txt"
    file = open(wordlist_file,'r')
    for line in file:
        dir = line.strip()
        full_url = target_url + "/" +dir
        resp = bruteFun(full_url)
        add_http_url = "http://" + full_url
        stat_code = str(resp.status_code)
        if resp:
            print("[#] Discovered Directories  : {}  Status code : {}".format(add_http_url,stat_code))
except KeyboardInterrupt:
    print("\nExiting Program......")