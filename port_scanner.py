from socket import *
import optparse
import threading
import colorama
from colorama import Fore

def banner():
    print(r"""
            #####    ####   #####    #####           ####    ####     ##    #    #  
            #    #  #    #  #    #     #            #       #    #   #  #   ##   #
            #    #  #    #  #    #     #             ####   #       #    #  # #  #
            #####   #    #  #####      #                 #  #       ######  #  # #
            #       #    #  #   #      #            #    #  #    #  #    #  #   ##
            #        ####   #    #     #   #######   ####    ####   #    #  #    #
""")


def get_banner(s):
    return s.recv(1024)

def portscan(host, port):
    try:
          s = socket(AF_INET, SOCK_STREAM)
          s.connect((host, int(port)))
          try:
               banner = get_banner(s)
               print( host + " tcp/"   +Fore.GREEN +str(port) + "  open  " + Fore.WHITE+str(banner.decode().strip('\n'))+Fore.WHITE)
          except:
               print(host + " tcp/"   + Fore.GREEN +str(port) + "  open"+Fore.WHITE)
          s.close()
    except:
        print(host + " tcp/" + Fore.RED+ str(port) + " closed" + Fore.WHITE)


def main():

    banner()
    parser = optparse.OptionParser("usage " + "-H <specify target host> -p <specify ports separated by ','> ")
    parser.add_option("-H" , '--host',dest='targethost',type='string',help='specify target host')
    parser.add_option("-P" , '--ports' , dest='targetports' ,type='string',help='specify target ports separated by ","')

    option , args = parser.parse_args()

    thost = option.targethost
    tports = str(option.targetports).split(",")

    if thost == None or tports[0] == None:
        print(parser.usage)
        exit(0)

    setdefaulttimeout(1)
    host_ip = gethostbyname(thost)

    for port in tports:
        t = threading.Thread(target=portscan, args=(thost,port))
        t.start()


main()
