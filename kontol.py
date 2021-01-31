#!/usr/bin/python2
# coding=utf-8
#Bocah kontol bisanya recode mulu ajg
#ngotak dong kontol


try:
    import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass, mechanize, requests, bababindsix
    from multiprocessing.pool import ThreadPool
    from requests.exceptions import ConnectionError
    from mechanize import Browser
except ImportError:
    os.system('pip2 install requests')
    os.system('pip2 install mechanize')
    time.sleep(1)
    os.system('python2 404.py')

reload(sys)
sys.setdefaultencoding('utf8')
os.system('clear')

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(3.0 / 200)


def psb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)


def tik():
    titik = [
     '   ', '.  ', '.. ', '...', '.. ', '.  ', '   ']
    for o in titik:
        print '\r\x1b[1;97m     [\x1b[1;92m•\x1b[1;97m] \x1b[1;91mLoa\x1b[1;97mding \x1b[1;94m' + o,
        sys.stdout.flush()
        time.sleep(0.7)


keyyy = '20x30id'

def yayan():
    os.system('clear')
    print ''
    print ''
    print '\x1b[1;97m  LICENSE KEY'
    print '\x1b[1;94m ───────────────'
    print '\x1b[1;97m '
    usr = raw_input('          \x1b[1;92mYOUR KEY \x1b[1;91m: \x1b[1;90m')
    if usr == keyyy:
        tik()
        xd()
    else:
        os.system('clear')
        print ''
        print ''
        print '\x1b[1;97m  LICENSE KEY'
        print '\x1b[1;94m ───────────────'
        print '\x1b[1;97m '
        print '          \x1b[1;97mYOUR KEY \x1b[1;91m: \x1b[1;93mJQSADSE3267 \x1b[1;91m' + usr + '\x1b[1;97m [\x1b[1;91m×\x1b[1;97m]'
        time.sleep(1)
        os.system('xdg-open https://youtu.be/bEUPM_BNMBw')
        yayan()


def xd():
    os.system('clear')
    print ''
    print ''
    print '\x1b[1;97m  LICENSE KEY'
    print '\x1b[1;94m ───────────────'
    print '\x1b[1;97m '
    print '          \x1b[1;97mYOUR KEY \x1b[1;91m: \x1b[1;90m1qC3c8i \x1b[1;97m[\x1b[1;92m•\x1b[1;97m]'
    print '\n\n \x1b[1;97mLICENSE KEY APPROVED BY \x1b[1;94mYayan XD.\x1b[0m'
    print ''
    jalan('\x1b[1;93mPLEASE WAIT 2MINUTES, ALL PACKAGES ARE CHECKING\x1b[1;97m...')
    time.sleep(1)
    os.system('python2 202.py')



if __name__ == '__main__':
    yayan()
