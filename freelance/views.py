from django.shortcuts import render

# index view
def index(request):
    # Return index.html
    return render(request, "freelance/index.html")
