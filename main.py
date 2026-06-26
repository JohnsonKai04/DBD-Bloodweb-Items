# Use python -m PyInstaller --onefile main.py
# To compile

import pyautogui
import time
import os
import keyboard


itemCount = 0
presCount = 0
lvlCount = 0
durtaion = time.perf_counter()
debug = ''
stop_requested = False


def request_stop():
	if debug == True: print("Debug: Stop requested")
	global stop_requested
	stop_requested = True


def finish():
	duration = time.perf_counter() - durtaion
	print(" ")
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Stats~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	print("  You've gained: ", itemCount, " Specific Items/Addons/Offerings from your list!")
	print("  You've gained: ", presCount, " Prestiges and ", lvlCount, " levels")
	print("  This took ", round(duration), "seconds")
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	print(" ")
	input("Press Enter to continue...")
	os._exit(0)


def moveClick(center):
	if debug == True: print("Debug: Moving to: ", center)
	pyautogui.moveTo(center)
	pyautogui.mouseDown()
	time.sleep(0.1)
	pyautogui.mouseUp()
	pyautogui.moveTo(1180, 535)

# Draws box around original image which can be scanned
def retAround(location, padding):
	return (
        max(0, location.left - padding),
        max(0, location.top - padding),
        location.width + padding * 2,
        location.height + padding * 2,
	)

# Intro
print("Moew meow welcome to Melon's DBD bloodpoint script!")
while debug not in (True, False):
	if debug == 'y':
		debug = True
		print("Debug mode True")
	elif debug == 'n':
		debug = False
		print("Debug mode False")
	else:
		debug = input("Would you like to enable debug mode? (y/n): ").lower().strip()

print("The script will begin in 3 seconds please full screen DBD")
print("Press ESC to exit the script")
time.sleep(3)
keyboard.add_hotkey('esc', request_stop)

# Main loop
while True:
	if stop_requested:
		finish()
	with os.scandir(r'.\Icons') as dir:
		i = False
		# Search for Items/Perks/Addons
		for f in dir:
			try:
				loc = pyautogui.locateOnScreen(f.path, confidence=0.60)
				moveClick(loc)
				i = True
				itemCount += 1

				# Attempts to find completed node
				limit = 0
				with os.scandir(r'.\IconsRed') as red:
					for r in red:
						# Checks for optional red icon if not found default to 3 seconds
						if limit >= 300:
							if debug == True: print("Debug: Red node limit hit. No image found within 3 seconds.")
							break
						limit += 1
						time.sleep(0.01)
						try:
							pyautogui.locateOnScreen(r.path, confidence=0.70, region=retAround(loc, 10))
							time.sleep(0.1)
							break
						except pyautogui.ImageNotFoundException:
							pass
				break

			except pyautogui.ImageNotFoundException:
				pass

		if i != True:

			# Finds Prestege Button
			try:
				loc = pyautogui.locateOnScreen(r'stages\pres.png', confidence=0.40)
				if debug == True: print("Debug: pres.png found")
				moveClick(loc)
				time.sleep(15)
				continue
			except pyautogui.ImageNotFoundException:
				pass

			# Presses OK when showing prestege rewards
			try:
				loc = pyautogui.locateOnScreen(r'stages\rewardsunlocked.png', confidence=0.60)
				if debug == True: print("Debug: rewardsunlocked.png found")
				moveClick((1679, 920))
				print("+1 Prestige")
				presCount += 1
				time.sleep(5)
				continue
			except pyautogui.ImageNotFoundException:
				pass

			# Defaults to pressing autobuy button
			loc = (682, 558)
			moveClick(loc)
			while True:
				if stop_requested:
					finish()
				try:
					pyautogui.locateOnScreen(r'stages\presanimation.png', confidence=0.60)
					if debug == True: print("Debug: presanimation.png found")
					lvlCount += 1
					time.sleep(5)
					break
				except pyautogui.ImageNotFoundException:
					time.sleep(0.1)