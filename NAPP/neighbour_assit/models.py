


from django.db import models

class UserDetail(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    email = models.EmailField()
    query = models.CharField(max_length=200)  # Service type query (e.g. plumber)
    latitude = models.FloatField()
    longitude = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)  # Time when the data was added
    
    def __str__(self):
        return f"{self.name} - {self.query}"
