import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk
import signal
import sys
import keyboard

def cleanup():
    # 리소스를 해제하거나 이벤트 핸들러를 언바운드하기 위한 코드를 추가하세요.
    key.destroy()

def handle_ctrl_c(signum, frame):
    cleanup()
    print("ctrl c is called")
    sys.exit(0)

# Ctrl+C 시그널 핸들러 설정
signal.signal(signal.SIGINT, handle_ctrl_c)

key = tk.Tk()  # key window name
key.title('Keyboard By EYEverything')  # title Name


# fontex = tkFont.Font(family="Consolas", size= 17)

#key.attributes('-fullscreen',True)  # fullscreen

# key.iconbitmap('add icon link And Directory name')    # icon add

# function coding start 

exp = " "          # global variable 
# showing all data in display 

def press(num):
    global exp
    exp=exp + str(num)
    equation.set(exp)
# end 


# function clear button

def clear():
    global exp
    exp = " "
    equation.set(exp)

# end 


# Enter Button Work Next line Function

def action():
  exp = " Next Line : "
  equation.set(exp)

# end function coding


# Tab Button Function 


def Tab():
  exp = " TAB : "
  equation.set(exp)

# END Tab Button Fucntion

# Size window size
key.geometry('940x250')         # normal size
key.maxsize(width=2000, height=1000)      # maximum size
key.minsize(width= 800 , height = 1000)     # minimum size
# end window size

key.configure(bg = 'white')    #  add background color

# textEx = tk.Text(key, height=20)
# textEx.configure(font = fontex)


# entry box
equation = tk.StringVar()
Dis_entry = ttk.Entry(key,state= 'readonly',textvariable = equation)
Dis_entry.grid(rowspan= 1 , columnspan = 100, ipadx = 999 , ipady = 10)
# end entry box

TV = ttk.Button(key,text = 'TV 전원' , width = 6, command = lambda : press('TV 전원'))
TV.grid(row = 1 , column = 0 , ipadx = 165 , ipady = 100)

Aircon = ttk.Button(key,text = '에어컨 전원' , width = 6, command = lambda : press('에어컨 전원'))
Aircon.grid(row = 1 , column = 1 , ipadx = 165 , ipady = 100)

Aircleaner = ttk.Button(key,text = '공기청정기 전원' , width = 6, command = lambda : press('공기청정기 전원'))
Aircleaner.grid(row = 1 , column = 2 , ipadx = 165 , ipady = 100)

emergency = ttk.Button(key,text = '비상 호출' , width = 6, command = lambda : press('비상 호출'))
emergency.grid(row = 1 , column = 3 , ipadx = 165 , ipady = 100)

TTS = ttk.Button(key,text = '문장 음성 출력' , width = 6, command = lambda : press('문장 음성 출력'))
TTS.grid(row = 1 , column = 4 , ipadx = 165 , ipady = 100)


TV1 = ttk.Button(key,text = '호흡이 불편해요' , width = 6, command = lambda : press('호흡이 불편해요'))
TV1.grid(row = 2 , column = 0 , ipadx = 165 , ipady = 100)

Aircon1 = ttk.Button(key,text = '자세가 불편해요' , width = 6, command = lambda : press('자세가 불편해요'))
Aircon1.grid(row = 2 , column = 1 , ipadx = 165 , ipady = 100)

Aircleaner1 = ttk.Button(key,text = '대변이 급해요' , width = 6, command = lambda : press('대변이 급해요'))
Aircleaner1.grid(row = 2 , column = 2 , ipadx = 165 , ipady = 100)

emergency1 = ttk.Button(key,text = '소변이 급해요' , width = 6, command = lambda : press('소변이 급해요'))
emergency1.grid(row = 2 , column = 3 , ipadx = 165 , ipady = 100)

TTS1 = ttk.Button(key,text = '목이 말라요' , width = 6, command = lambda : press('목이 말라요'))
TTS1.grid(row = 2 , column = 4 , ipadx = 165 , ipady = 100)

key.mainloop()  # using ending point