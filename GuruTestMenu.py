# *************************************************************************************
# Title:        Group Project: Group 1 Module 8
# Author:       Robert Macklem
# Date:         April 14 2024
# Description:  Test Selection Program for Guru99
# *************************************************************************************
import subprocess

# CONSTS
MENU_MESSAGE = (
    "\nPlease select which test module you would like to run:"
    "\n"
    "\n1:\tModule 1: New Customer"
    "\n2:\tModule 2: Edit Customer"
    "\n3:\tModule 3: Delete Customer"
    "\n4:\tModule 4: New Account"
    "\n5:\tModule 5: Edit Account"
    "\n6:\tModule 6: Delete Account"
    "\n7:\tModule 7: Balance Enquiry"
    "\n8:\tModule 8: Mini-statement"
    "\n9:\tModule 9: Customized Statement"
    "\n"
    "\n00:\tRun All"
    "\n99:\tExit"
    "\n"
    "\n"
)

EXIT_MESSAGE = "\nExiting testing program\n\nGoodbye...\n"

# VARS
# Modules
modules = {
    1: "module1_test.py",
    2: "module2_test.py",
    3: "module3_test.py",
    4: "module4_test.py",
    5: "module5_test.py",
    6: "module6_test.py",
    7: "module7_test.py",
    8: "module8_test.py",
    9: "module9_test.py"
}


# FUNCS
def run_all_modules():
    for i in modules:
        subprocess.run(["python", modules[i]])


# PROGRAM
# Welcome message
print("\n********************************************"
      "\nWelcome to the Guru99 Test Selection Program"
      "\n********************************************")

# Main loop
exiting = False
while not exiting:
    try:
        mode = int(input(MENU_MESSAGE))
        if mode == 00:
            run_all_modules()

        elif mode == 99:
            exiting = True

        else:
            subprocess.run(["python", modules[mode]])

    except:
        print("\n***INVALID SELECTION** Please re-try.\n")

print(EXIT_MESSAGE)
