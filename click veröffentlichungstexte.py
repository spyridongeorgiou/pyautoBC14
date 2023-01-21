import pyautogui
import sys
import keyboard
import time
import PIL
import win32api, win32con

# cd "C:\Skripts - Python\pyautoguiBC14\..."

wait = time.sleep(0.05) # Warten
confirmbutton = pyautogui.confirm(text='ENTFERNEN VON LASTSCHRIFTEINZUGSTEXTEN IN BC14', title='PYAUTOGUI AUSFÜHREN?', buttons=["OK", "CANCEL"]) # Knopf zum bestätigen ob weiter? OK/CANCEL

def cbutton():
    confirmbutton
    if confirmbutton == "OK":
        pass
    elif confirmbutton == "CANCEL":
        print ("OPERATION CANCELLED")
        return
        #break

#debitornummern.replace("|",",")
#print (debitornummern)

print('Press "Ctrl-C" or "q" to quit.')


def clicker():
    vtexte = pyautogui.locateCenterOnScreen("vtexte.png")
    if vtexte != None:
        print ("Veröffentlichungstext gefunden: ", vtexte)
        pyautogui.click(vtexte,clicks=1, button="left") # Veröffentlichungstexte klicken
        wait
        
    wait
    beschreibung = pyautogui.locateCenterOnScreen("beschreibung.png")
    if beschreibung != None:
        print ("Beschreibung gefunden: ", beschreibung)
        pyautogui.click(beschreibung,clicks=1, button="left") # Beschreibung klicken
        wait
    
    wait
    lstext = pyautogui.locateCenterOnScreen("lstext.png")
    if lstext != None:
        print ("Beschreibung gefunden: ", lstext)
        pyautogui.click(lstext,clicks=1, button="left") # Lastschrifteinzugstext klicken
        wait
        
    wait
    pyautogui.hotkey("ctrl", "del")
    
    wait
    ja = pyautogui.locateCenterOnScreen("jav2.png")
    if ja != None:
        print (" 'Ja' gefunden:", ja)
        pyautogui.click(ja,clicks=1, button="left") # Ja für löschen klicken
        wait
    
    wait
    pyautogui.hotkey("ctrl","enter")
    wait
    
    wait
    pyautogui.press("down")
    return
    

while keyboard.is_pressed("q") == False:
    cbutton()
    if confirmbutton == "CANCEL":
        print ("Q PRESSED")
        break
    wait
    clicker()
    wait
#    jaclicker()
#    wait
