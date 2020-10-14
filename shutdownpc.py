import os
check = input("Want to shut down your computer? (yes/no)\n>>> ")
if check == "no":
    print("System will not shutdown")
elif check == 'yes':
    act2 = input("Are you sure?(yes/no)\n>>>")
    if act2 == 'yes':
        print("your pc will now shutdown.")
        os.system("shutdown /s /t 1")
    elif act2 == "no":
        print("System will not shutdown.")
else:
    print("system was unable to process the code.")
