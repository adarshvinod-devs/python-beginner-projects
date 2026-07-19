import os
from datetime import datetime

os.system("cls")

a = " Hunter 350"
b = " Acess 125"
c = " Xpulse 210"
d = " GT 650"
e = " Interceptor 650"

hr = datetime.now().hour

if hr < 12 :
  wish = "Good Morning, Boss."
elif hr < 18 :
  wish = "Good Afternoon, Boss."
else:
  wish = "Good Evening, Boss."

print (f'''{wish}
1 = "Hunter 350"
2 = "Acess 125"
3 = "xpulse 210"
4 = "GT 650"
5 = "Interceptor 650"''')

valid_choice = True

while True:
  if valid_choice:
    ride = int (input(f"Choose Your Ride:"))
  else:
    ride = int (input("Choose one from the garage, Boss:"))

  match ride:
    case 1:
      print(f"You Choose{a}. Ah Yes, The OG")
      break

    case 2:
      print(f"You Choose{b}. A city commute, I assume")
      break

    case 3:
      print(f"You Choose{c}. Of-Roadind Today?")
      break

    case 4:
      print(f"You Choose{d}. Damnnnn")
      break

    case 5:
      print(f"You Choose{e}. A Long Cruis?")
      break

    case _:
      print("Huh?")
      valid_choice = False

    
    

