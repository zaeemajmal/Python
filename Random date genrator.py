import random
import datetime
year = random.randint(1, 2000)
month = random.randint(1,12)
day = random.randint(1,28)
hour = random.randint(0,24)
min = random.randint(0, 59)
sec = random.randint(0, 59)
date = datetime.datetime(year,month,day,hour,min,sec)

print(date)


