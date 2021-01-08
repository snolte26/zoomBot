import webbrowser
import datetime
import pyautogui
import time


def canvasLogin(school, username, password):
    # opens browser to go through login process
    url = school

    webbrowser.open_new(url)
    time.sleep(10)

    pyautogui.typewrite(username)
    pyautogui.press("tab")

    pyautogui.typewrite(password)
    pyautogui.press("enter")
    
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("enter")
    time.sleep(5)


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
    
    school = input("Enter Canvas link"
                   "(i.e. https://iu.instructure.com/): ") + "\n"
    classes.writelines(school)

    username = input("Enter Username: ") + "\n"
    password = input("Enter Password: ") + "\n"
    classes.writelines(username)
    classes.writelines(password)

    classes.writelines("\n")

    amount = int(input("How many classes: "))
    for i in range(amount):
        className = input("Name of Class: ") + "\n"
        classDay = input("Day of Week (i.e. Sunday): ")
        classStart = input("Start Time (24 hr i.e. 13:30): ")
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

    found = False
    
    for word in classLists:
        if "instructure" in word:
            word = word.replace("\n", "")

            user = (next(classLists))
            user = user.replace("\n", "")

            passw = (next(classLists))
            passw = passw.replace("\n", "")

            canvasLogin(word, user, passw)

    while True:
        currentDT = datetime.datetime.now()

        for word in classLists:
            if currentDT.strftime("%A %H:%M" + "\n") == word:
                # start opening the zoom link
                time.sleep(10)
                url = (next(classLists))
                openZoom(url)
                # end opening the zoom link
                found = True
        if found:
            break


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
