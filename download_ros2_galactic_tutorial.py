import os, time, re, shutil, sys
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#global rx patterns
yesRx = re.compile(r'^((y)|(yes))$', re.IGNORECASE)
noRx = re.compile(r'^((n)|(no))$', re.IGNORECASE)

#global variables
lesson_n = 0

#functions
def dirExists():
    redownload = input("The directory 'ROS 2 Galactic Tutorials' already exists in your 'Documents' folder. Would you like to delete and reinstall the tutorial?: ")
    if(re.match(yesRx, redownload)):
        shutil.rmtree('ROS 2 Galactic Tutorials')
    elif(re.match(noRx, redownload)):
        print("Cancelling download...")
        sys.exit()
    else:
        print("Failed to understand input. Please type 'yes' or 'no'")
        dirExists()
    return

#save the directory of the program in a variable
home_dir = os.getcwd()

#Create tutorials directory and configure to work in it
direc = input("Please paste the path to the directory where you would like to download the ROS2 Tutorial: ")
if((Path(direc)).exists() and Path(direc).is_dir):
    os.chdir(direc)
if((Path.cwd() / 'ROS 2 Galactic Tutorials').exists()):
    dirExists()
os.mkdir("ROS 2 Galactic Tutorials")
os.chdir("ROS 2 Galactic Tutorials")
tutorial_dir = os.getcwd() #save directory path

#begin selenium automation process
try:
    browser = webdriver.Chrome()
except:
    print("Chromedriver not on PATH")
    chromedriver = input("Please make sure Chrome and Chromedriver are installed to your PC and paste the full path to your chromedriver file here (may end in chromedriver or chromedriver.exe depending on your OS): ")
    browser = webdriver.Chrome(chromedriver)
browser.get("http://docs.ros.org/en/galactic/Tutorials.html")

all_lessons = browser.find_elements_by_css_selector("div.section div.section a.reference.internal")
print(len(all_lessons))
for i in all_lessons:
    lesson_n += 1
    file = open(f"{lesson_n}_{i.text}.html", "w")
    i.click()
    time.sleep(1)
    source = browser.page_source
    file.write(source)
    file.close()
    browser.back()
browser.close()
print("Download complete. Check your ROS2 Galactic Tutorials folder to see the HTML files. Open with a web browser to see the tutorials.")
sys.exit()