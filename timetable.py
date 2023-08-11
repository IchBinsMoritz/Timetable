#!/bin/python
# from day import d
import time

#lessons
free = "Freistunde"
over = "frei"
brk = "Pause"
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
wed2 = "Chemie in C009"
wed3 = "Physik in C005"
wed4 = "Physik in C005"
wed6 = "Deutsch in I101"
wed8 = "Sozial Wissenschaften in I013"
wed9 = "Sozial Wissenschaften in I013"

#thursday
thu1 = "Deutsch in I102"
thu2 = "Deutsch in I102"
thu3 = "Religion in I102"
thu4 = "Englisch in I102"
thu5 = "Erdkunde in I101"
thu6 = "Erdkunde in I101"
thu8 = "Mathe in I013"

#friday
fri1 = "Mathe in I013"
fri2 = "Mathe in I013"
fri3 = "Sozial Wissenschaften in I013"
fri4 = "Latein in A012"
fri5 = "Chemie in C009"
fri6 = "Chemie in C009"
fri8 = "Musik in A010M"
fri9 = "Geschichte in I101"

now = "Du hast jetzt "
nxt = "Gleich hast du  "
day = time.strftime('%a', time.localtime())
time = time.strftime('%H.%M', time.localtime())

#monday
if day == "Mon" and float(time) > 7.00 and float(time) < 8.01 :
    print(now + over)
    print(nxt + mon1)

if day == "Mon" and float(time) > 8.00 and float(time) < 8.51 :
    print(now + mon1)
    print(nxt + mon2)

if day == "Mon" and float(time) > 8.50 and float(time) < 9.36 :
    print(now + mon2)
    print(nxt + brk)

if day == "Mon" and float(time) > 9.35 and float(time) < 9.56 :
    print(now + brk)
    print(nxt + mon3)

if day == "Mon" and float(time) > 9.55 and float(time) < 10.46 :
    print(now + mon3)
    print(nxt + mon4)

if day == "Mon" and float(time) > 10.45 and float(time) < 11.31 :
    print(now + mon4)
    print(nxt + brk)

if day == "Mon" and float(time) > 11.30 and float(time) < 11.51 :
    print(now + brk)
    print(nxt + mon5)

if day == "Mon" and float(time) > 11.50 and float(time) < 12.36 :
    print(now + mon5)
    print(nxt + mon6)

if day == "Mon" and float(time) > 12.35 and float(time) < 13.26 :
    print(now + mon6)
    print(nxt + brk)

if day == "Mon" and float(time) > 13.25 and float(time) < 14.26 :
    print(now + brk)
    print(nxt + mon8)

if day == "Mon" and float(time) > 14.25 and float(time) < 15.16 :
    print(now + mon8)
    print(nxt + mon9)

if day == "Mon" and float(time) > 15.15 and float(time) < 16.01 :
    print(now + mon9)
    print(nxt + over)

#tuesday
if day == "Tue" and float(time) > 7.00 and float(time) < 8.01 :
    print(now + over)
    print(nxt + tue1)

if day == "Tue" and float(time) > 8.00 and float(time) < 8.51 :
    print(now + tue1)
    print(nxt + tue2)

if day == "Tue" and float(time) > 8.50 and float(time) < 9.36 :
    print(now + tue2)
    print(nxt + brk)

if day == "Tue" and float(time) > 9.35 and float(time) < 9.56 :
    print(now + brk)
    print(nxt + tue3)

if day == "Tue" and float(time) > 9.55 and float(time) < 10.46 :
    print(now + tue3)
    print(nxt + tue4)

if day == "Tue" and float(time) > 10.45 and float(time) < 11.31 :
    print(now + tue4)
    print(nxt + brk)

if day == "Tue" and float(time) > 11.30 and float(time) < 11.51 :
    print(now + brk)
    print(nxt + tue5)

if day == "Tue" and float(time) > 11.50 and float(time) < 12.36 :
    print(now + tue5)
    print(nxt + tue6)

if day == "Tue" and float(time) > 12.35 and float(time) < 13.26 :
    print(now + tue5)
    print(nxt + brk)

if day == "Tue" and float(time) > 13.25 and float(time) < 13.41 :
    print(now + brk)
    print(nxt + tue7)

if day == "Tue" and float(time) > 13.40 and float(time) < 14.25 :
    print(now + tue7)
    print(nxt + over)

if day == "Tue" and float(time) > 14.24 and float(time) < 16.00 :
    print(now + over)

#wednesday
if day == "wed" and float(time) > 8.00 and float(time) < 8.51 :
    print(now + over)
    print(nxt + wed2)

if day == "wed" and float(time) > 8.50 and float(time) < 9.36 :
    print(now + wed2)
    print(nxt + brk)

if day == "Wed" and float(time) > 9.35 and float(time) < 9.56 :
    print(now + brk)
    print(nxt + wed3)

if day == "wed" and float(time) > 9.55 and float(time) < 10.46 :
    print(now + wed3)
    print(nxt + wed4)

if day == "wed" and float(time) > 10.45 and float(time) < 11.31 :
    print(now + wed4)
    print(nxt + brk)

if day == "wed" and float(time) > 11.30 and float(time) < 11.51 :
    print(now + brk)
    print(nxt + free)

if day == "wed" and float(time) > 11.50 and float(time) < 12.36 :
    print(now + free)
    print(nxt + wed6)

if day == "wed" and float(time) > 12.35 and float(time) < 13.26 :
    print(now + wed6)
    print(nxt + brk)

if day == "wed" and float(time) > 13.25 and float(time) < 14.26 :
    print(now + brk)
    print(nxt + wed8)

if day == "wed" and float(time) > 14.25 and float(time) < 15.16 :
    print(now + wed8)
    print(nxt + wed9)

if day == "wed" and float(time) > 15.15 and float(time) < 16.01 :
    print(now + wed9)
    print(nxt + over)

#thursday
if day == "Thu" and float(time) > 7.00 and float(time) < 8.01 :
    print(now + over)
    print(nxt + thu1)

if day == "Thu" and float(time) > 8.00 and float(time) < 8.51 :
    print(now + thu1)
    print(nxt + thu2)

if day == "Thu" and float(time) > 8.50 and float(time) < 9.36 :
    print(now + thu2)
    print(nxt + brk)

if day == "Thu" and float(time) > 9.35 and float(time) < 9.56 :
    print(now + brk)
    print(nxt + thu3)

if day == "Thu" and float(time) > 9.55 and float(time) < 10.46 :
    print(now + thu3)
    print(nxt + thu4)

if day == "Thu" and float(time) > 10.45 and float(time) < 11.31 :
    print(now + thu4)
    print(nxt + brk)

if day == "Thu" and float(time) > 11.30 and float(time) < 11.51 :
    print(now + brk)
    print(nxt + thu5)

if day == "Thu" and float(time) > 11.50 and float(time) < 12.36 :
    print(now + thu5)
    print(nxt + thu6)

if day == "Thu" and float(time) > 12.35 and float(time) < 13.26 :
    print(now + thu6)
    print(nxt + brk)

if day == "Thu" and float(time) > 13.25 and float(time) < 14.26 :
    print(now + brk)
    print(nxt + thu8)

if day == "Thu" and float(time) > 14.25 and float(time) < 15.16 :
    print(now + thu8)
    print(nxt + over)

if day == "Thu" and float(time) > 15.15 and float(time) < 16.01 :
    print(now + over)

#friday
if day == "Fri" and float(time) > 7.00 and float(time) < 8.01 :
    print(now + over)
    print(nxt + fri1)

if day == "Fri" and float(time) > 8.00 and float(time) < 8.51 :
    print(now + fri1)
    print(nxt + fri2)

if day == "Fri" and float(time) > 8.50 and float(time) < 9.36 :
    print(now + fri2)
    print(nxt + brk)

if day == "Fri" and float(time) > 9.35 and float(time) < 9.56 :
    print(now + brk)
    print(nxt + fri3)

if day == "Fri" and float(time) > 9.55 and float(time) < 10.46 :
    print(now + fri3)
    print(nxt + fri4)

if day == "Fri" and float(time) > 10.45 and float(time) < 11.31 :
    print(now + fri4)
    print(nxt + brk)

if day == "Fri" and float(time) > 11.30 and float(time) < 11.51 :
    print(now + brk)
    print(nxt + fri5)

if day == "Fri" and float(time) > 11.50 and float(time) < 12.36 :
    print(now + fri5)
    print(nxt + fri6)

if day == "Fri" and float(time) > 12.35 and float(time) < 13.26 :
    print(now + fri6)
    print(nxt + brk)

if day == "Fri" and float(time) > 13.25 and float(time) < 14.26 :
    print(now + brk)
    print(nxt + fri8)

if day == "Fri" and float(time) > 14.25 and float(time) < 15.16 :
    print(now + fri8)
    print(nxt + fri9)

if day == "Fri" and float(time) > 15.15 and float(time) < 16.01 :
    print(now + fri9)
    print(nxt + over)

#free
if float(time) > 15.59 and float(time) < 23.6 :
    print(now + over)

if float(time) > 0.00 and float(time) < 8.00 :
    print(now + over)