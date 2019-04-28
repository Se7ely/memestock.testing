import math
for i in range(1920):
    print(" assign allroundkeysout["+str(1919-i)+"]=allroundkeys["+str(math.floor(i/32))+"]["+str(i%32)+"];")
