import datetime

folder = None

Try


date_hour = (datetime.datetime.now())
date, hour = str(date_hour).split()

folder = open ('greeting.txt', 'a')

folder.write('Hey, I\'m Felipe\n')
folder.write(date)
folder.write(date)
folder.write()
folder.write()
folder.write()
folder.write('\n')

folder.close()

folder = open ('greeting.txt', 'r')
read = folder.read()
print (read)
folder.close()

folder = open ('greeting.txt', 'r')
line = folder.readline()

while line != "":
    print(line)
    line = folder.readline()
folder.close()

folder = open ('greeting.txt', 'r')



print (f'The folder has {l} lines')


# r
# w
# a
#
# r+
# w+
# a+
#
# b -> (rb, wb, ab)
# x
