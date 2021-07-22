from cryptography.fernet import Fernet   #module that will aloow you to encrypt text

'''def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)'''

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

key = load_key()
fer = Fernet(key)

# key + password + text to encrypt = random text
#random text + key + password = text to encrypt

def view():
     with open('passwords.txt','r') as f:  
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|") 
            print("User:", user, ", Password:",fer.decrypt(passw.encode()).decode())

def add():
    name = input("account name: ")
    password = input("password: ")

    with open('passwords.txt','a') as f:  #as f == means name of file is 'f'
        f.write(name + "|" + fer.encrypt(password.encode()).decode()  + "\n")


while True:
    mode = input("would you like to add a new password of view existing ones (view, add), press q to quit ? ").lower()
    if mode == "q":
        break

    if mode  == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("invalid password")
        continue

