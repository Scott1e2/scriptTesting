import pyautogui

# Move the cursor to the location of the first input field
pyautogui.moveTo(100, 200)

# Enter some text into the field
pyautogui.typewrite("John Smith")

# Move the cursor to the location of the next input field
pyautogui.moveTo(100, 250)

# Enter some text into the field
pyautogui.typewrite("jsmith@example.com")

# Move the cursor to the location of the submit button
pyautogui.moveTo(150, 300)

# Click the submit button
pyautogui.click()

#This script uses the PyAutoGUI library to simulate mouse movements and keyboard input, 

#Additionally, there are several other options available to automate data entry, such as Optical Character Recognition (OCR) software and robotic process automation (RPA) tools, These are more sophisticated and advanced tools.

