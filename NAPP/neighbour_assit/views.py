

import requests
from django.shortcuts import render
from .models import UserDetail

def home(request):
    return render(request, "home.html")

def search_results(request):
    if request.method == "POST":
        # User Details
        name = request.POST.get("name")
        mobile = request.POST.get("mobile")
        email = request.POST.get("email")
        
        # Service and Location Details
        query = request.POST.get("query")
        latitude = request.POST.get("latitude")
        longitude = request.POST.get("longitude")

        # Validate user details
        if not name or not mobile or not email:
            return render(request, "home.html", {
                "error": "All fields (Name, Mobile, Email) are required."
            })
        
        # Basic error fallback for location
        if not latitude or not longitude:
            return render(request, "results.html", {
                "error": "Location access denied. Please allow GPS access or enter location manually."
            })

        # Save the user details in the database
        user_detail = UserDetail.objects.create(
            name=name,
            mobile=mobile,
            email=email,
            query=query,
            latitude=latitude,
            longitude=longitude
        )

    # Your SERP API key and URL
    SERP_API_KEY = ''
    url = 'https://serpapi.com/search.json'

    # SERP API request parameters
    params = {
            "engine": "google_maps",
            "q": query,
            "ll": f"@{latitude},{longitude},15z",  # 15z is zoom level
            "type": "search",
            "api_key": SERP_API_KEY
        }

    # Making the request to the SERP API
    response = requests.get(url, params=params)
    data = response.json()

    # Parse places from the response data
    places = []
    for result in data.get('local_results', []):
        places.append({
            'name': result.get('title'),
            'address': result.get('address'),
            'phone': result.get('phone', 'Mobile number not available'),
            'website': result.get('website'),
            'rating': result.get('rating', 0.0)
        })

    return render(request, "results.html", {'results': places})
