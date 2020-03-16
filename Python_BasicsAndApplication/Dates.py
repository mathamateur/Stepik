import datetime


y,m,d = map(int,input().split())

date = datetime.date(y,m,d)
delta = datetime.timedelta(float(input()))
print((date+delta).year,(date+delta).month,(date+delta).day)