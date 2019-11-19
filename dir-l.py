#/usr/bin/env python3
# -*- coding:utf-8 -*-
#练习：利用os模块编写一个能实现dir -l输出的程序。

import os,time,stat     

def  number2rwx(number):
    if number == '0':
        return '---'
    elif number =='1':
        return '--x'
    elif number =='2' :
        return '-w-'
    elif number =='3':
        return '-wx'
    elif number =='4':
        return 'r--'
    elif number =='5':
        return 'r-x'
    elif number =='6':
        return 'rw-'
    elif number =='7':
        return 'rwx'
    else:
        return  'null'
        

def ReadWrite(filename):
    st = os.stat(filename)    
    resultrwx = ''
    if os.path.isdir(filename):
        resultrwx = 'd'
    if  os.path.isfile(filename):
        resultrwx = '-'
        
    mode = st.st_mode
    stateoct = (oct(stat.S_IMODE(mode)))[2:]
    for i in range(len(stateoct)):
        resultrwx = resultrwx+number2rwx(stateoct[i])

    return resultrwx+'.'
    
#print(ReadWrite('aa'))

def getFileLink(filename):
    st = os.stat(filename)
    return st.st_nlink

#print(getFileLink('aa'))

def getOwner(filename):
    st = os.stat(filename)
    if st.st_uid == 0 and st.st_gid == 0:
        return 'root root'
    else:
        return 'null'
#print(getOwner('aa'))    

def getFileSize(filename):
    st = os.stat(filename)
    sizestr = str(st.st_size)    
    return '{:>9}'.format(sizestr)
#print(getFileSize('aa'))

def getFileMTime(filename):
    st = os.stat(filename)
    timestamp = st.st_mtime
    timearr = time.localtime(timestamp)
    if timearr.tm_year == 2019:
        return time.strftime("%b %d %H:%M",timearr)
    else:
        return time.strftime("%b %y  %Y", timearr)    

#print(getFileMTime('aa'))

def getFileSizeTotal(filenamelist):
    sum = 0 
    for file in filenamelist:
        st = os.stat(file)
        sizeint = st.st_size
        sum = sum + sizeint
       
    FileSizeTotal = sum//1024
    return FileSizeTotal
#print(getFileSizeTotal([x for x in os.listdir('.')]))

filepath= os.path.abspath('.')
filenamelist = [x for x in os.listdir('.')]
filenumber = len(filenamelist)
#filestate = os.stat(filename)  
print('total ',getFileSizeTotal(filenamelist))
for file in filenamelist:
    line = ReadWrite(file)+' '+str(getFileLink(file))+'  '+getOwner(file)+' '+str(getFileSize(file))+ ' '+\
           getFileMTime(file)+' '+file
    print(line)

    
