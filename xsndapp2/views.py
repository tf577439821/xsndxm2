from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse

# Create your views here.
def login(request):
    if request.method=="GET":
        return render(request,'login.html')
    elif request.method=='POST':
        u = request.POST.get('user')
        p = request.POST.get('pwd')
        #获取对象
        obj=models.UserInfo.objects.filter(username=u,password=p).first()
        #获取个数
        #count = models.UserInfo.objects.filter(username=u, password=p).count()
        #print(obj)
        #print(count)
        if obj:
            return redirect('/index/')
        else:
            return render(request,'login.html')

    else:
        return redirect(request,'/index/')

from xsndapp2 import models
#增加数据
def orm(request):
#增  #models.UserInfo.objects.create(username='root',password='123')
    #return HttpResponse('orm')
#查  result=models.UserInfo.objects.filter(username='root')
#    for row in result:
 #       print(row.id,row.username,row.password)
#删   models.UserInfo.objects.filter(username='xxx').delete()
#更新
#改名字models.UserInfo.objects.all().update(password='yyy')
      models.UserInfo.objects.filter(id=2).update(password='yyy')

from django.views import View

class Home(View):

    def get(self,request):
        print(request.method)
        return render(request, 'home.html')

    def post(self,request):
        print(request.method)
        return render(request, 'home.html')


USER_DI={
    '1':{'name':'12324','des':'5532'},
    '2':{'name':'54645','des':'5511'},
    '3':{'name':'88888','des':'5522'},
}

def index(request):

    return render(request,'index.html')

def detail(request,nid):
    detail2=USER_DI[nid]
    return render(request, 'detail.html', {'detail2':detail2})


def user_info(request):
    user_list=models.UserInfo.objects.all()
    return render(request,'user_info.html',{'user_list':user_list})

def user_detail(request,nid):
    obj=models.UserInfo.objects.filter(id=nid).first()
    return render(request, 'userdetail.html', {'obj':obj})