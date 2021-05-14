from django.shortcuts import render
import requests
import sys
import subprocess

# Create your views here.

def deploy(request):
    MYACC_PATH='/app/myacc/'
    MEDIA_URL='/app/media/'
    inp1= request.POST.get('param1') or ''
    inp2= request.POST.get('param2') or ''
    #print(f"{MYACC_PATH}deploy.py {MEDIA_URL}{inp1} {MEDIA_URL}{inp2}")

    #out= run([sys.executable,'myacc/deploy.py','/app/media/'+inp1,'/app/media/'+inp2],shell=False,stdout=PIPE)
    #out,err = run([sys.executable, f"{MYACC_PATH}deploy.py", f"{MEDIA_URL}{inp1}", f"{MEDIA_URL}{inp2}", "2>&1"], shell=False,stdout=PIPE,stderr=PIPE)
    #code, out, err = run([sys.executable, f"{MYACC_PATH}deploy.py", f"{MEDIA_URL}{inp1}", f"{MEDIA_URL}{inp2}"])

    result=subprocess.run([sys.executable, f"{MYACC_PATH}deploy.py", f"{MEDIA_URL}{inp1}", f"{MEDIA_URL}{inp2}"],capture_output=True,text=True,shell=False)

    return render(request, 'deploy.html',{ 'data1':result.stdout + result.stderr })
    #return render(request, 'deploy.html',{'data1':result.stdout + result.stderr}, content_type="html")
    #return render(request,'deploy.html',{'data1':out},content_type='application/xhtml+xml')
    #return render(request,'deploy.html',{'data1':out})

