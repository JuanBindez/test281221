import os
import time

def op1():
    time.sleep(1)
    os.system("grep MemTotal /proc/meminfo")

def op2():
    time.sleep(1)
    os.system("cat /proc/meminfo")

def op3():
    time.sleep(1)
    os.system("free -m")


x = int(input("digite opção 1 , opção 2 ou opção 3:"))

if x == 1:
    op1()

if x == 2:
    op2()

if x == 3:
    op2()
