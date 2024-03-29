# coding: UTF-8
import tkinter as tk
import webbrowser
import platform
import os
from tkinter import messagebox
import subprocess

#########
# SETUP
#########
if not os.name == 'nt':messagebox.showinfo('Attention','Windows以外のOSでの実行は想定されていません。エラーが発生しても自己責任でお願いします。')

APPNAME = "Fxxk-au-KDDI-Apps"
VERSION = "1.3"
DEVELOPER = "wakanameko2"

APPSID = [
    '''com.kddi.selfcare.external''',
    '''com.kddi.android.email''',
    '''com.kddi.android.emailprov''',
    '''com.kddi.android.imp''',
    '''com.kddi.cs.app001''',
    '''com.kddi.ar.satch.satchviewer''',
    '''com.sonymobile.simlock.kddiremotesimlock''',
    '''com.kddi.android.easysettingwizard''',
    '''com.kddi.ux.station''',
    '''com.kddi.android.ausharelink''',
    '''com.kddi.android.auhomelauncher''',
    '''com.kddi.android.klop''',
    '''com.kddi.android.cmail''',
    '''com.kddi.android.extract''',
    '''com.kddi.auoneshopping''',
    '''com.kddi.android.auoneidsetting''',
    '''com.kddi.market''',
    '''com.kddi.android.au_wifi_connect2''',
    '''com.kddi.android.aumanagementsystem''',
    '''com.kddi.disasterapp''',
    '''com.kddi.android.au_setting_menu''',
    '''com.kddi.android.checker_android''',
    '''com.kddi.android.smartpass''',
    '''com.kddi.android.packageinstaller''',
    '''com.kddi.extcontroldevice''',
    '''com.sonymobile.kddi.settings''',
    '''com.kddi.android.UtaPass''',
    '''com.kddi.android.btdun''',
    '''com.kddi.pass.launcher''',
    '''com.kddi.selfcare.client''',
    '''com.kddi.datacharge''',
    '''com.kddi.android.mamoru''',
    '''com.kddi.android.newspass''',
    '''com.kddi.android.videopass''',
    '''com.kddi.android.lismobookstore''',
    '''com.kddi.android.auworldservice''',
    '''com.kddi.android.repairreceipt''',
    '''com.kddi.android.antijaywalk''',
    '''web.wm.auone.jp''',
    '''com.uievolution.gguide.android''',
]
APPSID_SAIFU =[
    '''jp.auone.wallet''',
    '''com.sonyericsson.felicalock.kddi''',
]

i = 0

print(len(APPSID), len(APPSID_SAIFU))
print(APPNAME + " ver." + str(VERSION))
print('Developer @wakanameko2')

ur = platform.uname()
print(ur.system + '\n' + ur.release + '\n' + ur.version + '\n' + ur.processor)

if (ur.release == 'xp') or (ur.release == '2000') or (ur.release == 'me') or (ur.release == '98') or (ur.release == '95'):messagebox.showerror('Attention','このバージョンのWindowsは対応していません。')

#########
# setup main window
#########
baseGround = tk.Tk()

if (ur.release == 'vista') or (ur.release == '7') or (ur.release == '8') or (ur.release == '8.1') or (ur.release == '2012ServerR2'):
    baseGround.geometry('600x75')
    print('built a window for windows VISTA ~ 2012ServerR2')
elif ur.release == '10':
    #Windows11
    if ur.version >= '10.0.22000':baseGround.geometry('575x70')
    #Windows10
    else:baseGround.geometry('525x60')

baseGround.title(APPNAME + " | " + "ver" + VERSION + " | by " + DEVELOPER)

baseGround.resizable(width = False, height = False)

data = '''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'''
baseGround.tk.call('wm', 'iconphoto', baseGround._w, tk.PhotoImage(data=data))

#########
# core
#########
def running(option):
    label1 = tk.Label(baseGround, text='処理を実行中 (' + option + ')').place(x=290,y=15)
    if (option == "uninstall") or (option =="disable"):
        osaifuProtect = messagebox.askyesno('確認','おサイフケータイ機能を残しますか？')
    elif (option == "install") or (option == "enable"):
        for i in range(0, len(APPSID_SAIFU)):
            osaifuProtect = True
            if option == "install":
                subprocess.call('''adb shell cmd package install-existing ''' + APPSID_SAIFU[i])
            elif option == "enable":
                subprocess.call('''adb shell pm enable --user 0 ''' + APPSID_SAIFU[i])
    
    for i in range(0, len(APPSID)):
        if option == "uninstall":
            subprocess.call('''adb shell pm uninstall -k --user 0 ''' + APPSID[i])
        elif option == "install":
            subprocess.call('''adb shell cmd package install-existing ''' + APPSID[i])
        elif option == "disable":
            subprocess.call('''adb shell pm disable-user --user 0 ''' + APPSID[i])
        elif option == "enable":
            subprocess.call('''adb shell pm enable --user 0 ''' + APPSID[i])

    if osaifuProtect == False:
        for i in range(0, len(APPSID_SAIFU)):
            if option == "uninstall":
                subprocess.call('''adb shell pm uninstall -k --user 0 ''' + APPSID_SAIFU[i])
            elif option == "disable":
                subprocess.call('''adb shell pm disable-user --user 0 ''' + APPSID_SAIFU[i])
    else:
        pass

    print('All done')
    label1 = tk.Label(baseGround, text='All Done                           ').place(x=290,y=15)
    return True

def btn_click_adb():
    webbrowser.open('https://dl.google.com/android/repository/platform-tools_r33.0.1-darwin.zip')

if (ur.release == 'vista') or (ur.release == '7'):label1 = tk.Label(baseGround, text='このソフトフェアを使用するにはADBが必要です。').place(x=253,y=48)
elif (ur.release ==  '8') or (ur.release == '8.1') or (ur.release == '2012ServserR2'):label1 = tk.Label(baseGround, text='このソフトフェアを使用するにはADBが必要です。').place(x=290,y=48)
elif ur.release == '10':
    #Windows11
    if ur.version >= '10.0.22000':label1 = tk.Label(baseGround, text='このソフトフェアを使用するにはADBが必要です。').place(x=270,y=43)
    #Windows10
    else:label1 = tk.Label(baseGround, text='このソフトフェアを使用するにはADBが必要です。').place(x=225,y=36)

if (ur.release == 'vista') or (ur.release == '7'):
    button_adb = tk.Button(baseGround, text='Download', command=btn_click_adb).place(x= 530, y=41)
elif (ur.release == '8') or (ur.release == '8.1') or (ur.release == '2012ServserR2'):
    button_adb = tk.Button(baseGround, text='Download', command=btn_click_adb).place(x= 525, y=43)
elif ur.release == '10':
    #Windows11
    if ur.version >= '10.0.22000':button_adb = tk.Button(baseGround, text='Download', command=btn_click_adb).place(x= 500, y=40)
    #Windows10
    else:button_adb = tk.Button(baseGround, text='Download', command=btn_click_adb).place(x= 450, y=30)

button = tk.Button(
    baseGround, text='Uninstall', command = lambda:running("uninstall")).place(x= 10, y=10)
button2 = tk.Button(
    baseGround, text='Install', command = lambda:running("install")).place(x= 90, y=10)
button3 = tk.Button(
    baseGround, text='Disable', command = lambda:running("disable")).place(x= 155, y=10)
button4 = tk.Button(
    baseGround, text='Enable', command = lambda:running("enable")).place(x= 225, y=10)

baseGround.mainloop()