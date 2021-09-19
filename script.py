import requests

# Start Banner !
from pyfiglet import Figlet
custom_fig = Figlet(font='tty')
print(custom_fig.renderText('Dumb Brute Forcer!!'))
# End Banner !

# Start Color Support !
import colorama
from colorama import Fore
from colorama import Style
colorama.init()
# End Color Support !

# Start Inputs !
ip = str(input("Enter An Ip Address: "))
port = int(input("add a port Number: "))
wordlist = str(input("Add A Wordlist: "))
# End Inputs !

# Start Wodlist Fetching !
file = open(wordlist, "r")
# End Wordlist Fetching !

# Start Requesting IPs And Checking Response Codes !
for word in file:
    api = requests.get(f"http://{ip}:{port}/{word.strip()}")
    if api.status_code != 404:
       print(f''' 
{Fore.GREEN}
*****************************************
Trying /{word}, Here's The Results:
[*] /{word} Exists!!
[*] Status Code: {api.status_code} 
*****************************************
{Style.RESET_ALL}''')
# End Requesting IPs And Checking Response Codes !
