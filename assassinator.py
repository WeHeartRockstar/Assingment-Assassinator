try:
    import requests, time, os, sys, json, threading, random, getpass
    import undetected_chromedriver as uc

    from colorama import *
    from selenium import webdriver

    from selenium.common.exceptions import ElementNotInteractableException, TimeoutException
    from selenium.common.exceptions import NoSuchElementException
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.common.exceptions import WebDriverException
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support import expected_conditions as EC  
    from selenium.webdriver.common.action_chains import ActionChains
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support.ui import Select
except ModuleNotFoundError:
    print(Fore.YELLOW + "[!] Installing missing modules [!]" + Fore.RESET)
    os.system("pip3 install colorama")
    os.system("pip3 install selenium")
    os.system("pip3 install undetected_chromedriver")
    os.system("pip3 install requests")

options = webdriver.ChromeOptions()

options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36")
options.add_argument("--window-size=1920,1080")
options.add_argument("--ignore-certificate-errors")
options.add_argument("--allow-running-insecure-content")
options.add_argument("--disable-extensions")
options.add_argument("--proxy-server='direct://'")
options.add_argument("--proxy-bypass-list=*")
options.add_argument("--start-maximized")
options.add_argument("--disable-gpu")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")
options.add_experimental_option("excludeSwitches", ["enable-logging"])

#-------------------Interface stuff & Config Data-----------------------------#
os.system("title Assignment Assassinator")
name = getpass.getuser()

with open('data\config.json') as f:
    data = json.load(f)

edpuzzle_token = data["token"]

#-------------------Widly used program functions-----------------------------#
def exit():
    os.system("cls")
    sys.exit()

def return_back():
    os.system("cls")
    return welcome()

def random_name():
    usernames = open("data/usernames.txt").read().splitlines()
    random_username = random.choice(usernames)

    return random_username

#-------------------Interface Code-----------------------------#

def welcome():

    print(Fore.LIGHTRED_EX + '''
▄▀█ █▀ █▀ █ █▀▀ █▄░█ █▀▄▀█ █▀▀ █▄░█ ▀█▀   ▄▀█ █▀ █▀ ▄▀█ █▀ █▀ █ █▄░█ ▄▀█ ▀█▀ █▀█ █▀█
█▀█ ▄█ ▄█ █ █▄█ █░▀█ █░▀░█ ██▄ █░▀█ ░█░   █▀█ ▄█ ▄█ █▀█ ▄█ ▄█ █ █░▀█ █▀█ ░█░ █▄█ █▀▄''' + Fore.RESET)
    print(f"User Logged in > {name}")
    print("")
    return menu()

def menu():
    
    print("(0) Exit")
    print("(1) Quizlet")
    print("(2) EdPuzzle")
    print("(3) Kahoot")
    print("")
    options = input("Enter Number of tool > ")

    if options == "0":
        return_back()
    elif options == "1":
        print("")
        print("(0) Exit")
        print("(1) Autosolve")
        print("")

        quizlet_options = input("Enter Number of tool > ")
        if quizlet_options == "0":
            return_back()
        elif quizlet_options == "1":
            Quizlet.autosolve()
    elif options == "2":
        pass
    elif options == "3":
        Kahoot.start_flooder()

#----------------------------------Start of the code you're probably looking for | I have more code but it isn't finished so no point in uploading ---------------------------------------------------#

class Kahoot:

    def flooder(pin):
        
        username = random_name()
        options.headless = True
        driver = uc.Chrome(options = options)

        
        try:
            driver.get(f"https://kahoot.it?pin={pin}")
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="nickname"]')))
            driver.find_element_by_xpath('//*[@id="nickname"]').send_keys(username + Keys.RETURN)
            #WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div[1]/div/div[3]/div[2]/main/div/form/button')))           
            print(Fore.GREEN + f"[!] Flooded Kahoot {pin} with username {username} [!]" + Fore.RESET)
        except KeyboardInterrupt:
            driver.close()
            driver.quit()
            return_back()

    def start_flooder():

        print(Fore.YELLOW + "[INFO] Press CTRL + C to stop flooding [INFO]" + Fore.RESET)
        print(Fore.YELLOW + "[INFO] Using too many bots may crash your computer [INFO]" + Fore.RESET)
        print("")

        bots = int(input("Enter Number of bots you want to join > "))
        pin = str('6125283')#str(input("Enter Game Pin > "))

        for i in range(bots):
            t = threading.Thread(target=Kahoot.flooder(pin))
            t.start()
           
if __name__ == "__main__":
    welcome()
