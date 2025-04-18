# 🧭 Neighbour Assistant Platform (NAP)

A simple and privacy-conscious web app that helps users find nearby services (like electricians, tutors, plumbers, etc.) based on their current or manually entered location.

## 🔍 Overview

The **Neighbour Assistant Platform (NAP)** uses geolocation and Google Maps data via **SerpAPI** to display real-time local service providers. The app collects minimal user information (name, email, and phone number) through a basic form before searching. It's designed with simplicity and responsiveness in mind.

## 🚀 Features

- 📍 **Live Location Access** via browser geolocation
- 🗺️ **Manual Location Input** (if GPS is unavailable)
- 🔎 **Flexible Service Search** (e.g., "doctor", "electrician", etc.)
- 🌙 **Dark/Light Mode** toggle for accessibility
- 📱 **Responsive UI** built with Bootstrap 5.3
- 🛡️ **Privacy Focused** – No login system, only minimal form data
- 🗄️ **User Data Storage** with Django ORM

## 🛠️ Tech Stack

| Component       | Technology            |
|----------------|------------------------|
| Backend         | Django (Python)        |
| Frontend        | HTML, Bootstrap 5.3    |
| API Integration | SerpAPI (Google Maps)  |
| Database        | SQLite (development)   |

## 📦 How It Works

1. User opens the app and submits a form with name, email, phone, and service query.
2. The app fetches user’s GPS coordinates (or manual location).
3. It sends the query and coordinates to SerpAPI.
4. Results are displayed as cards with service details like address, contact, ratings, etc.
5. Option to toggle between dark and light themes.

## 🧩 Django Model

```python
class UserQuery(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    service_query = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)


🛠️ Future Enhancements
User reviews and ratings for services

Login system for advanced tracking

Filters based on distance, rating, etc.

Map integration using Google Maps API

📂 Setup Instructions
Clone the repository:

git clone https://github.com/sidhu-26/Neighbourhood_Assitance_App.git
cd Neighbourhood_Assitance_App
Set up a virtual environment:


python -m venv venv
source venv/bin/activate  # on Windows: venv\Scripts\activate
Install dependencies:


pip install -r requirements.txt
Add your SerpAPI key in the .env or settings file as required.

Run the server:

python manage.py runserver
📧 Developer
Siddaarth P T
📍 Mechanical Engineering, SRM Easwari Engineering College
✉️ siddaarth28@gmail.com

