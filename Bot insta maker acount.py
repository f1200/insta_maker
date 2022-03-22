import os
global STAT
info=[]
from telegram.ext import Updater, MessageHandler, Filters
lib =2
updater = Updater(token="التوكن")
dispatcher = updater.dispatcher
# بوت عمل حساب انستغرام 
#المطور بارون
# نعتذر على شكل الكود لاني كنت اجرب فيه ولم اهتم كفايه به
#طوره وحاول ان تذكر المصدر
# المصدر فريق البارون  @adowat
if lib == "1":
    os.system('pip install requests')
    os.system('pip install user_agent')
    os.system('cls' if os.name == 'nt' else 'clear')
    pass
else:
    os.system('cls' if os.name == 'nt' else 'clear')
    pass

import requests
import random
import secrets
from time import sleep, time
from user_agent import generate_user_agent
from telegram.ext import Updater, MessageHandler, Filters
import telepot
# Class of different styles
class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'
banner = ("""
-----
      ]
      ----#CodedBy BT------------------------------------//
                                                        
__________BARON TEAM @adowat channel___________________//

""")
print('\033[32m'+banner)
def smssend(url2,head,data2,r,code,id_msg,tok,ID,phone):
           print("send __________________________________SMS   DONE")
           Make_Acc2 = r.post(url2,headers=head,data=data2)
           if 'Looks like your phone number may be incorrect.' in Make_Acc2.text :
            start_msg = requests.post(f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text= خطأ في رقم هاتفك الرجاء ادخال رقم صالح").json()
            exit()
           elif 'Please wait a few minutes before you try again.' in Make_Acc2.text:
            start_msg = requests.post(f"https://api.telegram.org/bot{tok}/editmessagetext?chat_id={ID}&message_id={id_msg}&text= قبل ان تحاول مرة اخرى الرجاء الانتظار قليلا").json()
            
           elif 'true' in Make_Acc2.text:
            start_msg = requests.post(f"https://api.telegram.org/bot{tok}/editmessagetext?chat_id={ID}&message_id={id_msg}&text= تم ارسال الرسالة بنجاح").json()
            pass
           else:
            start_msg = requests.post(f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text= خطأ الان").json()
            pass
           start_msg = requests.post(f"https://api.telegram.org/bot{tok}/editmessagetext?chat_id={ID}&message_id={id_msg}&text=  $ ادخــــــــــــل الكود الذي استلمته الان").json()
           if code==0:
            print('go to get a new code ')      
            start_msg = requests.post(f"https://api.telegram.org/bot{tok}/editmessagetext?chat_id={ID}&message_id={id_msg}&text= {code} الكود الذي استلمته الان").json()
            start()
def crreate(r,url3,head,data3,tok,ID,id_msg,paas,user,phone):
        token=tok
        myID=ID
        print("INSIDE CREATE <<<<<<<<<<<<<<<<<<<<<")
        Make_Acc3 = r.post(url3,headers=head,data=data3)
        if "That code isn't valid." in Make_Acc3.text:
            print("[!] That code isn't valid")
            exit()
        elif 'true' in Make_Acc3.text:
            print("[-] Done Created Account")
            start_msg = requests.post(f"https://api.telegram.org/bot{tok}/editmessagetext?chat_id={ID}&message_id={id_msg}&text= {paas} والرمز {user}").json()
            pass
        elif "checkpoint_required" in Make_Acc3.text:

            print('[!] Done, checkpoint required')
            pass
        else:
            print(Make_Acc3.text)
            print('[!] Error ..')
            exit()
        Account = 'https://api.telegram.org/bot{}/sendMessage?chat_id={}&text=⌯ Instagram Fake Account  \n⌯ User : {}\n⌯ Pass : {}\n⌯ Ch : @Berlin_Tools'.format(token,myID,user,paas)
        r.get(Account)
        start_msg = requests.post(f"https://api.telegram.org/bot{tok}/editmessagetext?chat_id={ID}&message_id={id_msg}&text= {paas} ههههه").json()
       

def Make(ID,phone,CODE):
    myID=ID ##################
    code=CODE##################
    print("In Make")
    tok   ='1975399665:AAEwcl6E0zHOdD8XnsTT4etBk_DP-tsZ2tc'
    start_msg = requests.post(f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text= بدء").json()
    id_msg = start_msg['result']['message_id']

    while 1:
        idd    = 'X5uC6wALAAF-Lw3oSZE9kuY0mP_9'
        r      = requests.Session()
        cookie = secrets.token_hex(8)*2
        token   ='التوكن هنا ايضا'
        chars  = 'abcdefghijklmnopqrstuvwxyz123456789'
        if myID == "":
            start_msg = requests.post(f"https://api.telegram.org/bot{tok}/editmessagetext?chat_id={ID}&message_id={id_msg}&text= خطأ في معرفك احذف المحادثة وعاود الارسال").json()
            exit()
            
        else:
            token   ='1975399665:AAEwcl6E0zHOdD8XnsTT4etBk_DP-tsZ2tc'
            pass
        if phone == "":
            start_msg = requests.post(f"https://api.telegram.org/bot{tok}/editmessagetext?chat_id={ID}&message_id={id_msg}&text=  !خطأ في رقم هاتفك الرجاء ادخال رقم صالح").json()
        else:
            pass
        userr  = ""
        passs  = ""
        for x in range(0,10):
            userr_char = random.choice(chars)
            userr      = userr + userr_char
        for i in range(0,8):
            passs_char = random.choice(chars)
            passs      = passs + passs_char   
        paas   = passs
        user   = (f'ba{userr}')
        name   = (f'baron{userr}')
        url1   = 'https://www.instagram.com/accounts/web_create_ajax/attempt/'
        url2   = 'https://www.instagram.com/accounts/send_signup_sms_code_ajax/'
        url3   = 'https://www.instagram.com/accounts/web_create_ajax/'
        head   = {
            'HOST': "www.instagram.com",
            'KeepAlive' : 'True',
            'user-agent' : generate_user_agent(),
            'Cookie': cookie,
            'Accept' : "*/*",
            'ContentType' : "application/x-www-form-urlencoded",
            "X-Requested-With" : "XMLHttpRequest",
            "X-IG-App-ID": "936619743392459",
            "X-Instagram-AJAX" : "missing",
            "X-CSRFToken" : "missing",
            "Accept-Language" : "en-US,en;q=0.9"
        }

        data1   = {
            'enc_password': '#PWD_INSTAGRAM_BROWSER:0:1589682409:{}'.format(paas),
            'phone_number': phone,
            'username': user,
            'first_name': name,
            'month': '1',
            'day': '1',
            'year': '1999',
            'client_id': idd,
            'seamless_login_enabled': '1',
            'opt_into_one_tap': 'fals'
        }
        data2   = {
            'client_id': idd,
            'phone_number': phone,
            'phone_id': '',
            'big_blue_token': ''
        }
        data3 = {
            'enc_password': '#PWD_INSTAGRAM_BROWSER:0:1589682409:{}'.format(paas),
            'phone_number': phone,
            'username': user,
            'first_name': name,
            'month': '3',
            'day': '9',
            'year': '1999',
            'sms_code': code,
            'client_id': idd,
            'seamless_login_enabled': '1',
            'tos_version': 'row'
        }
        Make_Acc1 = r.post(url1,headers=head,data=data1)
        larg=len(phone)
        print(larg)
        if larg != 6:
            print("send sms")
            smssend(url2,head,data2,r,code,id_msg,tok,ID,phone)
        else:
            
            print("GO to creaaate")
            crreate(url3,head,data3,tok,ID,id_msg,paas,user,phone)
            
          
            


def start(bot, update):
    xx=update.message.text
    ID=update.message.chat_id
    if len(xx)!=6:
        print("This a pHONE >>>>>>>>......",xx)
        info.append(xx)
        phone=xx
        CODE=0
        Make(ID,phone,CODE)
    else:
        CODE=xx
        if len(CODE)==6:
            print("Create ACCOUNT >>>>>>>>......",len(CODE) ," AND ")
            phone=int(info[0])
            print(info[0])
            Make(ID,phone,CODE)
    



start_handler = MessageHandler(Filters.text, start)
dispatcher.add_handler(start_handler)
updater.start_polling()
updater.idle()