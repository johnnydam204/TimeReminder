# Project: CNC Vina Working Time Reminder 
# Author: duandh@cncvina.com.vn
# Project Leader: thanhdn@cncvina.com.vn
# Target PC: Raspberry Pi 3
# Reminder for: Office Department
# Project Finish: 16:00:00 Tuesday June 20th 2017

import os
from time import sleep
import datetime

# Khai bao bai nhac
# omxplayer -o local => duong am thanh o cong headphone 3.5mm 
PlaySong = ["omxplayer -o local /home/pi/TimeReminder/Audio/TheDucBuoiSang.mp3 &", 
			"omxplayer -o local /home/pi/TimeReminder/Audio/BatDauGioLamViec.wav &",			
			"omxplayer -o local /home/pi/TimeReminder/Audio/BatDauGioNghi.wav &",
			"omxplayer -o local /home/pi/TimeReminder/Audio/KetThucGioNghi.wav &", 
			"omxplayer -o local /home/pi/TimeReminder/Audio/TietKiemDien.wav &",
			"omxplayer -o local /home/pi/TimeReminder/Audio/KetThucGioLamViec.WAV &",
			"omxplayer -o local /home/pi/TimeReminder/Audio/BatDauGioHopDauTuan.WAV &"			
			]

# Khai bao thoi gian chay nhac
HourStart 	= [7,	8, 12, 12, 17, 17, 8 ]
MinuteStart = [55,	0, 0,  55, 0,  9,  58]
SecondStart = [0, 	0, 0,  0,  0,  0,  0 ]

# Khai bao thoi gian dung chay nhac
HourStop 	= [7,  8, 12, 12, 17, 17, 8 ]
MinuteStop 	= [59, 0, 0,  55, 0,  9,  59]
SecondStop 	= [51, 6, 15, 15, 17, 15, 10]

while True:

	# Doc thoi gian
	MyDateTime = datetime.datetime.now()
	
	#Tach thoi gian
	Hour = MyDateTime.hour
	Minute = MyDateTime.minute
	Second = MyDateTime.second
	
	Day = MyDateTime.day   			#Day of month
	Weekday = MyDateTime.weekday()	#Day of week
	Month = MyDateTime.month
	Year = MyDateTime.year
	
	# So sanh voi thoi gian cai dat
	# Nhac chuong hang ngay
	for i in range(0,5):
		if Hour == HourStart[i] and Minute == MinuteStart[i] and Second == SecondStart[i]:
			os.system(PlaySong[i])
		if Hour == HourStop[i] and Minute == MinuteStop[i] and Second == SecondStop[i]:	
			#os.system("omxplayer -i")
			os.system("sudo killall omxplayer.bin &")
			
	# Them nhac chuong hop dau tuan
	if Weekday == 0:
		if Hour == HourStart[6] and Minute == MinuteStart[6] and Second == SecondStart[6]:
			os.system(PlaySong[6])
		if Hour == HourStop[6] and Minute == MinuteStop[6] and Second == SecondStop[6]:	
		#os.system("omxplayer -i")
			os.system("sudo killall omxplayer.bin &")

	#In ra ngay thang nam
	print("Date: %s/%s/%s" % (Day, Month,Year))
	
	# In ra Thu trong tuan
	#print("Weekday: %s" % (Weekday))
	if 		Weekday == 0: print 'Monday'
	elif	Weekday == 1: print 'Tuesday'
	elif	Weekday == 2: print 'Wednesdayday'
	elif	Weekday == 3: print 'Thursday'
	elif	Weekday == 4: print 'Friday'
	elif	Weekday == 5: print 'Saturday'
	elif	Weekday == 6: print 'Sunday'	
	
	# In ra thoi gian
	print("Time: %s:%s:%s" % (Hour, Minute,Second))

	# Delay 1 s
	sleep(1);	
