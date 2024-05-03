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
    return render(request,'home.html')