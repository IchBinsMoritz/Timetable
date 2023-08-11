#!/bin/python
# from day import d
import time

#lessons
free = "Freistunde"
brk = "pause"
#monday
mon1 = "Sport in Halle 2"
mon2 = "Sport in Halle 2"
mon3 = "Musik in A010M"
mon4 = "Musik in A010M"
mon5 = "Latein in I103"
mon6 = "Latein in I103"
mon8 = "Englisch in I102"
mon9 = "Englisch in I102"

#tuesday
tue1 = "Physik in C005"
tue2 = "Erdkunde in I101"
tue3 = "Geschichte in I101"
tue4 = "Geschichte in I101"
tue5 = "Religion in I102"
tue6 = "Religion in I102"
tue7 = "Sport in Halle 2"

#wednesday


#thursday


#friday

now = "Du hast jetzt "
fifteen = time.strftime('%H.%M', time.localtime())
day = time.strftime('%a', time.localtime())
time = time.strftime('%H.%M', time.localtime())







if day == "Fri" and float(time) > 17.00 and float(time) < 18.00 :
    print(now)