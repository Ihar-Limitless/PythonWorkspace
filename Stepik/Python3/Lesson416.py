import datetime
dat = input().split()
a = datetime.date(int(dat[0]), int(dat[1]), int(dat[2]))
b = datetime.timedelta(int(input()))
c = a+b
print(c.year, c.month, c.day)