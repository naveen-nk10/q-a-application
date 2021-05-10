from django.shortcuts import render,redirect
from . import forms
from django.contrib import messages
from django.contrib.auth.models import User,auth
#from django.contrib.auth import authenticate
from django.core.mail import send_mail
import smtplib
from clgprjt.settings import EMAIL_HOST_USER
from django.conf import settings
from django.core.mail import EmailMessage
import math,random
from . import models
from .models import Question,Answer
# Create your views here.
def post_answer(request):
    que=request.POST['ans']
   
    return render(request,'homepage.html',{'data':data,'ans':ans})
def answer(request):
    question__id=request.POST['question_id']
    print("question",question__id)
    return render(request,"post_ans.html")
def post_question(request):
    que=request.POST['text']
    q=Question(quest=que,user=request.user)
    q.save()
    data=Question.objects.all()
    ans=Answer.objects.all()
    print(data)
    return render(request,'homepage.html',{'data':data,'ans':ans})
def post(request):
    return render(request,"post.html")
def insta(reqest):
    return render(reqest,"login.html")
def login(request):
    
    if request.method == 'POST':
        name=request.POST['name']
        password=request.POST['password']
        print(name)
        print(password)
        q=User.objects.all()
        print(q)
        s=User.objects.filter(password=password)
        print(s)
        user=auth.authenticate(username=name,password=password)
        print(user)
        
        if user is not None:
            auth.login(request,user)
            data=Question.objects.all()
            ans=Answer.objects.all()
            print(data)
            return render(request,'homepage.html',{'data':data,'ans':ans})
        else:
            messages.info(request,'invalid password or username')
            return redirect('login')
    else:
        return render(request,'login.html')    

def register(request):
    if request.method == 'POST':
        
        
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        print("hii")
        
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                print("me")
                messages.info(request,'username')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email taken')
                return redirect('register')
            else:
               with smtplib.SMTP('smtp.gmail.com',587 ) as server:
                    digits="0123456789"
                    result=" "
                    for i in range(4):
                        otp=digits[math.floor(random.random()*7)]
                        
                        print(otp,end="")
                        result=result+otp
                    print()
                    print(result)
                    server.ehlo()
                    server.starttls()
                    server.ehlo()
                    server.login('nk4556138@gmail.com','naveennk')
                    subject='welcome'
                    body='hii'
                    msg=f"subject:{subject}\n\n{body}\n\n{result}"
                    server.sendmail(
                        'nk4556138@gmail.com',
                        email,
                        msg
                    )
                    print("sent")
                    
                
                    print("bye")
                
                    return render(request,'check.html',{'result':result,'email':email,'username':username,'password':password1,'password2':password2})

        else:
             messages.info(request,'password not created')
             return redirect('/')
    else:

         return render(request,'register.html')
               
def check(request):
    otp=request.POST['otp']
    res=0
    res=request.POST['result']
    
    username=request.POST['username']
    email=request.POST['email']
    cou=request.POST['count']
    password1=request.POST['password1']
    print(cou)
    if cou==0:
        return render(request,'check.html')
       
    else:
        
        if otp==res:
            user=User.objects.create_user(username=username,password=password1,email=email)
            user.save()
            messages.info(request,"usercreated")
            return render(request,'homepage.html')
        else:
            messages.info(request,"wrong otp")
            return render(request,'check.html')
def answ(request):
    ans=request.POST.get('que')
    answer_q=Answer.objects.filter(ques=ans)
    quest=Question.objects.filter(id=ans)
    
    print(answer_q)
    print(ans)
    return render(request,'ans.html',{'result':answer_q,'quest':quest})