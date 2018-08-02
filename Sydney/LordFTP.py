##这段代码用于读取FTP服务器的文件,由于我们服务器是对order等数据定时存储,并用时间作为文件名,故使用了排序取最大值的方式提取最新的文件
from ftplib import FTP
ftp = FTP()
# ftp.set_debuglevel(2)    #打开调试
timeout = 30
port = 21
ftp.connect('172.18.81.**',port,timeout) # 连接FTP服务器
ftp.login('***','***') # 登录

ftp.cwd('MM/daixiu')    # 设置FTP路径
FtpList1 = ftp.nlst()       # 获得目录列表
NewFtplist1 = sorted(FtpList1, reverse=True)   #排序文件名
BufSize = 1024
# for FtpFileName in FtpList:
#     print(FtpFileName)             # 打印文件名字
FileName1 = NewFtplist1[0]            # 需要下载的FTP文件名,取文件列表最大
with open(path1, 'wb') as File_handle1:
    ftp.retrbinary('RETR %s' % FileName1, File_handle1.write, BufSize)
ftp.cwd('..')    # 设置FTP路径
ftp.cwd('..')    # 设置FTP路径
ftp.cwd('MM/order')
FtpList2 = ftp.nlst()       # 获得目录列表
NewFtplist2 = sorted(FtpList2, reverse=True)   #排序文件名 由大到小
FileName2 = NewFtplist2[0]            # 需要下载的FTP文件名,取文件列表最大
with open(path2, 'wb') as File_handle2:
    ftp.retrbinary('RETR %s' % FileName2, File_handle2.write, BufSize)
ftp.quit()   
