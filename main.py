import os
import re
from datetime import datetime
from pathlib import Path

data = "/home/tanvir_pc/sobriety-tracker/log.txt"
now = datetime.now()

if os.path.exists(data):
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    status = input("Have you broken your streak? [y/n] ")
    if(status == 'y'):
        prev_data = Path(data).read_text()
        #print(prev_data.splitlines()[3])
        with open(data, "w") as f:
            f.write(f"Today's date: {str(now).split('.')[0]}\n")
            f.write(f"Start date: {str(now).split('.')[0]}\n")
            f.write(f"Last sober: {prev_data.splitlines()[1].split(': ')[1]}\n")
            f.write(f"Current streak: 0 days\n")
            last_date = datetime.fromisoformat(prev_data.splitlines()[2].split(": ")[1])
            # f.write(f"Last streak: {str((now - last_date).days).split('.')[0]} day(s)")
            f.write(f"Last streak: {prev_data.splitlines()[3].split(': ')[1]}")
        print("\n===========================================")
        print(Path(data).read_text())
        print("===========================================\n")
        print("Don't give up, keep trying!\n")
    else:
        prev_data = Path(data).read_text()
        with open(data, "w") as f:
            f.write(f"Today's date: {str(now).split('.')[0]}\n")
            f.write(f"{prev_data.splitlines()[1]}\n")
            f.write(f"{prev_data.splitlines()[2]}\n")
            start_date = datetime.fromisoformat(prev_data.splitlines()[1].split(": ")[1])
            f.write(f"Current streak: {str((now - start_date).days)} day(s)\n")
            f.write(f"{prev_data.splitlines()[4]}")
        print("\n===========================================")
        print(Path(data).read_text())
        print("===========================================")
        print("\nCongratulations, keep it up!\n")

else:
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    confirmation = input("Do you want to start being sober from today? [y/n] ")
    if(confirmation == 'y') :
        with open(data, "w") as f:
            f.write(f"Today's date: {str(now).split('.')[0]}\n")
            f.write(f"Start date: {str(now).split('.')[0]}\n")
            f.write(f"Last sober: {str(now).split('.')[0]}\n")
            f.write(f"Current streak: 0 days\n")
            f.write(f"Last streak: You have not broken any streaks!")
        print("\n===========================================")
        print(Path(data).read_text())
        print("===========================================")
