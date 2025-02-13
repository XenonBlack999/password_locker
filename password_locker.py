#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os,random,string,sqlite3
from colorama import Fore, Style
from tabulate import tabulate
from cryptography.fernet import Fernet
import time,webbrowser



KEY_FILE = "secret.key"

logo = rf"""{Fore.RED}
       ,-.                               
       ___,---.          /'|`\          ,---,___          
    ,-'    \`    -.____,-'  |  -.____,-'    //    `-.       
  ,'        |           ~'\     /~           |        .      
 /      ___//              `. ,'          ,  , \___      \    
|    ,-'   -.__   _         |        ,    __,-'   -.    |    
|   /          /\_  `   .    |    ,      _/\          \   |   
\  |           \ \`-.___ \   |   / ___,-'/ /           |  /  
 \  \           | `._   `\\  |  //'   _,' |           /  /      
  -.\         /'  _ ---'' , . ``---' _  `\         /,-'     
     ``       /     \    ,='/ \`=.    /     \       ''          
             |   /|\_,--.,-.--,--._/|\   |                  
             /  `./  \\`\ |  |  | /,//' \,'  \                  
            /   /     ||--+--|--+-/-|     \   \                 
           |   |     /'\_\_\ | /_/_/`\     |   |                
            \   \__, \_     `~'     _/ .__/   /            
             -._,-'   -._______,-'   `-._,-'
             Xenon Black
             Password Locker V 1.0
{Style.RESET_ALL}"""


def creating_db():
    con = sqlite3.connect("fuckyou.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS password (webname TEXT, name TEXT, password TEXT)")
    con.commit()
    con.close()
    print("Done!")
    
def load_key():
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as key_file:
            key_file.write(key)
    else:
        with open(KEY_FILE, "rb") as key_file:
            key = key_file.read()
    return Fernet(key)

cipher = load_key()



def check_update(webname, name, password):
    if not os.path.exists("fuckyou.db"):
        creating_db()
        print("Database is not have but we create now!")
    else:
        insert_data(webname, name, password)
        
        
        
        
        

def insert_data(webname, name, password):
    encrypted_password = encrypt_password(password)
    conn = sqlite3.connect("fuckyou.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO password (webname, name, password) VALUES (?, ?, ?)",
                   (webname, name, encrypted_password))
    conn.commit()
    conn.close()
    print("Credentials saved successfully!")
    
    


def show_all_passwords():
    con = sqlite3.connect("fuckyou.db")
    cur = con.cursor()
    data = list(cur.execute("SELECT webname, name, password FROM password ORDER BY webname"))
    con.close()
    if data:
        print(tabulate(data, headers=["Website", "Username", "Password"], tablefmt="grid"))
    else:
        print("No stored credentials found.")
        
        
        
        


def retrieve_password(webname):
    con = sqlite3.connect("fuckyou.db")
    cur = con.cursor()

    cur.execute("SELECT webname, name, password FROM password WHERE webname = ?", (webname,))
    
    result = cur.fetchone()
    
    if not result:
        print("⚠️ No stored credentials found.")
        return

    print("\n🔐 Stored Credentials:")
    
    website, username, encrypted_password = result
    password = decrypt_password(encrypted_password)
    print(f"🌐 {website} | 👤 {username} | 🔑 {password}")
    
    con.close()
    
    
    
    

def generate_password(length, use_upper, use_digits, use_special):
    char_pool = string.ascii_lowercase
    
    if use_upper:
        char_pool += string.ascii_uppercase
    if use_digits:
        char_pool += string.digits
    if use_special:
        char_pool += string.punctuation
    password = ''.join(random.choice(char_pool) for _ in range(length))
    print(f"Generated Password: {password}")
    
    
def encrypt_password(password):
    return cipher.encrypt(password.encode()).decode()

def decrypt_password(encrypted_password):
    return cipher.decrypt(encrypted_password.encode()).decode()

def self_encryption(user_string):
    en_str = cipher.encrypt(user_string.encode()).decode()
    print("Your encrypt string was:", en_str)
    
def self_decryption(user_string):
    de_str = cipher.decrypt(user_string.encode()).decode()
    print("Your decrypt string was:", de_str)
    

def password_handler():
    try:
        length = int(input("Input your password length: "))
    except ValueError:
        print("Invalid input for length! Please enter a number.")
        return

    use_upper = input("Do you want to use upper case? [Y/n]: ").lower()
    use_digits = input("Do you want to use Digits? [Y/n]: ").lower()
    use_special = input("Do you want to use special Characters? [Y/n]: ").lower()

    if use_upper not in ['y', 'n']:
        print("Invalid input for uppercase choice!")
        return

    if use_digits not in ['y', 'n']:
        print("Invalid input for digits choice!")
        return

    if use_special not in ['y', 'n']:
        print("Invalid input for special characters choice!")
        return

    use_upper = use_upper == 'y'
    use_digits = use_digits == 'y'
    use_special = use_special == 'y'

    generate_password(length, use_upper, use_digits, use_special)

def sleepy():
    print("I think you are sleepy now.So,Let's play")
    while True:
        print('Happy Hacking brother....')
        os.system("firefox https://osintframework.com/")
        time.sleep(.1)

    
    
    
    
def function_handler():
    print("Select The Function from the following")
    load_key()
    creating_db()
    list1 = """
    1. Random Password Generator 
    2. Password Store in Database
    3. Password Gathering from Database
    4. Password Gathering All from Database
    5. Self Encryption
    6. Self Decryption
    """
    print(list1)
    
    response2 = input("Input your Chosen function number: ") 
    
    if response2 == '1':
        password_handler()
        
    elif response2 == '2':
        webname = input ("Input your Website name :")
        name = input ("Input your user name or email:")
        password = input ("Input your Password:")
        insert_data(webname, name, password)
        
    
    elif response2 == '3':
        webname = input("Input the website name to retrieve password: ")
        retrieve_password(webname)
        
        
    elif response2 == '4':
        show_all_passwords()
        
    elif response2 == '5':
        user_string = input("Input your string to encrypt:")
        self_encryption(user_string)
    
    elif response2 == '6':
        user_string = input("Input your code to decrypt:")
        self_decryption(user_string)
        
    elif response2 == '7':
        sleepy()
    else:
        print("I think something was wrong. Try again later....")

        

    
    
def main():
    print(logo)
    print("Wellcome to my Password Locker Tool")
    response = input("Do you want to start?[Y/n]")
    response1 = response.lower()
    if response1 == 'y':
        function_handler()
    else  :
        print("We are now Exit from Password Locker Tool.....")
        
    
if __name__ == "__main__":
    main()
    
