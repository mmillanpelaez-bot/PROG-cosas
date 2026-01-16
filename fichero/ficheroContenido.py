import pickle
import datetime

date_hour = (datetime.datetime.now())
date, hour = (str(date_hour).split())
print(date, hour)

ymd = date.split('-')
hms = hour.split(':')

date_time = {
    'year': ymd[0],
    'month': ymd[1],
    'day': ymd[2],
    'hour': hms[0],
    'minute': hms[1],
    'second': hms[2]
}

with open ('date.dat', 'wb') as folder:
    pickle.dump(date_time, folder)

with open ('date.dat', 'rb') as folder:
    dic = pickle.load (folder)
    print(dic['hour'])
    print(dic['minute'])

user_options = {
    'theme': 'dark',
    'font-size': 14,
    'show_line_numbers': True
}

with open ('options.dat', 'wb') as fol:
    pickle.dump (user_options, fol)

with open ('options.dat', 'rb') as fol:
    opt = pickle.load(fol)

# dump
# load
# dumps
# loads
