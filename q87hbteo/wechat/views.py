from django.shortcuts import render
from django.http import HttpResponse
import hashlib
import time
# Create your views here.

def wechat_main(request):
    if request.method == 'GET':
        signature = request.GET.get('signature', None)
        timestamp = request.GET.get('timestamp', None)
        nonce = request.GET.get('nonce', None)
        echostr = request.GET.get('echostr', None)

        token='wexin'

        hashlist=[token,timestamp,nonce]
        hashlist.sort()

        hashstr=''.join([s for s in hashlist])
        hashstr=hashlib.sha1(hashstr).hexdigest()

        if hashstr == signature:
            return  HttpResponse(echostr)


