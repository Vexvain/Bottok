from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pyfiglet
from os import system
import time

chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument("--headless")
chrome_options.add_argument("--log-level=3")
driver = webdriver.Chrome(r"chromedriver.exe", options=chrome_options)
driver.set_window_size(1024, 650)

i = 0
a = 0
x = 0

def loop1():
    global i
    time.sleep(10)
    try:
        driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[3]/div/div[4]/div/button").click()
    except:
        print("You didn't solve the captcha yet. Need to refresh to avoid endless loop.")
        driver.refresh()
        loop1()
    try:
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id=\"sid4\"]/div/div/div/form/div/input").send_keys(vidUrl)
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id=\"sid4\"]/div/div/div/form/div/div/button").click()
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id=\"c2VuZC9mb2xsb3dlcnNfdGlrdG9V\"]/div[1]/div/form/button").click()
        driver.refresh()
        i += 1
        total = i * 1000
        print("Views have been delivered! Total:", total,"views")
        time.sleep(55)
        loop1()
    except:
        print("An error occured. We'll try again")
        driver.refresh()
        loop1()

def loop2():
    global i
    time.sleep(10)
    try:
        driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[3]/div/div[2]/div/button").click()
    except:
        print("You didn't solve the captcha yet. Need to refresh to avoid endless loop.")
        driver.refresh()
        loop2()
    try:
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[4]/div[3]/div/div/div/form/div/input").send_keys(vidUrl)
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div[4]/div[3]/div/div/div/form/div/div/button").click()
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[4]/div[3]/div/div/div/div/div[1]/div/form/button").click()
        driver.refresh()
        hearts = driver.find_element_by_xpath('//*[@id="c2VuZE9nb2xsb3dlcnNfdGlrdG9r"]/span').text
        print(hearts,"Hearts have been delivered!")
        time.sleep(605)
        loop2()
    except:
        print("An error occured. We'll try again")
        driver.refresh()
        loop2()


def loop3():
    time.sleep(10)
    try:
        driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[3]/div/div[1]/div/button").click()
    except:
        print("You didn't solve the captcha yet. Need to refresh to avoid endless loop.")
        driver.refresh()
        loop4()
    try:
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div/div/form/div/input").send_keys(username)
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div/div/form/div/div/button").click()
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div/div/div/form/button").click()
        time.sleep(2)
        folls = driver.find_element_by_xpath('//*[@id="c2VuZF9mb2xsb3dlcnNfdGlrdG9r"]/span').text
        print(folls)
        driver.refresh()
        time.sleep(318)
        loop4()
    except:
        print("An error occured. We'll try again")
        driver.refresh()
        loop4()

vidUrl = "YOUR_URL" #Change YOUR_URL to any TikTok video URL
username = "YOUR_USERNAME" #Change YOUR_USERNAME to the username of the user that uploaded the TikTok video

system("cls")
bottok = pyfiglet.figlet_format("BOTTOK", font="slant")
print(bottok)
print("Vexvain")
print("")

"""
You can change the auto value below
auto = 1 for auto views
auto = 2 for auto hearts
auto = 3 for auto followers
"""
auto = 1 #Change this

if auto == 1:
    driver.get("https://vipto.de/")
    loop1()
elif auto == 2:
    driver.get("https://vipto.de/")
    loop2()
else:
    driver.get("https://vipto.de/")
    loop3()
