from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render, redirect
from app.models import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User ,auth



def home (request):
    return render (request,"index.html")

def log_in (request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username = username, password = password)

        if ( user.is_superuser == True ) :


            auth.login(request,user)

            return redirect('dashboard')
               
           

        else :
             messages.info(request,'Please enter the correct username and password for a admin account.')
             return redirect('log_in')
    return render(request,"login.html")


@login_required(login_url='log_in')
def dashboard(request):
    
    info = contact_table.objects.all()
    # contact is table name which we create in models.py
    data = {'information':info}

    print('You are logged in, Hi', request.session.get('username_id'))

    return render(request, 'dashboard/dashboard.html', data)

def contact_info(request):

    info = contact_table.objects.all()
    # contact is table name which we create in models.py
    data = {'information':info}
    return render(request, 'dashboard/tables.html', data)


def contact(request):

    if request.method == "POST":
        a = request.POST.get('name')
        b = request.POST.get('email')
        c = request.POST.get('subject')
        d = request.POST.get('message')

        enquiry = contact_table(name = a, email = b, subject = c, message = d)
        enquiry.save()

        messages.success(request, 'message is successfully send')

    return render(request, 'contact.html')
def farmer_log(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username = username, password = password)

        if user is not None:
            # is not None is keyword None 'N' is capital which check above user (username and password) is available in database or not

            login(request, user)
            
            request.session['username_id'] = username    

            # Redirect to a success page.
            return redirect('farmer_ui')
            # from django.shortcuts import redirect, render - this module we need to import in same file, to access redirect() where only path name should be call
        else:
            # display 'invalid login' error message
            messages.error(request, 'In-correct username or password!..')    
        
    return render (request,"farm_log.html")

def farmer_info(request):
    info = farmer_table.objects.all()
    # contact is table name which we create in models.py
    data = {'information':info}
    
    return render(request, 'dashboard/table2.html',data)

def portfolio(request):
    return render(request,"portfolio.html")
def delete_record(request, id):
   
    enquiry = farmer_table.objects.get(pk=id)
    enquiry.delete()
    return redirect('/farmer_info/')
    
def farmer(request):



    




    if request.method == "POST":

            a = request.POST.get('name')
            b = request.POST.get('email')
            c = request.POST.get('username')
            d = request.POST.get('city')
            e = request.POST.get('password')

           
            my_user = User.objects.create_user(c,b,e)   
            my_user.save()

            enquiry = farmer_table(name = a, email = b, username = c, city = d , password = e)
            enquiry.save()

            messages.success(request, 'YOUR ACCOUNT IS CREATED')

    return render(request, 'farm_sign.html')
# Create your views here.

def customer(request):
    if request.method == "POST":
        abc= request.POST.get("name")
        email=request.POST.get("email")
        username=request.POST.get("username")
        gender=request.POST.get("gender")
        mobile=request.POST.get("mobile_no")
        password=request.POST.get("password")
        customer=request.POST.get("is_customertable")
        if User.objects.filter(username=username).exists():

            messages.info(request,'username already taken')
            return redirect('customer')

        elif User.objects.filter(email=email).exists():




            messages.info(request,'email already taken')
            return redirect('customer')
                
        else:


            

           
            my_users = User.objects.create_user(username,email,password)   
            my_users.save()

            cust = customertable(name = abc, email = email, username = username, mobile_no=mobile , password =password,gender=gender)
            cust.save()

            messages.success(request, 'YOUR ACCOUNT IS CREATED')

        return redirect('customer_login')
    return render(request,'signup.html')
def user_ui(request):
    return render(request,"user_ui.html")

def customer_login(request):
    if request.method == 'POST':

          username =  request.POST.get('username')
          password =  request.POST.get('password')
 
          user = auth.authenticate(username=username,password=password)

          if user is not None :
            if (user.customertable.is_customertable == True ) :
                auth.login(request,user)


                request.session['username'] = user.username

                return redirect('user_ui')
               

             
            
                
            else:
                  messages.info(request,'invalid credentials')
                  return redirect('customer_login')


          else :
             messages.info(request,'invalid credentias')
             return redirect('customer_login')


    else :




        return render(request,'dashboard/login.html')

   

    

def farmer_ui(request):
    return render(request,"abc.html")