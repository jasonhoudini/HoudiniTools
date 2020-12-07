import os
import sys
import time

update = 5
repeat = 2
path = "E:/test"

def watchDir(path):
    print(time.ctime())
    # os.stat().st_mtime返回监管的Dir最后一次修改的时间戳（1970纪元后经过的浮点秒数）
    return os.stat(path).st_mtime


# 初始化检查时间和起始时间以及计数器
initCheck = watchDir(path)
startTime = time.time()
counter = 0

while True:
    # 检查Dir最后一次修改的时间
    check = watchDir(path)
    if initCheck != check:
        print("dir update, run something")
        initCheck = check
    counter += 1
    if counter == repeat:
        sys.exit()
    # 延迟一定的秒数再执行下一条语句，该句的意思是从startTime开始，必为每五秒执行一遍整个循环
    # time.time()返回当前时间的时间戳（1970纪元后经过的浮点秒数）
    time.sleep(update - (time.time()-startTime) % update)
