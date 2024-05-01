from django.shortcuts import render

def my_view(request):
    menu_items = [
        {'name': 'Button 1', 'url': '#'},
        {'name': 'Button 2', 'url': '#'},
        # ...
    ]
    return render(request, 'base.html', {'menu_items': menu_items})