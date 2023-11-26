from django.db import models

class Owner(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.name
    
    @property
    
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Restaurant(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=20)
    opening_hours = models.TimeField()
    closing_hours = models.TimeField()
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.name
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    prices = models.IntegerField()
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.name
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
        

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Order(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    complete = models.BooleanField(default=False)
    price = models.IntegerField()
    order_date_and_time = models.DateTimeField()
    address = models.TextField()
    payment_method = models.CharField(max_length=255)

    def __str__(self):
        return f"Order #{self.id}"
