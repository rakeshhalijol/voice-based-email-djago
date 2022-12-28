from django.shortcuts import render,redirect
from django.contrib.auth.models import auth,User
from django.contrib import messages
from django.http import HttpResponse
import speech_recognition as sr
import smtplib
from django.core.mail import send_mail
from voicebasedemail.emset import sett
from .models import *
from django.core import mail

r = sr.Recognizer()
import pyttsx3
# Create your views here.

def signin(request):
    if request.method == "POST":
        email = request.POST.get("email")
        pass1 = request.POST.get("pass1")
        pass2 = request.POST.get("pass2")

        if email == "" or pass1 == "" or pass2 == "":
            messages.info(request,"Fields required")
            return redirect("/")

        get_email = User.objects.filter(email = email).first()
        if get_email:
            messages.info(request,"Email already exists")
            return redirect("/")

        else:
            if pass1 == pass2:
                create_user = User.objects.create_user(username = email[0:6],email = email,password=pass1)
                create_user.save()
                messages.info(request,"Signin successfull")
                return redirect("/login/")

            else:
                messages.info(request,"Password missmatch")
                return redirect("/")
    else:
        return render(request,'signin.html')

def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        pass1 = request.POST.get("pass1")

        if email == "" or pass1 == "":
            messages.info(request,"Fields required")
            return redirect("/")
        user = auth.authenticate(username = email[0:6],email = email,password = pass1)
        print("The user is",user)
        if user:
            auth.login(request,user)
            get_user = User.objects.filter(email = email)[0]
            u = U.objects.filter(usr = get_user)
            if len(u) == 0:
                U.objects.create(usr = get_user,login = True,logout = False)
            else:
                u.update(login = True,logout = False)
            return redirect('/main/')
        else:
            messages.info(request,"Incorrect data entered")
            return redirect("/login/")

    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect("/")

def main(request):

    if request.method == 'POST':
        out = request.POST.get("out")
        reciver = request.POST.get("reciver")
        print(f"reciver is {reciver} output is {out} sender is {request.user.email}")
        u,v = request.user.email,request.user.password
        sett["EMAIL_HOST_USER"] = request.user.email
        sett["EMAIL_HOST_PASSWORD"] = request.user.password

        print(sett["EMAIL_HOST_USER"])


        send_mail('subject',out,"sss7259675199@gmail.com",[reciver],fail_silently=False)
        return HttpResponse("Mail sent")

    return render(request, 'main.html')


def inbox(request):
    import imaplib
    import email
    from email.header import decode_header
    import webbrowser
    import os
    all_data = {}
    username = "sss7259675199@gmail.com"
    password = "xnlrrmmkusjzarbk"
    imap = imaplib.IMAP4_SSL("imap.gmail.com")
    result = imap.login(username, password)
    imap.select('"[Gmail]/All Mail"', readonly=True)
    response, messages = imap.search(None, 'UnSeen')
    messages = messages[0].split()
    latest = int(messages[-1])
    oldest = int(messages[0])

    for i in range(latest, latest - 20, -1):
        z = {}
        bdy = []
        res, msg = imap.fetch(str(i), "(RFC822)")
        for response in msg:
            if isinstance(response, tuple):
                msg = email.message_from_bytes(response[1])
                z['d'] = msg["Date"]
                z['f'] = msg["From"]
                z['s'] = msg["Subject"]
        print(z)

        for part in msg.walk():
            if part.get_content_type() == "text / plain":
                body = part.get_payload(decode=True)
                print(f'Body: {body.decode("UTF-8")}', )
                z['b'] = body.decode("UTF-8")
                bdy.append(body.decode("UTF-8"))
        all_data[f"data{i}"] = z
        print("*******************************************")
        print(bdy)


    return render(request,'inbox.html',{'all_data':all_data})


def separate(request):
    return render(request,'separate.html')

