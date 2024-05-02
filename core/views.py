from django.shortcuts import render

def main(request):
    availabilities = []  # Define the list before the loop
    for i in range(4):
        availability = {
            'date': f'test_{i}',
            'time': f'test_{i}',
            'status': f'test_{i}'
        }
        availabilities.append(availability)
    return render(request, 'index.html', {'availabilities': availabilities})

def create(request):
    return render(request, 'create-account.html')

def profile(request):
    return render(request, 'my-profile.html')
