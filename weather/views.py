from django.shortcuts import render

# Create your views here.

def home_view(request):
    city = request.GET.get("city")
    print(city)  # فقط برای تست

    context = {
        "city": city
    }
    return render(request, "weather/home.html", context)
     

