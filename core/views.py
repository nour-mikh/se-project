from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from .models import UserProfile
from django.contrib import messages
from .models import Interview, Booking

def main(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            print("login successfull")
            login(request, user)
            return redirect('home')  
        else:
            print("failed to login: ", request)
            messages.error(request, 'Invalid username or password')
    
    return render(request, 'index.html')

def create(request):
    print("alo alo 1")
    if request.method == 'POST':
        print("alo alo")
        # Get data from the form
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password1')  # Assuming both passwords are the same
        gender = request.POST.get('gender')
        mobile_number = request.POST.get('mobile_number')
        date_of_birth = request.POST.get('date_of_birth')
        image = request.FILES.get('image')

        # Create a new User object
        user = User.objects.create_user(username=username, email=email, password=password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        # Create a new UserProfile object
        user_profile = UserProfile.objects.create(
            user=user,
            mobile_number=mobile_number,
            gender=gender,
            date_of_birth=date_of_birth,
            # If you want to include image, uncomment the line below
            # image=image
        )

        print('User and UserProfile created successfully!')
        return render(request, 'home.html')
    return render(request, 'create-account.html')

def profile(request):
    user = request.user
    user_bookings = Booking.objects.filter(Q(interviewer=user) | Q(interviewee=user))
    return render(request, 'my-profile.html', {'user': user, 'user_bookings': user_bookings})

def bookings(request):
    return render(request, 'bookings.html')

def statistics(request):
    return render(request, 'statistics.html')

def host(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        time = request.POST.get('time')
        category = request.POST.get('category')
        price = request.POST.get('price')

        # Create a new Interview object with the submitted data
        interview = Interview.objects.create(
            interviewer=request.user,
            interview_date=date,
            interview_time=time,
            category=category,
            price=price
        )
        print('Interview created successfully!')
        return redirect('home.html')
    print("No interview getting created")
    return render(request,'host.html')

def book(request):
    if request.method == 'POST':
        interview_id = request.POST.get('interview_id')
        # Retrieve the interview object
        interview = Interview.objects.get(pk=interview_id)
        
        # Create the Booking object
        booking = Booking.objects.create(
            interview=interview,
            interviewer=interview.interviewer,
            interviewee=request.user,
        )
        print('Booking created successfully!')
    return render(request, 'booked.html')

def feedback(request):
    return render(request,'feedback.html')

def home(request):
    interviews = Interview.objects.all()
    return render(request, 'home.html', {'interviews': interviews})

#view function for submitting the host interview inputs 
def host_interview_form(request):
    if request.method == 'POST':
        category = request.POST.get("category")
        date = request.POST.get("date")
        time = request.POST.get("time")
        price = request.POST.get("price")
        print(category, " ",date," ",time," ",price)
    return render(request,'home.html')

def feedback_form(request):
#TODO: Implement the feedback form
    return render(request,'home.html')


def logout(request):
    logout(request)
    return(request, 'home.html')
