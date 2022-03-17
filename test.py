import pyautogui
import sys
#cd "C:\Skripts - Python\pyautoguiBC14"
#while True:
#    last = pyautogui.locateCenterOnScreen("lastschrifteinzugv2.png", confidence=0.8)
#    last
#    print (last)
#confirmbutton = pyautogui.confirm(text='Continue?', title='Continue?', buttons=["OK", "CANCEL"]) # Knopf zum bestätigen ob weiter? OK/CANCEL

#while 1:
#    if confirmbutton == "OK":
#        pass
#    elif confirmbutton == "CANCEL":
#        print ("Sadge")
#        break
#    x = 0
#    x = x + 1
#    print (x)
    
    
def cbutton():
    confirmbutton = pyautogui.confirm(text='Continue?', title='Continue?', buttons=["OK", "CANCEL"]) # Knopf zum bestätigen ob weiter? OK/CANCEL
    if confirmbutton == "OK":
        pass
    elif confirmbutton == "CANCEL":
        print ("Sadge")
        return
        #break
    x = 0
    x = x + 1
    print (x)
cbutton()
    #ja = pyautogui.locateCenterOnScreen('jav2.png', confidence=0.99)
    #jaxy = (ja[0],ja[1])
    #print (jaxy)
    
#jaxy = (ja[0],ja[1])
#print (jaxy)