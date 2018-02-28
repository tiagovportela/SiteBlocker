import datetime
import time

host_path = '/etc/hosts'
sites = ['www.google.com\n','www.facebook.com\n']

''' hostsRead(host, site)

    @param host: open file with hosts
    @param site: site to check if already exist in Hosts

    return True in case that site is already in host.
           False otherwise'''
def hostsRead(host, site):
    lines = host.readlines()
    #print 'Im doing comp!\n'
    #print lines
    if site in lines:
        return True
    else:
        return False

def deleteLine(host, site):
    host.seek(0)
    lines = host.readlines()

    if site in lines:
        lines.remove(site)
        host.seek(0)
        for line in lines:
            host.write(line)
        host.write(' '* len(site)+'\n')
        host.truncate()
    else:
        print 'Dont have any site blocked!'

while True:
    hour= datetime.datetime.now().hour
    host = open(host_path, 'r+')
    if  hour > 9 and hour < 18:
        print 'Working Hours'
        i=0
        for site in sites:

            if hostsRead(host, site) == False:
                host.write(site)
                print i
            else:
                print 'Already exist!'
            i +=1

        '''for site in sites:
            if hostsRead(host, site) == True:
                print 'already exist!'
                print site

            else:
                try:
                    print site
                    host.write(site)
                except Exception as e:
                    print e'''

    elif hour >= 18 and hour < 19:
        print 'Lauch Time!'
        for site in sites:
            deleteLine(host, site)
    host.close()
    time.sleep(5)
