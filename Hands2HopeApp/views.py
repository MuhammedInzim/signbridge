from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from .forms import *
from .models import *
from datetime import datetime
from datetime import datetime
from django.contrib import messages
from django.shortcuts import redirect

# Create your views here.
from django.contrib import messages

class loginview(View):
    def get(self, request):
        return render(request,'administration/login.html')

    def post(self,request):
        username=request.POST.get('username')
        password=request.POST.get('password')

        try:
            obj=LoginTable.objects.get(username=username, password=password)
            request.session['user_id']=obj.id

            if obj.usertype=='admin':
                return redirect('/adminhompage')
            elif obj.usertype=='user':
                return redirect('/userhomepage')
            else:
                messages.error(request,"Invalid user type")
                return redirect('/')

        except LoginTable.DoesNotExist:
            messages.error(request,"Invalid Mail or Password")
            return redirect('/')
                 
class manageuser(View):
    def get(self,request):
        p=UserTable.objects.all()
        return render(request,'administration/manage_users.html',{'user':p})
    
class feedback(View):
        def get(self,request):
            c=FeedbackTable.objects.exclude(USER__LOGIN_id=request.session['user_id'])
            return render(request,'administration/feedback.html',{'user':c})
        
class complaints(View):
     def get(self,request):
          r=ComplaintsTable.objects.all()
          return render(request,'administration/complaints.html',{'complaints':r})
     

     
class Replyview(View):
     def post(self,request,id):
          d=ComplaintsTable.objects.get(id=id)
          n=ReplyForm(request.POST,instance=d)
          if n.is_valid():
               n.save()
          return redirect('/complaints')

           
     
class adminhomepage(View):
     def get(self,request):
          return render(request,'administration/adminhomepage.html')     
     
class userregistration(View):
     def get(self,request):
          return render(request,'user/user_registration.html')
     def post(self,request):
          Name=UserForm(request.POST, request.FILES)
          if Name.is_valid():
               reg=Name.save(commit=False)
               Name=LoginTable.objects.create(username=reg.Email,password=request.POST['password'],usertype="user")
               reg.LOGIN = Name
               reg.save()    
               return redirect('/')                         

class userhomepage(View):
    def get(self, request):
        login_id = request.session.get('user_id')

        if not login_id:
            return redirect('/')

        try:
            user = UserTable.objects.get(LOGIN_id=login_id)
        except UserTable.DoesNotExist:
            return redirect('/')

        hour = datetime.now().hour

        if hour < 12:
            greeting = "Good Morning"
        elif hour < 18:
            greeting = "Good Afternoon"
        else:
            greeting = "Good Evening"

        return render(request, 'user/userhomepage.html', {
            'user': user,
            'greeting': greeting
        })
     
class usercomplaints(View):
     def get(self,request):
          return render(request,'user/usercomplaints.html')
     def post(self,request):
          d=UserTable.objects.get(LOGIN__id=request.session['user_id'])
          c=ComplaintsForm(request.POST)
          if c.is_valid():
               reg=c.save(commit=False)
               reg.USER=d
               reg.save()
          return HttpResponse('''<script>alert("send ");window.location='/viewcomplaints'</script>''')
     

          
class viewcomplaints(View):
    def get(self, request):

        # get login_id stored in session
        login_id = request.session.get('user_id')
        if not login_id:
            return redirect('login')

        # fetch the user using LOGIN foreign key
        try:
            user = UserTable.objects.get(LOGIN_id=login_id)
        except UserTable.DoesNotExist:
            return redirect('login')

        # fetch complaints linked to this user
        complaints = ComplaintsTable.objects.filter(USER=user)

        return render(request, 'user/viewcomplaints.html', {'complaints': complaints })

def post(self, request):
        user = UserTable.objects.get(id=request.session['user_id'])
        form = ComplaintsForm(request.POST)

        if form.is_valid():
            reg = form.save(commit=False)
            reg.USER = user
            reg.save()
            return HttpResponse('''<script>alert("Replay send ");window.location='/viewcomplaints'</script>''')
                 
class userfeedback(View):
     def get(self,request):
               return render(request,'user/userfeedback.html')
     
     def post(self,request):
          d=UserTable.objects.get(LOGIN__id=request.session['user_id'])
          c=FeedbackForm(request.POST)
          if c.is_valid():
               reg=c.save(commit=False)
               reg.USER=d
               reg.save()
               return redirect('/viewfeedback')
     
class viewfeedback(View):
     def get(self,request):
          c=FeedbackTable.objects.all()
          return render(request,'user/viewfeedback.html',{'user':c})     


import subprocess
from django.http import JsonResponse

from django.http import HttpResponseRedirect, JsonResponse
from django.views import View
import subprocess
import socket
import time

class StartSignAnimationView(View):
    def get(self, request):
        print("Starting sign animation frontend...")

        project_path = r"C:\Users\USER\Desktop\Project\Hands2Hope\sign_animation"
        frontend_url = "http://localhost:4200/"

        try:
            # Step 1: Check if frontend already running
            if self.is_port_in_use(4200):
                print("Frontend already running.")
                return HttpResponseRedirect(frontend_url)
 
            # Step 2: Start frontend in background
            subprocess.Popen(
                "npm start",
                cwd=project_path,
                shell=True
            )

            # Step 3: Wait for the server to come up (max 45 sec)
            print("Waiting for Angular server to start...")
            for i in range(45):
                if self.is_port_in_use(4200):
                    print("Angular server is up!")
                    return HttpResponseRedirect(frontend_url)
                time.sleep(1)

            # Step 4: Timeout
            print("Timeout: Angular did not start in time.")
            return JsonResponse({
                "status": "starting",
                "message": "Frontend is starting... Try refreshing after a few seconds."
            })

        except Exception as e:
            print("Error starting frontend:", e)
            return JsonResponse({"status": "error", "message": str(e)})

    @staticmethod
    def is_port_in_use(port):
        """Check if a given TCP port is in use (localhost)."""
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            return s.connect_ex(("localhost", port)) == 0

from django.http import StreamingHttpResponse
from Hands2HopeApp.camera import generate_frames

class isl_page(View):
    def get(self,request):
        return render(request, 'user/isl_live.html')

class video_feed(View):
    def get(self,request):
        return StreamingHttpResponse(
            generate_frames(),
            content_type='multipart/x-mixed-replace; boundary=frame'
        )
 

class DeleteUser(View):
     def get(self, request, id):
          c = LoginTable.objects.get(id=id)
          c.delete()
          return redirect('/manage_users')
     
class Profilesview(View):
    def get(self, request):
        user = UserTable.objects.get(LOGIN=request.session['user_id'])
        return render(request, 'user/profile.html', {'user': user})


class editprofile(View):
    def get(self, request):
        user = UserTable.objects.all()
        return render(request, 'user/editprofile.html', {'user': user})
     

class edituser(View):

    def get(self, request, id):
        user = UserTable.objects.get(id=id)
        return render(request, 'user/editprofile.html', {'user': user})

    def post(self, request, id):
        user = UserTable.objects.get(id=id)

        user.Name = request.POST.get('Name')
        user.Age = request.POST.get('Age')
        user.Gender = request.POST.get('Gender')
        user.Email = request.POST.get('Email')
        user.Phone_no = request.POST.get('Phone_no')
        user.Place = request.POST.get('Place')

        user.save()
        # update logintable
        login_obj = user.LOGIN
        login_obj.username = request.POST.get('Email')
        login_obj.save()

        # Redirect to Profilesview page
        return redirect('profile')
    
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.contrib import messages   
class ForgetPassword(View):
    def get(self, request):

        return render(request, 'user/forgot.html')

    def post(self, request):
        email = request.POST.get('Email')

        if  not email:
            messages.error(request, "Both Name and Email are required")
            return redirect('/Forgotpassword')

        # List of user tables to check
        user_tables = [UserTable]

        for table in user_tables:
            try:
                user = table.objects.get(Email=email)
                login_obj = get_object_or_404(LoginTable, id=user.LOGIN.id)

                # Send email (Consider replacing this with a password reset link)
                send_mail(
                    'Password Recovery',
                    f'Your Account Password is: {login_obj.password}',
                    'thatunique23@gmail.com',
                    [email],
                )

                messages.success(request, f'Password sent to {email}')
                return HttpResponse(
                    '''<script> window.location="/";</script>'''
                )

            except table.DoesNotExist:
                continue  # Check the next table

        messages.error(request, "Invalid Email. Please try again")
        return HttpResponse('''<script> window.location="/"</script>''')
    
class signs(View):
    def get(self, request):
        return render(request, "user/signs.html")