import requests
import os
import re
import time
import random
from requests.exceptions import RequestException
from time import sleep
import datetime
import threading

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,/;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
    'referer': 'www.google.com'
}

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def send_message_thread(access_token):
    try:
        while True:
            for line in lines:
                parameters = {'access_token': access_token.strip(), 'message': line}
                url = "https://graph.facebook.com/v15.0/{0}/".format(cuid)
                send_message = requests.post(url, data=parameters, headers=headers)
                print("Message Sent Done ::- ", line, '\n')
                time.sleep(t)
    except RequestException:
        print("[×] Error Connection.............\n")
        time.sleep(5.5)

while True:
    try:
        clear()
        
        # Read access tokens from files token.txt, token1.txt, token2.txt, token3.txt, token4.txt
        access_tokens = []
        for filename in ['token.txt', 'token1.txt', 'token2.txt', 'token3.txt', 'token4.txt']:
            with open(filename, 'r') as f:
                access_tokens.extend([line.strip() for line in f.readlines()])

        # Read conversation ID from file
        with open('convo.txt', 'r') as f:
            cid = int(f.read().strip())
            cuid = 't_' + str(cid)

        # Set the desired time delay
        t = 2

        # Set the notepad file name
        np = 'TEXTFILE.txt'

        # Read lines from the notepad file with the UTF-8 encoding
        with open(np, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        # Create and start a thread for each access token
        threads = []
        for access_token in access_tokens:
            thread = threading.Thread(target=send_message_thread, args=(access_token,))
            threads.append(thread)
            thread.start()

        # Wait for all threads to finish
        for thread in threads:
            thread.join()
            
    except Exception as e:
        print("An error occurred:", str(e))
        print("Restarting the script in 60 seconds...")
        time.sleep(60)  # Wait for 60 seconds before restarting
