import pyautogui
import sys
import PIL
#cmousepos = list(pyautogui.position())
#print (cmousepos)
print('Press Ctrl-C to quit.')

#debitornummern.replace("|",",")
#print (debitornummern)
def clicker():
    #vtext = pyautogui.locateCenterOnScreen('Veroeffentlichungstextev2.png')
    #vtextxy = (vtext[0],vtext[1])
    #print (vtextxy)
    pyautogui.click(1047,448,clicks=1,button="left")
        
#    fenster = pyautogui.locateCenterOnScreen("fensterveroeffentlichungstext.png")
#    fensterxy = (fenster[0],fenster[1])
#    print (fensterxy)
#    pyautogui.click(fenster[0],fenster[1],clicks=1,button="left")
#    fensterc()

#    beschreibung = pyautogui.locateCenterOnScreen("beschreibungv2.png")
#    beschreibungxy = (beschreibung[0],beschreibung[1])
#    print (beschreibungxy)
#    pyautogui.click(beschreibungxy,clicks=1,button="left")

if __name__ == "__main__":
    clicker()
