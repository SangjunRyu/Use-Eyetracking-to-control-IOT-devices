"""
Demonstration of the GazeTracking library.
Check the README.md for complete documentation.
"""
import subprocess
import cv2
from gaze_tracking import GazeTracking
import pyautogui
import time
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
import playsound
import os
from gtts import gTTS
import threading
import socket

#exp = " "          # global variable 
# showing all data in display 
exp = ''
lang = 'ko'
abs_path = 'C:\\Users\\ysjun5656\\Desktop\\eyetracking model\\Eyeverything\\GazeTracking\\TTS'

# 클라이언트 설정
HOST = '192.168.118.137'  # 라즈베리 파이의 IP 주소
PORT = 12347  # 서버와 동일한 포트 번호

# client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client_socket.connect((HOST, PORT))

# message = input("전송할 명령 입력: ")
# client_socket.send(message.encode())

def speak(exp):
    global lang
    global abs_path

    file = exp + f'.mp3'
    mp3_path = os.path.join(abs_path, file)  # 파일저장경로
    # sp = gTTS(lang=lang, text = exp, slow = False)
    # sp.save(mp3_path)
    print(mp3_path)
    playsound.playsound(mp3_path)

def press(num):
    global exp
    exp = ''
    exp=exp + str(num)
    equation.set(exp)
    thread = threading.Thread(target = speak, args=(exp,))
    thread.start()
    if exp == '서큘레이터 전원':
        message="10"
        client_socket.send(message.encode())

def clear():
    global exp
    exp = " "
    equation.set(exp)

def action():
  exp = " Next Line : "
  equation.set(exp)

def Tab():
  exp = " TAB : "
  equation.set(exp)

def Ini():
	#key.configure(bg = 'white')    #  add background color

	# 키보드 입력칸
	Dis_entry = ttk.Entry(key,state= 'readonly',textvariable = equation)
	Dis_entry.grid(row= 0 , column = 0, columnspan = 2, padx = 0 , pady = 0, ipadx = 100, ipady=10)
	# end entry box

	# add all button line wise 

	TV = ttk.Button(key,text = 'TV 전원', width = 6, style='my.TButton',command = lambda : press('TV 전원'))
	TV.grid(row = 1 , column = 0 , columnspan = 2, padx = 0, pady = 0, ipadx = 142 , ipady = 80)

	Aircon = ttk.Button(key,text = '에어컨 전원', style='my.TButton' , width = 6, command = lambda : press('에어컨 전원'))
	Aircon.grid(row = 1 , column = 2 , columnspan = 2, padx = 0, pady = 0, ipadx = 142 , ipady = 80)

	Aircleaner = ttk.Button(key,text = '서큘레이터 전원' , style='my.TButton', width = 6, command = lambda : press('서큘레이터 전원'))
	Aircleaner.grid(row = 1 , column = 4 , columnspan = 2, padx = 0, pady = 0, ipadx = 142, ipady = 80)

	emergency = ttk.Button(key,text = '비상 호출' , style='my.TButton', width = 6, command = lambda : press('비상 호출'))
	emergency.grid(row = 1 , column = 6 , columnspan = 2, padx = 0, pady = 0, ipadx = 142, ipady = 80)

	TTS = ttk.Button(key,text = '문장 음성 출력' , style='my.TButton', width = 6, command = lambda : press('문장 음성 출력'))
	TTS.grid(row = 1 , column = 8 , columnspan = 2, padx = 0, pady = 0, ipadx = 142, ipady = 80)


	TV1 = ttk.Button(key,text = '호흡이 불편해요', style='my.TButton' , width = 6, command = lambda : press('호흡이 불편해요'))
	TV1.grid(row = 2 , column = 0 , columnspan = 2, padx = 0, pady = 0, ipadx = 142, ipady = 80)

	Aircon1 = ttk.Button(key,text = '자세가 불편해요' , style='my.TButton',width = 6, command = lambda : press('자세가 불편해요'))
	Aircon1.grid(row = 2 , column = 2 , columnspan = 2, padx = 0, pady = 0, ipadx = 142, ipady = 80)

	Aircleaner1 = ttk.Button(key,text = '대변이 급해요' , style='my.TButton', width = 6, command = lambda : press('대변이 급해요'))
	Aircleaner1.grid(row = 2 , column = 4 , columnspan = 2, padx = 0, pady = 0, ipadx = 142, ipady = 80)

	emergency1 = ttk.Button(key,text = '소변이 급해요' , style='my.TButton', width = 6, command = lambda : press('소변이 급해요'))
	emergency1.grid(row = 2 , column = 6 , columnspan = 2, padx = 0, pady = 0, ipadx = 142, ipady = 80)

	TTS1 = ttk.Button(key,text = '목이 말라요' , style='my.TButton', width = 6, command = lambda : press('목이 말라요'))
	TTS1.grid(row = 2 , column = 8 , columnspan = 2, padx = 0, pady = 0, ipadx = 142, ipady = 80)

	

	TTS1 = ttk.Button(key,text = '몸이 가려워요' , style='my.TButton', width = 6, command = lambda : press('몸이 가려워요'))
	TTS1.grid(row = 3 , column = 0 , columnspan = 2, padx = 0, pady = 0, ipadx = 142, ipady = 80)

	Aircon1 = ttk.Button(key,text = '배가 고파요' , style='my.TButton',width = 6, command = lambda : press('배가 고파요'))
	Aircon1.grid(row = 3 , column = 2 , columnspan = 2, padx = 0, pady = 0, ipadx = 142, ipady = 80)

	Aircleaner1 = ttk.Button(key,text = '열이 나요' , style='my.TButton', width = 6, command = lambda : press('열이 나요'))
	Aircleaner1.grid(row = 3 , column = 4 , columnspan = 2, padx = 0, pady = 0, ipadx = 142, ipady = 80)

	emergency1 = ttk.Button(key,text = '배가 아파요' , style='my.TButton', width = 6, command = lambda : press('배가 아파요'))
	emergency1.grid(row = 3 , column = 6 , columnspan = 2, padx = 0, pady = 0, ipadx = 142, ipady = 80)

	TTS1 = ttk.Button(key,text = '가래를 뽑아주세요' , style='my.TButton', width = 6, command = lambda : press('가래를 뽑아주세요'))
	TTS1.grid(row = 3 , column = 8 , columnspan = 2, padx = 0, pady = 0, ipadx = 142, ipady = 80)


	q = ttk.Button(key,text = 'ㅂ' , style='my.TButton',width = 6, command = lambda : press('ㅂ'))
	q.grid(row = 4 , column = 0 , padx = 0, pady = 0, ipadx = 45, ipady = 40)

	w = ttk.Button(key,text = 'ㅈ' , style='my.TButton', width = 6, command = lambda : press('ㅈ'))
	w.grid(row = 4 , column = 1 , padx = 0, pady = 0, ipadx = 45, ipady = 40)

	e = ttk.Button(key,text = 'ㄷ' , style='my.TButton', width = 6, command = lambda : press('ㄷ'))
	e.grid(row = 4 , column = 2 , padx = 0, pady = 0, ipadx = 45, ipady = 40)

	r = ttk.Button(key,text = 'ㄱ' , style='my.TButton', width = 6, command = lambda : press('ㄱ'))
	r.grid(row = 4 , column = 3 , padx = 0, pady = 0, ipadx = 45, ipady = 40)

	t = ttk.Button(key,text = 'ㅅ' , style='my.TButton', width = 6, command = lambda : press('ㅅ'))
	t.grid(row = 4 , column = 4 , padx = 0, pady = 0, ipadx = 45, ipady = 40)

	y = ttk.Button(key,text = 'ㅛ' , style='my.TButton', width = 6, command = lambda : press('ㅛ'))
	y.grid(row = 4 , column = 5 , padx = 0, pady = 0, ipadx = 45, ipady = 40)

	u = ttk.Button(key,text = 'ㅕ' , style='my.TButton', width = 6, command = lambda : press('ㅕ'))
	u.grid(row = 4 , column = 6 , padx = 0, pady = 0, ipadx = 45, ipady = 40)

	i = ttk.Button(key,text = 'ㅑ' , style='my.TButton', width = 6, command = lambda : press('ㅑ'))
	i.grid(row = 4 , column = 7 , padx = 0, pady = 0, ipadx = 45, ipady = 40)

	o = ttk.Button(key,text = 'ㅐ' , style='my.TButton', width = 6, command = lambda : press('ㅐ'))
	o.grid(row = 4 , column = 8 , padx = 0, pady = 0, ipadx = 45, ipady = 40)

	p = ttk.Button(key,text = 'ㅔ' , style='my.TButton', width = 6, command = lambda : press('ㅔ'))
	p.grid(row = 4 , column = 9 , padx = 0, pady = 0, ipadx = 45, ipady = 40)




	a = ttk.Button(key,text = 'ㅁ' , style='my.TButton', width = 6, command = lambda : press('ㅁ'))
	a.grid(row = 5 , column = 0 , padx = 0, pady = 0, ipadx = 45, ipady = 40)

	s = ttk.Button(key,text = 'ㄴ' , style='my.TButton', width = 6, command = lambda : press('ㄴ'))
	s.grid(row = 5 , column = 1 , padx = 0, pady = 0, ipadx = 45, ipady = 40)

	d = ttk.Button(key,text = 'ㅇ' , style='my.TButton', width = 6, command = lambda : press('ㅇ'))
	d.grid(row = 5 , column = 2 , padx = 0, pady = 0, ipadx = 45, ipady = 40)

	f = ttk.Button(key,text = 'ㄹ' , style='my.TButton', width = 6, command = lambda : press('ㄹ'))
	f.grid(row = 5 , column = 3 , padx = 0, pady = 0, ipadx = 45, ipady = 40)

	g = ttk.Button(key,text = 'ㅎ' , style='my.TButton', width = 6, command = lambda : press('ㅎ'))
	g.grid(row = 5 , column = 4 , padx = 0, pady = 0, ipadx = 45, ipady = 40)

	h = ttk.Button(key,text = 'ㅗ' , style='my.TButton', width = 6, command = lambda : press('ㅗ'))
	h.grid(row = 5 , column = 5 , padx = 0, pady = 0, ipadx = 45, ipady = 40)

	j = ttk.Button(key,text = 'ㅓ' , style='my.TButton', width = 6, command = lambda : press('ㅓ'))
	j.grid(row = 5 , column = 6 , padx = 0, pady = 0, ipadx = 45, ipady = 40)

	k = ttk.Button(key,text = 'ㅏ' , style='my.TButton', width = 6, command = lambda : press('ㅏ'))
	k.grid(row = 5 , column = 7 , padx = 0, pady = 0, ipadx = 45, ipady = 40)

	l = ttk.Button(key,text = 'ㅣ' , style='my.TButton', width = 6, command = lambda : press('ㅣ'))
	l.grid(row = 5 , column = 8 , padx = 0, pady = 0, ipadx = 45, ipady = 40)

	enter = ttk.Button(key,text = 'Enter' , style='my.TButton', width = 6, command = lambda : press('Enter'))
	enter.grid(row = 5 , column = 9 , padx = 0, pady = 0, ipadx = 45, ipady = 40)


	shift = ttk.Button(key,text = 'Shift' , style='my.TButton', width = 6, command = lambda : press('Shift'))
	shift.grid(row = 6 , column = 0 , padx = 0, pady = 0, ipadx = 45, ipady = 40)

	z = ttk.Button(key,text = 'ㅋ' , style='my.TButton', width = 6, command = lambda : press('ㅋ'))
	z.grid(row = 6 , column = 1 , padx = 0, pady = 0, ipadx = 45, ipady = 40)

	x = ttk.Button(key,text = 'ㅌ' , style='my.TButton', width = 6, command = lambda : press('ㅌ'))
	x.grid(row = 6 , column = 2 , padx = 0, pady = 0, ipadx = 45, ipady = 40)

	c = ttk.Button(key,text = 'ㅊ' , style='my.TButton', width = 6, command = lambda : press('ㅊ'))
	c.grid(row = 6 , column = 3 , padx = 0, pady = 0, ipadx = 45, ipady = 40)

	v = ttk.Button(key,text = 'ㅍ' , style='my.TButton', width = 6, command = lambda : press('ㅍ'))
	v.grid(row = 6 , column = 4 , padx = 0, pady = 0, ipadx = 45, ipady = 40)

	b = ttk.Button(key,text = 'ㅠ' , style='my.TButton', width = 6, command = lambda : press('ㅠ'))
	b.grid(row = 6 , column = 5 , padx = 0, pady = 0, ipadx = 45, ipady = 40)

	n = ttk.Button(key,text = 'ㅜ' , style='my.TButton', width = 6, command = lambda : press('ㅜ'))
	n.grid(row = 6 , column = 6 , padx = 0, pady = 0, ipadx = 45, ipady = 40)

	m = ttk.Button(key,text = 'ㅡ' , style='my.TButton', width = 6, command = lambda : press('ㅡ'))
	m.grid(row = 6 , column = 7 , padx = 0, pady = 0, ipadx = 45, ipady = 40)

	space = ttk.Button(key,text = 'Space' , style='my.TButton', width = 6, command = lambda : press(' '))
	space.grid(row = 6 , column = 8 , padx = 0, pady = 0, ipadx = 45, ipady = 40)

	Backspace = ttk.Button(key,text = 'Backpace' , style='my.TButton', width = 6, command = lambda : press('Backspace'))
	Backspace.grid(row = 6 , column = 9 , padx = 0, pady = 0, ipadx = 45, ipady = 40)

start_time = time.time()
end_time = time.time()
btn_click = False

# FAILSAFE 모드를 비활성화
pyautogui.FAILSAFE = False

# OpenCV로 카메라 열기
cap = cv2.VideoCapture(0)
gaze = GazeTracking()

def update_frame():
    global start_time
    global end_time
    global btn_click
    # 카메라에서 프레임 읽기
    ret, frame = cap.read()

    if ret:
        frame = cv2.flip(frame,1)
        text = ""
        gaze.refresh(frame)
        frame = gaze.annotated_frame()
        frame = frame[190:230,150:490]

        if gaze.is_blinking():
            text = "Blinking"
            if not btn_click:     
                start_time = time.time()
                end_time = time.time()
                btn_click = True
        elif gaze.is_right():
            text = "Looking right"
        elif gaze.is_left():
            text = "Looking left"
        elif gaze.is_center():
            text = "Looking center"
        # else:
        #     text = "else"

        cv2.putText(frame, text, (0, 30), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 255, 255), 2)

        if not (gaze.is_blinking()):
            left_pupil = gaze.pupil_left_coords()
            right_pupil = gaze.pupil_right_coords()
            cv2.putText(frame, "Left pupil:  " + str(left_pupil), (90, 130), cv2.FONT_HERSHEY_DUPLEX, 0.9, (255,255,255), 1)
            cv2.putText(frame, "Right pupil: " + str(right_pupil), (90, 165), cv2.FONT_HERSHEY_DUPLEX, 0.9, (255,255,255), 1)
        else:
            left_pupil = None
            right_pupil = None
        cv2.ellipse(frame, (95,20), (35,15), 0, 0, 360, (0,0,255))
        cv2.ellipse(frame, (245,20), (35,15), 0, 0, 360, (0,0,255))

        #Moving mouse
        if left_pupil is not None:
            left = tuple(x-y for x,y in  zip(left_pupil , (245, 210))) 
            left_move = tuple(100*x+y for x,y in zip(left, (960,540)))
            right = tuple(x-y for x,y in  zip(right_pupil , (395, 210)))
            right_move = tuple(100*x+y for x,y in zip(right, (960,540)))

            mouse = tuple(x/2 for x in (left_move + right_move))
            pyautogui.moveTo(mouse)
        
        if gaze.is_blinking():
            end_time = time.time()
            print("time diff: ", end_time - start_time)
            if end_time-start_time>1.75:
                print("click")
                pyautogui.click()
                btn_click = False
        else:
            btn_click = False

        #if cv2.waitKey(1) == 27:
            
        # OpenCV 프레임을 Pillow 이미지로 변환
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame_rgb)

        # Pillow 이미지를 Tkinter PhotoImage로 변환
        img_tk = ImageTk.PhotoImage(image=img)

        # Label에 이미지 업데이트
        label.img = img_tk
        label.config(image=img_tk)

    # 계속해서 프레임 업데이트
    label.after(10, update_frame)

if __name__ == "__main__":

    # Tkinter 창 설정
    key = tk.Tk()
    key.title("Keyboard by EYEVRYTHING")
    key.attributes('-fullscreen',True)  # fullscreen

    #Size window size
    key.geometry('940x250')         # normal size
    key.maxsize(width=2000, height=1000)      # maximum size
    key.minsize(width= 800 , height = 1000)     # minimum size
    # end window size

    style = ttk.Style()
    style.configure('my.TButton', font=('Helvetica',20))

    # 이미지를 표시할 Label 생성
    label = ttk.Label(key)
    #label.pack()
    label.grid(row =0, column = 4, columnspan = 2, ipady=30)

    equation = tk.StringVar()
    Ini()

    # 프레임 업데이트 시작
    update_frame()

    # Tkinter 창 실행
    key.mainloop()

    # 카메라 해제
    cap.release()
