import requests
import time
from faker import Faker
from random import choice
from fake_useragent import UserAgent
from concurrent.futures import ThreadPoolExecutor

input_referral = input("Your Referral Link : ")

if input_referral:
  url_proxies = "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt"
  proxies_response = requests.get(url_proxies)
  proxies = proxies_response.text.split('\n')
  proxies = [proxy.strip() for proxy in proxies if proxy.strip()]
  
  ua = UserAgent()
  user_agent = ua.random
  headers = {'User-Agent': user_agent}
  proxy = {
    'http':  choice(proxies)
  }
  
  session_cookie = requests.Session() 
  response_cookie = session_cookie.get(input_referral, headers=headers, proxies=proxy) 
  get_cookie = session_cookie.cookies.get_dict()
  cookie = {"ref": get_cookie["ref"]}
  password = "abcd12345"
  f = Faker()
  url = 'https://crypcet.com/wp-admin/admin-ajax.php'
  
  def create_user ():
    ua = UserAgent()
    user_agent = ua.random
    headers = {'User-Agent': user_agent}
    proxy = {
      'http':  choice(proxies)
    }
    username = f.user_name()
    email = f.email()
    data = {
      'action': 'register_user_front_end',
      'username':  username,
      'email': email,
      'password': password,
      'confirm': password
    }
  
    try:
      response = requests.post(url, cookies=cookie, data=data, headers=headers, proxies=proxy)
    except Exception as err:
      print ("No Internet Connection!")
      return create_user()
    if response.text == "1":
      text = "Success!"
    else:
      text = "Failed!!"
    print(f"""
--------------------------------
Username : {username}
Email : {email}
Account Create : {text}
Output : {response.text}
Proxy HTTP : {proxy["http"]}
User Agent : {user_agent}
--------------------------------
  """)
    return response.text == "1"

  while True:
    if not create_user():
      print ("Enable/Disable Airplane Mode!")
else:
  print ("Referral Links Must Not Be Empty!")