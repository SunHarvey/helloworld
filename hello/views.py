from django.shortcuts import HttpResponse
import socket


def hello(request):
    ClinetIP = request.META.get("HTTP_X_FORWARDED_FOR") or request.META.get("REMOTE_ADDR")
    hostname = socket.gethostname()
    ServerIP = socket.gethostbyname_ex(hostname)
    # print(ServerIP)
    return HttpResponse("hello world! Your ip is: %s, ServerHostname: %s, ServerIP: %s" % (
        ClinetIP.split(",")[0], hostname, ServerIP[-1][-1]))
