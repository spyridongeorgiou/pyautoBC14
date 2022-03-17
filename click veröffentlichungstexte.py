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

#debitornummern =  "10357|10459|(10465|10514)|(10551|10555|(10590|10715))|(10718|10735|(10747|10768)|(10769|10770|(10771|10780)))|(10781|10951|(10953|10954)|(10955|10959|(10961|10964))|(10965|10971|(10972|10978)|(10980|10981|(10983|10984))))|(10985|10986|(10988|10989)|(10993|10994|(10997|10998))|(11000|11003|(11004|11005)|(11006|11008|(11010|11013)))|(11014|11016|(11018|11019)|(11020|11021|(11022|11024))|(11025|11026|(11032|11039)|(11045|11047|(11048|11050)))))|(11054|11056|(11067|11071)|(11075|11079|(11084|11087))|(11090|11095|(11099|11100)|(11107|11108|(11109|11114)))|(11115|11118|(11131|11133)|(11134|11135|(11136|11137))|(11138|11139|(11140|11143)|(11151|11158|(11159|11160))))|(11169|11170|(11171|11172)|(11184|11188|(11191|11194))|(11200|11204|(11205|11206)|(11207|11222|(11223|11224)))|(11225|11233|(11235|11236)|(11241|11242|(11243|11244))|(11245|11246|(11248|11249)|(11250|11251|(11252|11253))))))|(11254|11255|(11256|11257)|(11258|11259|(11260|11261))|(11262|11263|(11264|11265)|(11266|11267|(11269|11270)))|(11271|11272|(11273|11274)|(11275|11276|(11278|11279))|(11281|11282|(11285|11286)|(11287|11288|(11289|11290))))|(11291|11292|(11293|11294)|(11296|11297|(11298|11300))|(11301|11303|(11304|11305)|(11307|11310|(11311|11312)))|(11313|11314|(11315|11316)|(11317|11319|(11320|11321))|(11322|11323|(11324|11326)|(11327|11328|(11329|11332)))))|(11333|11334|(11335|11336)|(11337|11338|(11340|11341))|(11342|11344|(11345|11347)|(11348|11349|(11350|11351)))|(11354|11355|(11357|11359)|(11360|11361|(11362|11364))|(11365|11366|(11367|11368)|(11369|11370|(11371|11372))))|(11373|11374|(11375|11376)|(11380|11384|(11385|11386))|(11389|11390|(11391|11392)|(11393|11394|(11396|11397)))|(11399|11400|(11401|11403)|(11404|11405|(11410|11411))|(11412|11415|(11416|11418)|(11421|11422|(11425|11427)))))))|(11428|11429|(11430|11431)|(11432|11434|(11435|11438))|(11441|11442|(11444|11445)|(11447|11449|(11450|11451)))|(11452|11453|(11454|11455)|(11456|11457|(11458|11459))|(11460|11461|(11462|11463)|(11464|11465|(11466|11467))))|(11468|11469|(11470|11471)|(11472|11473|(11474|11475))|(11476|11477|(11478|11479)|(11480|11481|(11482|11483)))|(11484|11486|(11487|11489)|(11490|11491|(11492|11493))|(11495|11497|(11499|11522)|(11523|11530|(11582|11595)))))|(11931|11932|(11933|11934)|(11935|11936|(11937|11938))|(11939|11940|(11941|11953)|20000)))"
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