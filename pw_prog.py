# Import modules

import subprocess as s
import os.path
import time
import pyautogui
import psutil


# Ensure all file locations are correct

def check_file_locations():
    
    if (os.path.isfile(keepass_app) and 
        os.path.isfile(keepass_db) and 
        os.path.isfile(pw_file) and 
        os.path.isfile(test)):

        return True
    
    else:
        return False


# Ignore the pw file YAML header

def cleanup_pw_file(pw_file):
    
    clean_pw_file = []
    
    for line in open(pw_file, 'r'):
        if not line.startswith(tuple(keyword_list)):
            line = line.strip()
            clean_pw_file.append(line)
        
    return clean_pw_file


# Check each permutation in the calculated pw file!

def check_each_pw(clean_pw_file, counter):

    # If KeePass is not running
    if "KeePass.exe" not in (i.name() for i in psutil.process_iter()):

        # Start counter
        counter = counter

        # For each password in the list
        for pw in clean_pw_file[counter:]:

            # Iterate counter
            counter += 1
            print(f'{counter}/{len(clean_pw_file)}')

            # Open KeePass
            t = s.Popen([keepass_app, keepass_db])

            # Move cursor to MasterPW field
            pyautogui.moveTo(x=916, y=568, duration=0.50)

            # Click MasterPW field
            pyautogui.click()

            # Type in MasterPW
            pyautogui.typewrite(pw)

            # Move cursor to the view button (good for debugging)
            #pyautogui.moveTo(x=1135, y=572)

            # Click the view button (good for debugging)
            #pyautogui.click()

            # Move cursor to OK button
            pyautogui.moveTo(x=1014, y=669)

            # Click Ok
            pyautogui.click()

            # Wait for OpenCV to scan the screen
            time.sleep(1)

            # If the 'alert' popup is NOT found, then the pw must have worked!
            if pyautogui.locateOnScreen('alert.png') is None:
                print(f'The password has been found: {pw}')
                quit()

            # Else, close KeePack and try the next password                
            else:
                t.terminate()


# KeePass executable, KeePass db, computed pw file, and test file locations

# Something like C:\Program Files\KeePass Password Safe 2\KeePass.exe
keepass_app = ''

# Somethinglike E:\Documents\personal\latest.kdbx
keepass_db = ''

# Keep the pw file in the same directory as the pw_prog.py file
pw_file = 'output.txt'

# Slap a test file in the same directory as the pw_prog.py file
test = 'test.txt'

# Keywords to ignore (I orginally used Dendron to as my pw list, this ignores the YAML header)

keyword_list = ['\n', '---', 'id', 'title', 'desc', 'updated', 'created']

# Counter in case I want to stop the program and pick up where it left off

counter = 0

# Call functions

if check_file_locations():
    clean_pw_file = cleanup_pw_file(pw_file)
    check_each_pw(clean_pw_file, counter)