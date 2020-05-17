#By R@H33M_Haxor
import requests,socket,argparse,sys,os,threading,queue,re
import os
from urllib.request import urlopen
#list of admins , Extend it if you want more results results
import webbrowser

getx=['/admin/','/administrator/','/admin-cp/','/webways-admin/','/admin_login/','/admin/index.php/','/admin/dashboard.php/','/admin/home.php/','/admin/adminindex.php/']

found=[]
#Queue

q=queue.Queue()
#parser
parser=argparse.ArgumentParser(description="Reverse IP admin finder ./Hunter Hassam")
# parser.add_argument("--timeout","-t", help="Custom connection timeout",type=float,default=2.0)
# parser.add_argument("--target","-u", help="Specify the target URL/IP")
parser.add_argument("--proxy","-p",help="Proxy e.g 127.0.0.1:8080 ")
# parser.add_argument("--thrd","-w",help="Number of threads",type=int,default=2)
args=parser.parse_args()
#cleaner
if sys.platform == "linux" or sys.platform == "linux2":
    cl = "clear"
else:
    cl="cls"
os.system(cl)
def banner():
    print("\n")
    print("\t /$$   /$$           /$$   /$$           /$$           /$$ /$$$$$$$$  ")
    print("\t| $$  | $$          | $$  / $$          | $$          |__/|__  $$__/  ")
    print("\t| $$  | $$  /$$$$$$ |  $$/ $$/  /$$$$$$ | $$  /$$$$$$  /$$   | $$     ")                                      
    print("\t| $$  | $$ /$$__  $$ \\  $$$$/  /$$__  $$| $$ /$$__  $$| $$   | $$    ")
    print("\t| $$  | $$| $$$$$$$$  >$$  $$ | $$  \\ $$| $$| $$  \\ $$| $$   | $$   ")
    print("\t| $$  | $$| $$_____/ /$$/\\  $$| $$  | $$| $$| $$  | $$| $$   | $$    ")
    print("\t|  $$$$$$/|  $$$$$$$| $$  \\ $$| $$$$$$$/| $$|  $$$$$$/| $$   | $$    ")
    print("\t \\______/  \\_______/|__/  |__/| $$____/ |__/ \\______/ |__/   |__/  ")
    print("\t                              | $$                                    ")
    print("\t                              | $$                                    ")
    print("\t                              |__/                                    ")
banner()

def stormer(q,getx):
    try:
        log=open('sites.txt','a')
        while not q.empty():
            site=q.get(block=True, timeout=2)
            for adm in getx:
                cn=requests.get('http://'+site+adm)
                if cn.status_code==404:
                    pass
                else:
                    rsp=cn.text
                    rx=re.findall('type="Password"',rsp,re.I)
                    if  len(rx) ==1:
                        if "wp-admin" in rsp:
                            print('[w] %s'%site+adm)
                            found.append('[w] http://%s'%site+adm)
                        else:
                            
                            print('[+] %s'%site+adm)
                            webbrowser.open(site+adm)
                            found.append('[+] http://%s'%site+adm)
                    else:
                        pass
            q.task_done()
    except Exception as e:
        pass
    finally:
        for uri in found:
            log.write(uri+'\n')
        log.close()

def killa(nom):
    for i in range(nom):
        thread=threading.Thread(target=stormer,args=(q,getx,))
        thread.start()
    thread.join()
#target filter
try:
    target= input("Enter URL: \n\n")
    if target[-1]=='/':
        target=target.replace(target[-1],"")
        target=target.replace("http://","")
        
    yg=open('list.txt','w')
    target=socket.gethostbyname(target)
    print("\n"+"-"*25)
    print('Target : %s' %target)
    print("-"*25)
    #proxy 
    proxy=args.proxy
    proxies={}
    if proxy:
        proxies = {'http':'http://'+proxy}
    #request
    url = "https://domains.yougetsignal.com/domains.php"
    useragent = "Mozilla/5.0 (Windows NT 5.1; rv:24.0) Gecko/20100101 Firefox/24.0"
    postdata = {'remoteAddress':target,'key':''}
    result = requests.post(url, data=postdata,headers={'User-Agent':useragent},proxies=proxies)
    #reading youget response
    dom=result.json()
    #filter
    #stripper 😉
    if dom['status'] == 'Success':
        l=int(dom['domainCount'])
        if l==0:
            print("[-] No Domain Found")
        print("-"*25)
        print("[+] Domain list fetch complete \n[+] Domain count : %s" % l)
        print("[+] Ip: %s" % dom['remoteIpAddress'])
        print("-"*25)
        #writer
        with open('list.txt','w') as yg:
            for each in dom['domainArray']:
                yg.write(each[0]+'\n')
        #REverse IP COmplete
        if proxy:
            print("-"*25+'\n'+'Proxy : %s'%proxy+'\n'+"-"*25)
        # if args.thrd:
        #   print("-"*25+'\n'+'Threads: %s'%args.thrd+'\n'+"-"*25)
        # if args.timeout:
            print("-"*25+'\n'+'Timeout: %s Seconds'%args.timeout+'\n'+"-"*25)
        #Start of Admin buster
        
        lstx=open('list.txt','r')
        sites=lstx.readlines()
        print("\n"+"-"*25)
        print(' Rsp | \tURL')
        print('-'*25)
        socket.setdefaulttimeout(3)
        for each in dom['domainArray']:
            q.put(each[0])
    else:
        print("[-] IP Limit Reached")
    while not q.empty():
        killa(5)
except TypeError:
    print("[-] NO target specified")
except socket.gaierror:
    print("[-]NOPE WRONG URL")
except KeyboardInterrupt:
    print("[-] Abort signal Detected")
except Exception as e:
    print(e)
    print("[-] Something went wrong try again or let it go")
input("\n\nEverything Modified By Hunter Hassam\nPress Enter Key To Exit.");


#Modified by Hunter Hassam
#Team Pak Cyber Hunters