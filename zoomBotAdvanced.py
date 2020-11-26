import webbrowser
import datetime
import pyautogui
import time


def canvasLogin():
    # opens browser to go through login process
    url = "https://iu.instructure.com/"

    webbrowser.open_new(url)
    time.sleep(10)

    pyautogui.moveTo(935, 383, duration=1)
    pyautogui.click()
    pyautogui.moveTo(935, 533, duration=1)
    pyautogui.click()
    pyautogui.moveTo(935, 437, duration=5)
    pyautogui.click()


def openZoom(link):
    # opening the zoom link
    new = 2
    autoraise = True

    webbrowser.open(link, new, autoraise)
    time.sleep(5)
    pyautogui.press("enter")
    pyautogui.moveTo(935, 507, duration=10)
    pyautogui.click()


def fileExists():
    # tries to open this file
    # if successful, close it and return true
    # otherwise return false
    try:
        f = open("classes.txt")
        f.close()
        return True
        # Do something with the file
    except IOError:
        print("File Doesn't Exist")
        return False


# ``````````````````````````````````````````````````````````````````````````
def setup():
    # goes through setup process,
    # collecting info about the classes
    # and adding them to the file
    classes = open("classes.txt", "w+")
    print("Beginning initial setup")
    print()

    amount = int(input("How many classes: "))
    for i in range(amount):
        className = input("Name of Class: ") + "\n"
        classDay = input("Day of Week: ")
        classStart = input("Start Time: ")
        classDayTime = classDay + " " + classStart + "\n"
        classURL = input("URL: ") + "\n"
        classes.writelines(className)
        classes.writelines(classDayTime)
        classes.writelines(classURL)
        classes.writelines("\n")

        print()

    classes.close()

    return classes


# `````````````````````````````````````````````````````````````````````````
def openClass(classLists):
    # gets current day and time info,
    # then compares this info to the
    # day and time of document.
    # afterwards it gets the link on the next line
    # and sends it to the open zoom function.

    # this is where my major aneurysm was

    currentDT = datetime.datetime.now()
    for word in classLists:
        if currentDT.strftime("%A %H:%M" + "\n") == word:
            canvasLogin()
            time.sleep(10)
            url = (next(classLists))
            openZoom(url)


# ``````````````````````````````````````````````````````````````````````````````
def main():
    # checking if the classes.txt file exists
    exists = fileExists()
    if exists:
        classList = open("classes.txt", "r")
        openClass(classList)
    else:
        print("neh")
        classList = setup()
        print("goodbye")


main()
