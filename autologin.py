from selenium import webdriver
from getpass import getpass
from selenium.common.exceptions import NoSuchElementException
from time import sleep


options = webdriver.ChromeOptions() 
options.add_argument("start-maximized")


username = input("Enter username: ")

password = getpass("Enter password: ")

driver = webdriver.Chrome(options=options, executable_path=r'C:\Users\muzza\Downloads\chromedriver_win32\chromedriver.exe')

driver.get("https://discord.com/login")


def main():
    try:
        user = driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div/div/form/div/div/div[1]/div[2]/div[1]/div/div[2]/input")
        user.send_keys(username)
    except NoSuchElementException:   
        pass

    try:
        passw = driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div/div/form/div/div/div[1]/div[2]/div[2]/div/input")
        passw.send_keys(password)
    except NoSuchElementException: 
        pass

    try:
        sub = driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div/div/form/div/div/div[1]/div[2]/button[2]")
        sub.click()
    except NoSuchElementException: 
        pass

    print("Logged in successfully")

    sleep(1)

    driver.get("https://discord.com/channels/@me")

    sleep(1000)

if __name__ == "__main__":
    main()
