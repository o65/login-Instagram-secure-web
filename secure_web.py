import requests
import json

def login():
  
  global login_req

  username = input("Enter Your Username: ")
  password = input("Enter Your password: ")
  login_url = 'https://www.instagram.com/accounts/login/ajax/'
  login_header = {
      'accept': '*/*',
      'accept-encoding': 'gzip, deflate, br',
      'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
      'content-length': '291',
      'content-type': 'application/x-www-form-urlencoded',
      'cookie': 'ig_nrcb=1; mid=YfyRDwALAAE2u2Xao59RvgY4Kie1; ig_did=24EAD7A2-41F3-458B-81B2-4C4E87CE77AE; csrftoken=Gqpabe6S9nfg1355Y2zelxzotxiiUAD7',
      'origin': 'https://www.instagram.com',
      'referer': 'https://www.instagram.com/',
      'sec-fetch-dest': 'empty',
      'sec-fetch-mode': 'cors',
      'sec-fetch-site': 'same-origin',
      'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Edg/98.0.1108.43",
      'x-csrftoken': 'Gqpabe6S9nfg1355Y2zelxzotxiiUAD7',
      'x-ig-app-id': '936619743392459',
      'x-ig-www-claim': '0',
      'x-instagram-ajax': '9a16d12cf843',
      'x-requested-with': 'XMLHttpRequest'
    }
  login_data = {
        'username': username,
      'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:&:{password}',
      'queryParams': '{}',
      'optIntoOneTap': 'false'
      }

  login_req = requests.post(url=login_url, headers=login_header, data=login_data)

  if '"checkpoint_required"' in login_req.text:
    print(f"@{username} Is Secured \n\n")
    send_code()

  elif '"authenticated":true' in login_req.text:
    print(f'@{username} Logged In √ \n')
  else:
    print("error")


def send_code():	

  global security_code , checkpoint_url

  get_checkpoint_url = json.loads(login_req.text)
  if "checkpoint_url" in get_checkpoint_url:
    checkpoint_url = get_checkpoint_url.get("checkpoint_url")
    # print(checkpoint_url)

  send_code_url = f'https://www.instagram.com{checkpoint_url}'
  send_code_header = {

    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9,ar;q=0.8',
    'Alt-Used': 'www.instagram.com',
    'Connection': 'keep-alive',
    'Content-Length': '63',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': 'ig_nrcb=1; mid=YfyRDwALAAE2u2Xao59RvgY4Kie1; ig_did=24EAD7A2-41F3-458B-81B2-4C4E87CE77AE; csrftoken=Gqpabe6S9nfg1355Y2zelxzotxiiUAD7',
    'Host': 'www.instagram.com',
    'Origin': 'https://www.instagram.com',
    'Referer': 'https://www.instagram.com',
    'TE': 'Trailers',
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Edg/98.0.1108.43",
    'X-ASBD-ID': '437806',
    'X-CSRFToken': 'Gqpabe6S9nfg1355Y2zelxzotxiiUAD7',
    'X-IG-App-ID': '936619743392459',
    'X-IG-WWW-Claim': '0',
    'X-Instagram-AJAX': '9a16d12cf843',
    'X-Requested-With': 'XMLHttpRequest'
    }

  code = 1

  send_code_date = {
    'choice': code
    }

  send_code_req = requests.post(url=send_code_url, headers=send_code_header, data=send_code_date)

  if ("security_code") in send_code_req.text:

    choose_number = input("""[ 1 ] Enter the code ?    [ 2 ] Accept login without code ?
    
choose the number: """)
    if choose_number == '1':
       security_code= input("\nEnter your code: ")
       get_code()
    elif choose_number == '2':
       security_code = input('\nPress this was me in your account and press enter: ')
       get_code()

    else:
      print("Please chose 1 or 2 ")
      send_code()
	

def get_code():
  get_code_url = f'https://www.instagram.com{checkpoint_url}'
   
  get_code_header = {

    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9,ar;q=0.8',
    'Alt-Used': 'www.instagram.com',
    'Connection': 'keep-alive',
    'Content-Length': '63',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': 'ig_nrcb=1; mid=YfyRDwALAAE2u2Xao59RvgY4Kie1; ig_did=24EAD7A2-41F3-458B-81B2-4C4E87CE77AE; csrftoken=Gqpabe6S9nfg1355Y2zelxzotxiiUAD7',
    'Host': 'www.instagram.com',
    'Origin': 'https://www.instagram.com',
    'Referer': 'https://www.instagram.com',
    'TE': 'Trailers',
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Edg/98.0.1108.43",
    'X-ASBD-ID': '437806',
    'X-CSRFToken': 'Gqpabe6S9nfg1355Y2zelxzotxiiUAD7',
    'X-IG-App-ID': '936619743392459',
    'X-IG-WWW-Claim': '0',
    'X-Instagram-AJAX': '9a16d12cf843',
    'X-Requested-With': 'XMLHttpRequest'
    }
  
  get_code_data = {

    "security_code" : security_code

    }
  get_code_req = requests.post(url=get_code_url, headers=get_code_header, data=get_code_data)

  if '"status":"ok"' in get_code_req.text:
    print("login done")
  
  elif '"status":"fail"' in get_code_req.text:
    print("code is wrong")
    send_code()

  else:
    print(" error")

login()