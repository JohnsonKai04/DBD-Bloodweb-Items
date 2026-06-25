import pyautogui
import time
import os
import keyboard
import ctypes

ctypes.windll.user32.SetProcessDPIAware()

count = 0
presCount = 0
durtaion = time.perf_counter()

def finish():
	duration = time.perf_counter() - durtaion
	print(" ")
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Stats~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	print("  You've gained: ", count, " Specific Items/Addons/Offerings from your list!")
	print("  You've gained: ", presCount, " Prestiges")
	print("  This took ", round(duration), "s")
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

	os._exit(0)

def moveClick(location):
	center = pyautogui.center(location)
	print("moving to: ", center)
	pyautogui.moveTo(center)
	pyautogui.mouseDown()
	time.sleep(0.5)
	pyautogui.mouseUp()
	pyautogui.moveTo(1180, 535)
	time.sleep(0.5)


# Intro
print("Moew meow welcome to Melon's DBD bloodpoint script!")
print("The script will begin in 10 seconds please full screen DBD")
print("Press ESC to exit the script")
time.sleep(11)

keyboard.add_hotkey('esc', finish)

while True:
	with os.scandir(r'.\Icons') as dir:
		i = False
		for f in dir:
			try:
				loc1 = pyautogui.locateOnScreen(f.path, confidence=0.85)
				moveClick(loc1)
				i = True
				count += 1
				time.sleep(1.75)
			except pyautogui.ImageNotFoundException:
				pass

		if i != True:
			try:
				loc = pyautogui.locateOnScreen(r'Bloodwebcenter\autobuy.png', confidence=0.80)
				moveClick(loc)
				time.sleep(5)
				continue
			except pyautogui.ImageNotFoundException:
				pass

			try:
				loc = pyautogui.locateOnScreen(r'Bloodwebcenter\pres.png', confidence=0.60)
				moveClick(loc)
				time.sleep(7)
				continue
			except pyautogui.ImageNotFoundException:
				pass

			try: # Too sleepy this doesnt work though it needs to move the mouse to the continue button
				loc = pyautogui.locateOnScreen(r'Bloodwebcenter\rewardsunlocked.png', confidence=0.60)
				moveClick(loc)
				print("+1 Prestige")
				presCount += 1
				time.sleep(5)
			except pyautogui.ImageNotFoundException:
				print("Warning error occured when finding autobuy.png")
				print("Warning error occured when finding pres.png")
				print("Warning error occured when finding rewardsunlocked.png")
				break
