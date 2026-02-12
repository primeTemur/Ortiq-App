from django.db import models

ORGINAL = "orginal"
SERVICE = "service"
OPTOM = "optom"

STATUS_CHOICES = [
    (ORGINAL, "Orginal"),
    (SERVICE, "Service"),
    (OPTOM, "Optom")
]

INPUT = "input"
OUTPUT = "output"

ORDER = [
    (INPUT, 'input'),
    (OUTPUT, 'output')
]


# Mahsulotlar va 3 ta turdagi narxi
class Food(models.Model):
    name = models.CharField(max_length=255, null=True)
    comment = models.TextField(null=True)
    original_price = models.IntegerField(default=0)
    service_price = models.IntegerField(default=0)
    optom_price = models.IntegerField(default=0)


# Ombordagi mahsulotlar
class Product(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE, null=True)
    amount = models.IntegerField(default=0)
    change_price = models.IntegerField(default=0)  
    all_price = models.IntegerField(default=0)  

    date = models.DateTimeField(auto_now=True)

# Kirim-chiqim tarixi
class History(models.Model):
    name = models.CharField(max_length=250,null=True)

    amount = models.IntegerField(default=0)
    change_price = models.IntegerField(default=0)
    all_price = models.IntegerField(default=0)

    status = models.CharField(max_length=250,null=True)
    order = models.CharField(max_length=250,null=True)

    date = models.DateTimeField(auto_now=True)


# Qarzlar tarixi
class DebtHistory(models.Model):
    fullname = models.CharField(max_length=255)
    all_price = models.IntegerField(null=True)
    date = models.DateTimeField(auto_now=True)

    phone = models.CharField(max_length=50, null=True)
    amount = models.IntegerField(null=True)

    status = models.CharField(max_length=250,null=True)
    name = models.CharField(max_length=250,null=True)


# Foydalanuvchi
class User(models.Model):
    full_name = models.CharField(max_length=250, null=True)
    phone = models.CharField(max_length=50, null=True)
    password = models.CharField(max_length=250, null=True)


# Iste'mol hujjatlari
class Doc(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.TextField(null=True)
    price = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now=True)


class ReturnedProduct(models.Model):
    name = models.CharField(null=True,max_length=255)
    count = models.IntegerField(null=True)
    price = models.IntegerField(null=True)

    