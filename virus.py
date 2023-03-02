import datetime
from playsound import playsound

print(datetime.datetime.now())
first = int(input("hour: ").lower())
second = int(input("minutes: ").lower())
time = input("AM/PM: ").upper()

if time == "PM":
    first += 12

while True:
    if first == datetime.datetime.now().hour and second == datetime.datetime.now().minute:
        print("playing..")
        playsound(r'C:\Users\Prisca\Documents\SORT\kin.mp3')
        break
