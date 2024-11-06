import time, random
import pyautogui

groups = [106019756560100,
          343119952453091,
          "wordpressonlinejobs",
          "wppremiumthemeplugin",
          246895841468826,
          "wpworkforce",
          "elite.wordpressdeveloperandwebprojects",
          1049597849079072,
          "topwordpressexperts",
          "bdwebhostingco",
          327748254580928,
          "cnethost",
          "bestwhs",
          "freedomainandhosting",
          1740781352905908,
          5918218401609609,
          149762078896835,
          948204758974160,
          178390283610486,
          "WebHostingExperts",
          363596310408939,
          270813953903246,
          208616943612768,
          912987732163633,
          368565350291277,
          488501434970507,
          842230342487962,
          "webhostingproviders",
          "ben10host",
          "WebHostiing",
          235395126611168,
          614515998708092,
          ]
temp = [948204758974160]

image_path = r"C:\Users\apost\OneDrive\Desktop\company\media\smal posts\5"
text = "Find Your Perfect Package and Get Started Now at https://www.fandomhost.com \n \n \n#fandomhost #webhosting #wordpresshosting #woocommercehosting"

def delay(start, stop):
    time.sleep(random.randrange(start, stop))

time.sleep(1)
pyautogui.hotkey("alt", "tab")
delay(2, 3)
pyautogui.hotkey("ctrl", "t")

for index, uid in enumerate(temp):
    link = "https://www.facebook.com/groups/" + str(uid)

    try:
        if index == 15:
            time.sleep(10800)
            pyautogui.press("f6")

        delay(1, 2)
        pyautogui.typewrite(link, interval=0.1)
        pyautogui.press("enter")

        delay(10, 12)
        post_aria = pyautogui.locateCenterOnScreen(r"fb_group_poster\posting.PNG", confidence=.5)
        if post_aria is None:
            raise LookupError
        pyautogui.click(post_aria)

        delay(3, 4)
        pyautogui.typewrite(text, interval=0.2)

        delay(3, 4)
        img_btn = pyautogui.locateCenterOnScreen(r"fb_group_poster\post_image.PNG", confidence=.5)
        pyautogui.click(img_btn)

        delay(2, 3)
        img_aria = pyautogui.locateCenterOnScreen(r"fb_group_poster\upload_image_video_section.png", confidence=.5)
        if img_aria is not None:
            pyautogui.click(img_aria)
            delay(3, 4)

        pyautogui.press("f6")
        delay(1, 2)
        pyautogui.typewrite(image_path, interval=0.1) 
        delay(1, 2)
        pyautogui.press("enter")

        delay(2, 3)
        post_btn = pyautogui.locateCenterOnScreen(r"fb_group_poster\post_btn.PNG", confidence=.5)
        #pyautogui.click(post_btn)

        delay(10, 12)
        pyautogui.press("f6")

    except LookupError:
        print(uid)
