import datetime
import time

host_path = '/etc/hosts'

host = open(host_path , 'a+')

def removeHost(f, host):
    lines = f.readlines()
    hostRemove = host + '\n'
    if hostRemove in lines:
        lines.remove(hostRemove)
        tam = len(hostRemove)
        f.seek(0)
        print lines
        for line in lines:
            f.write(line)
            f.write(' '*tam)


while True:
    times = datetime.datetime.now()
    times = str(times)
    year, hour = times.split()
    hour = hour.split(':')
    if int(hour[0]) > 9 and int(hour[0]) <12:
        host.write('127.0.0.1 www.google.com')
        print " Working Hours 1"
    elif int(hour[0]) >12 and int(hour[0]) <13:
        host.write('')
        print "Lauch Hours"
    elif int(hour[0]) >13 and int(hour[0]) <18:
        try:
            host.write('127.0.0.1 www.google.com')
        except Exception as e:
            print e
        print "Working Hours 2"

    else:
        removeHost(host, '127.0.0.1 www.google.com' )
        print "Work is already finish for today"
    time.sleep(5)
host.close()
