from django.shortcuts import render

def main(request):
    availabilities = []  # Define the list before the loop
    for i in range(4):
        availability = {
            'category': f'test_{i}',
            'date': f'test_{i}',
            'time': f'test_{i}',
            'price': f'test_{i}'
        }
        availabilities.append(availability)
    return render(request, 'index.html', {'availabilities': availabilities})

def create(request):
    return render(request, 'create-account.html')

def profile(request):
    return render(request, 'my-profile.html')

def bookings(request):
    return render(request, 'bookings.html')

def statistics(request):
    return render(request, 'statistics.html')

def host(request):
    return render(request,'host.html')

def feedback(request):
    return render(request,'feedback.html')

def home(request):
    availabilities = [] 
    for i in range(4):
        availability = {
            'category': f'test_{i}',
            'date': f'test_{i}',
            'time': f'test_{i}',
            'price': f'test_{i}'
        }
        availabilities.append(availability)
    return render(request, 'home.html', {'availabilities': availabilities})

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
    if request.method == 'POST':
        booking_ID = request.POST.get("booking_id")
        com_skills = request.POST.get("com_skills")
        professionalism = request.POST.get("professionalism")
        adaptability = request.POST.get("adaptability")
        preparation = request.POST.get("preparation")
        competency = request.POST.get("competency")
        time_mgt = request.POST.get("time_mgt")
        effectiveness = request.POST.get("effectiveness")
    return render(request,'home.html')

def create_account_form(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        email = request.POST.get("email")
        gender = request.POST.get("gender")
        password = request.POST.get("password")
    return render(request,'home.html')

def login_form(request):
    if request.method == 'POST':
        email = request.POST.get("email")
        password = request.POST.get("password")
    return render(request,'home.html')
