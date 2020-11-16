import webbrowser
# import datetime
import pyautogui
import time


# https://iu.zoom.us/signin

# `````````````````````````````````````````````````````
# iu login: iu.instructure.com/
# 935, 330
# 935 383
# 935 533
# 935 437
# ````````````````````````````````````````````````````
def canvasLogin():
    url = "https://iu.instructure.com/"

    webbrowser.open_new(url)
    time.sleep(10)

    pyautogui.moveTo(935, 383, duration=1)
    pyautogui.click()
    pyautogui.moveTo(935, 533, duration=1)
    pyautogui.click()
    pyautogui.moveTo(935, 437, duration=5)
    pyautogui.click()


def openZoom(picked):
    new = 2
    autoraise = True

    if picked == 1:
        # UX DESIGN
        url = "https://iu.zoom.us/j/93158763962"
        webbrowser.open(url, new, autoraise)
        time.sleep(5)
        pyautogui.press("enter")
        pyautogui.moveTo(935, 507, duration=10)
        pyautogui.click()
        # 935, 563
    elif picked == 2:
        # HUMAN RELATIONS
        # ````````````````````````````````````````````
        url = "https://iu.zoom.us/signin"
        webbrowser.open(url, new, autoraise)
        time.sleep(10)

        pyautogui.moveTo(935, 383, duration=1)
        pyautogui.click()
        pyautogui.moveTo(935, 533, duration=1)
        pyautogui.click()
        pyautogui.moveTo(935, 437, duration=5)
        pyautogui.click()
        time.sleep(10)
        # `````````````````````````````````````````````````
        url = "https://iu.zoom.us/j/99744507454?pwd=S2JiTFpVL1I0bDA3WFRDdGVoemFQUT09"
        webbrowser.open(url, new, autoraise)
        time.sleep(5)
        pyautogui.press("enter")
        pyautogui.moveTo(935, 507, duration=10)
        pyautogui.click()
    elif picked == 3:
        url = "https://iu.zoom.us/j/92140536878"
        webbrowser.open(url, new, autoraise)
        time.sleep(5)
        pyautogui.press("enter")
        pyautogui.moveTo(935, 507, duration=10)
        pyautogui.click()


def main():
    while True:
        while True:
            print("Which Class to Attend?")
            print()
            print("1. UX design")
            print("2. Human Relations")
            print("3. DBMS")
            print("4. EXIT")
            print()

            choice = int(input())
            if choice > 0 & choice < 5:
                break
            else:
                print("Must be 1-4")
                continue

        if choice == 4:
            confirm = int(input("Are you sure? 1 for yes, 0 for no. "))
            if confirm == 1:
                break
        else:
            canvasLogin()
            time.sleep(10)
            openZoom(choice)


main()
