import json
from urllib import parse, request as urlrequest

from django.shortcuts import render


def _fetch_json(url):
    """Call the given URL and return parsed JSON data."""
    with urlrequest.urlopen(url, timeout=10) as response:
        return json.load(response)


def _get_weather_for_city(city):
    """Resolve a city name to coordinates and fetch current weather data."""
    if not city:
        return None, "لطفاً نام شهر را وارد کنید."

    geo_url = (
        "https://geocoding-api.open-meteo.com/v1/search?"
        + parse.urlencode({"name": city, "count": 1, "language": "fa", "format": "json"})
    )

    try:
        geo_data = _fetch_json(geo_url)
    except Exception:
        return None, "امکان برقراری ارتباط با سرویس مکان‌یاب وجود ندارد."

    results = geo_data.get("results") or []
    if not results:
        return None, "شهری با این نام پیدا نشد."

    location = results[0]
    latitude = location.get("latitude")
    longitude = location.get("longitude")

    weather_url = (
        "https://api.open-meteo.com/v1/forecast?"
        + parse.urlencode(
            {
                "latitude": latitude,
                "longitude": longitude,
                "current_weather": "true",
                "timezone": "auto",
            }
        )
    )

    try:
        weather_data = _fetch_json(weather_url)
    except Exception:
        return None, "امکان دریافت وضعیت آب‌وهوا وجود ندارد."

    current = weather_data.get("current_weather")
    if not current:
        return None, "اطلاعات فعلی آب‌وهوا در دسترس نیست."

    return (
        {
            "city": location.get("name") or city,
            "country": location.get("country"),
            "temperature": current.get("temperature"),
            "windspeed": current.get("windspeed"),
            "winddirection": current.get("winddirection"),
            "weathercode": current.get("weathercode"),
            "time": current.get("time"),
        },
        None,
    )


def home_view(request):
    city_query = request.GET.get("city", "").strip()
    weather, error = (None, None)

    if city_query:
        weather, error = _get_weather_for_city(city_query)

    context = {
        "query": city_query,
        "weather": weather,
        "error": error,
    }
    return render(request, "weather/home.html", context)
