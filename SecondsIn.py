from datetime import datetime

inminute = 60
inhour = inminute * 60
inday = inhour * 24
inyear = inday * 365
now = datetime.now()
nowseconds = (now.hour * inhour + now.minute * inminute + now.second)

options = ("A Day","A week","A Month","A year","A Leap Year","Today")

for index, value in enumerate(options):
  print(f"{index + 1} : {value}")


months = ["January","February","March","April","May","June","July","August","September","October","November","December"]

def the_seconds_in_month(monthnumber):
  if monthnumber ==2:
    secondsinmonth = 28 * inday
  elif monthnumber % 2 == 0 and monthnumber < 7:
    secondsinmonth = 30 * inday
  elif monthnumber % 2 == 0 and monthnumber > 7:
    secondsinmonth = 31 * inday
  elif monthnumber <= 7:
    secondsinmonth = 31 * inday
  else:
    secondsinmonth = 30 * inday
  return secondsinmonth

def select_the_month():
  for index,value in enumerate(months):
    print (f"{index + 1} : {value}")
  whichmonth = int(input("Which Month?\n"))
  return whichmonth


while True:


  choice = int (input("How many seconds in what?:\n"))

  match choice:
    case 1 :
      print(f"There are {inday:,} seconds in a day")
      break
    case 2 :
      print(f"There are {inday * 7:,} seconds in a week")
      break
    case 3 :
      month_number = select_the_month()
      monthchoice =  the_seconds_in_month(month_number)
      if monthchoice == the_seconds_in_month(2):
        print(f"There are {monthchoice:,} seconds in {months[month_number - 1]} , {monthchoice + inday:,} if its leap year")
        break
      else:
        print(f"There are {monthchoice:,} seconds in {months[month_number - 1]}")
        break
    case 4 :
      print(f"There are {inyear:,} seconds in a year")
      break
    case 5 :
      print(f"There are {inyear + inday:,} seconds in a leap year")
      break
    case 6 :
      print(f"{nowseconds:,} seconds have passed today")
      break
    case _:
      print("Enter a valid choice: ")
