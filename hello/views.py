from django.shortcuts import HttpResponse
import threading
import logging
import random
import socket
import time

logging.basicConfig(format="%(asctime)s %(thread)d %(levelname)s - %(message)s", filename="helloworld.log")


def hello(request):
    ClinetIP = request.META.get("HTTP_X_FORWARDED_FOR") or request.META.get("REMOTE_ADDR")
    hostname = socket.gethostname()
    ServerIP = socket.gethostbyname_ex(hostname)
    return HttpResponse("hello world! Your ip is: %s, ServerHostname: %s, ServerIP: %s" % (
        ClinetIP.split(",")[0], hostname, ServerIP[-1][-1]))


def printNum():
    while True:
        time.sleep(2)
        num = random.randint(100, 200)
        logging.warning("线程已经启动，正在打印随机数: - %s -" % num)


def threadstart():
    t = threading.Timer(interval=5, function=printNum)
    t.start()


threadstart()
