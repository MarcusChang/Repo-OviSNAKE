from pywinauto import application
from pywinauto.controls.common_controls import ToolbarWrapper,ListViewWrapper
import time
import win32con,win32api,win32gui,win32process
import winGuiAuto
from winGuiAuto import WinGuiAutoError
import re
from PIL import ImageGrab
import threading

class mythread(threading.Thread):
    def run(self):
        runSikuli()
        
def runSikuli():
    try:
        app = application.Application.start('D:\\Sikuli\\Sikuli-IDE.exe')
    except application.AppStartError:
        print "The specified path of Sikuli-IDE is not found, pls. check it again!!"
        exit()
    time.sleep(3)
    app3 = app.window_(title_re = '.*Sikuli*')
    app3.TypeKeys('^o')
    open=app.window_(title_re = '.*Open.*')
    time.sleep(1)
    open.TypeKeys('C:\\MOS\\res.sikuli')   #Point out to your sikuli reserve folder
    time.sleep(1)
    open.TypeKeys('{ENTER}')
    time.sleep(1)
    app3.TypeKeys('^r')
    t = True
    while t == True:
        try:
            pids = win32pdhutil.FindPerformanceAttributesByName('Sikuli-IDE')   #monitor the Sikuli process
            if pids == []:               #to jugde if the Sikuli is terminated
                t = False
        except:                          #there will be a Exception throwed out, so put an except handling section here
            t = False

try:
    app = application.Application.start('C:\\Documents and Settings\\marcuschang\\Desktop\\MOS WORK\\OviMiddleWare.exe')
except application.AppStartError:
    print "The specified applicaiton 'OviMiddleWare.exe' path is not found, pls. check !"
    exit()
app1 = app.window_(title_re = '.*OviMiddleWare.*')
app1.Maximize()
time.sleep(1)
T = 'C:\\Rendering_BAT_auto.txt'

#app1.print_control_identifiers()
#Init WXTEST
def initMMO():    #define the "MapModel Online" button's initialization check formula
    if (app1.CheckBox2.GetCheckState()==1):
        app1.CheckBox2.Click()
    
def initSP():    #define the "Show Prefix" button's initialization check formula
    if (app1.CheckBox.GetCheckState()==1):
        app1.CheckBox.Click()
    
def initEX3DM():    #define the "3D Map" button's initialization check formula
    if (app1.CheckBox6.GetCheckState()==1):
        app1.CheckBox6.Click()  

def initEX3DL():    #define the "3D Landmarks" button's initialization check formula
    if (app1.CheckBox7.GetCheckState()==1):
        app1.CheckBox7.Click() 

def initEXCH():    #define the "Crosshair" button's initialization check formula
    if (app1.CheckBox8.GetCheckState()==1):
        app1.CheckBox8.Click()

def initEXTZ():    #define the "TimeZones" button's initialization check formula
    if (app1.CheckBox9.GetCheckState()==1):
        app1.CheckBox9.Click()

def initEXSL():    #define the "Street Lines" button's initialization check formula
    if (app1.CheckBox10.GetCheckState()==1):
        app1.CheckBox10.Click()

def initEXBL():    #define the "Blocking" button's initialization check formula
    if (app1.CheckBox11.GetCheckState()==1):
        app1.CheckBox11.Click()

def initEXMM():    #define the "Mini Map" button's initialization check formula
    if (app1.CheckBox12.GetCheckState()==1):
        app1.CheckBox12.Click()


oviMdWare=winGuiAuto.findTopWindow(wantedText='OviMiddleWare', wantedClass=None, selectionFunction=None)
toolbar=winGuiAuto.findControl(oviMdWare,wantedClass="ToolbarWindow32")
tlw = ToolbarWrapper(toolbar)
tlw.PressButton(0)


time.sleep(1)

app2 = app.window_(title_re = '.*Choose a file.*')

app2.TypeKeys('world_00.02.41.121.cdt')
#app2.TypeKeys('world_00.40.114.cdt')
time.sleep(1)
app2.TypeKeys('{ENTER}')

time.sleep(1)

try:
    f = open (T, 'r')
except IOError:
    print "The specified file: C:\\Rendering_BAT_auto.txt is not found, pls. check!!"
    exit()


for line in f.readlines()[1: ]:
    try:
        initMMO()     #initialization
        initSP()      #initialization
        initEX3DM()   #initialization
        initEX3DL()   #initialization
        initEXCH()    #initialization
        initEXTZ()    #initialization
        initEXSL()    #initialization
        initEXBL()    #initialization
        initEXMM()    #initialization
    except:
        print "The controls are not properly be initiated, pls. check your map data file."
        exit()
    
    Long = line.split('\t')[1]
    app1.Edit.DoubleClick()
    app1.TypeKeys(Long)
    app1.TypeKeys('{ENTER}')
    time.sleep(1)

    Lat = line.split('\t')[2]
    app1.Edit2.DoubleClick()
    app1.TypeKeys(Lat)
    app1.TypeKeys('{ENTER}')
    time.sleep(1)

    CS = line.split('\t')[3]
    app1.ComboBox0.Select(CS)
    time.sleep(1)

    CT = line.split('\t')[4]
    app1.ComboBox2.Select(CT)
    time.sleep(1)

    MMO = line.split('\t')[5]
    if (MMO == 'Check'):
        app1.CheckBox2.Click()

    time.sleep(1)
    
    DP = line.split('\t')[6]
    app1.Edit8.SetEditText(DP)
    app1.Edit8.Click()
    app1.TypeKeys('{ENTER}')
    time.sleep(1)


    ZF = int(line.split('\t')[7])
    app1.Trackbar2.Click()
    for z in range(0, ZF/9):      #The trackbar process for 9 unit when type 'Page-down' key once
        app1.TypeKeys('{PGUP}')
    for z in range(0, ZF%9):
        app1.TypeKeys('{UP}')

    time.sleep(1)


    RO = int(line.split('\t')[8])
    app1.Trackbar1.Click()
    for r in range(0, RO/36):     #The trackbar process for 36 unit when type 'Page-down' key once
        app1.TypeKeys('{PGDN}')
    for r in range(0, RO%36):
        app1.TypeKeys('{DOWN}')

    time.sleep(1)

    MARC = line.split('\t')[9]
    app1.Edit11.SetEditText(MARC)
    app1.Edit11.Click()
    app1.TypeKeys('{ENTER}')
    time.sleep(2)

    SP = line.split('\t')[10]
    if (SP == 'Check' ):
        app1.CheckBox.Click()
    time.sleep(1)

    W3DM = line.split('\t')[11]
    if (W3DM == 'Check'):
        app1.CheckBox6.Click()
    time.sleep(1)

    W3DL = line.split('\t')[12]
    if (W3DL == 'Check'):
        app1.CheckBox7.Click()
    time.sleep(1)

    Cros = line.split('\t')[13]
    if (Cros == 'Check'):
        app1.CheckBox8.Click()
    time.sleep(1)

    Block = line.split('\t')[14]
    if (Block == 'Check'):
        app1.CheckBox11.Click()
    time.sleep(1)

    MMM = line.split('\t')[15]
    if (MMM == 'Check'):
        app1.CheckBox12.Click()
    time.sleep(1)

    im = ImageGrab.grab()

    p = line.split("\t")[16].split("\\")[3].split(".")[0]
    
    im.save(('C:\\MOS\\actualIMG\\') + (p) + ('.png'))

    time.sleep(1)

    Test_Name = line.split('\t')[0]
    Pic = line.split('\t')[16]
    

    tempFile='C:\\MOS\\config\\formatData.txt'
    try:
        tr=open(tempFile, 'w')
    except IOError:
        print "The specified file: C:\\MOS\config\\formatData.txt, pls. check!!"
        exit()
    tr.write(line.split('\t')[0])
    tr.write('\n')
    tr.write(line.split('\t')[1])
    tr.write('\n')
    tr.write(line.split('\t')[2])
    tr.write('\n')
    tr.write(line.split('\t')[16])
    tr.write('\n')
    tr.close()
    
    t1 = mythread()
    t1.start()
    time.sleep(1)
    t1.join()
    time.sleep(1)


    app1.Trackbar1.Click()      #initialization for the Trackbar1
    app1.TypeKeys('{HOME}')     #initialization for the Trackbar1

    time.sleep(1)

f.close()
    
 
