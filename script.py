import requests
ip = str(input("Enter An Ip Address: "))
port = int(input("add a port Number: "))
wordlist = str(input("Add A Wordlist: "))
file = open(wordlist, "r")
for word in file:
    api = requests.get(f"http://{ip}:{port}/{word}")
    if api.status_code == 200 or api.status_code == 403 or api.status_code == 301 or api.status_code == 402 or api.status_code == 500:
       print(f'''Trying {word}, Good Luck And Here's The Results: 
                 *****************************************
                 [*] /{word} Exists!!
                 [-] Status Code: {api.status_code}
                 ----------------------------------------- ''')
