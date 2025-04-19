from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Login(AbstractUser):
    usertype=models.CharField(max_length=50,null=True)
    view_password=models.CharField(max_length=50,null=True)


class Doctor(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    image = models.FileField(null=True, upload_to="profile")
    loginId = models.ForeignKey(Login, on_delete=models.CASCADE, null=True) 
    medical_license_number = models.CharField(max_length=255,null=True)
    specialization=models.CharField(max_length=255,default="")

class Pharmacist(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    image = models.FileField(null=True, upload_to="profile")
    loginId = models.ForeignKey(Login, on_delete=models.CASCADE, null=True) 
    pharmacy_license_number = models.CharField(max_length=255,null=True)
    pharmacy_name = models.CharField(max_length=255,null=True)



class User(models.Model):
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=100, null=True)
    phone = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=300, null=True)
    age = models.CharField(max_length=100,null=True)
    gender = models.CharField(max_length=100,null=True)
    image = models.FileField(null=True, upload_to="profile")
    loginId = models.ForeignKey(Login, on_delete=models.CASCADE, null=True)
    blood_group=models.CharField(max_length=200,null=True) 
    # medical_prblm = models.CharField(max_length=500, null=True)

    
class Medicine(models.Model):
    pid=models.ForeignKey(Pharmacist, on_delete=models.CASCADE, null=True)
    name=models.CharField(max_length=255)
    price=models.IntegerField()
    desc=models.CharField(max_length=255,null=True, blank=True)
    qty=models.IntegerField()
    image = models.FileField(null=True, upload_to="profile")
    date=models.DateField(null=True)
    expiry=models.DateField(null=True)
    side_effects=models.CharField(max_length=255,null=True)
    orginal_Price=models.IntegerField(null=True)




class Appointments(models.Model):
    date=models.DateField()
    time=models.TimeField()
    desc=models.CharField(max_length=255,null=True, blank=True)
    status=models.CharField(max_length=255,null=True, blank=True)
    did=models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True)
    uid=models.ForeignKey(User, on_delete=models.CASCADE, null=True)    




class Prescription(models.Model):
    uid=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    pharmacist = models.ForeignKey(Pharmacist, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    medicines = models.CharField(max_length=100,null=True) 
    instructions = models.CharField(max_length=100,null=True) 



class MedicineOrder(models.Model):
    Pharmacist = models.ForeignKey(Pharmacist, on_delete=models.CASCADE, null=True)
    uid = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    mid = models.ForeignKey(Medicine, on_delete=models.CASCADE, null=True)
    date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=50, default='in_cart')
    qty = models.IntegerField(null=True)
    total = models.IntegerField(null=True)
    profit = models.IntegerField(null=True, blank=True)  # New field for profit tracking

def save(self, *args, **kwargs):
        if self.mid and self.qty:
            # Calculate profit
            self.profit = (self.mid.price - self.mid.orginal_Price) * self.qty
        super(MedicineOrder, self).save(*args, **kwargs)



class Invoice(models.Model):
    invoice_no = models.CharField(max_length=20, unique=True, blank=True, null=True)
    pharmacist = models.ForeignKey(Pharmacist, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    medicine_order = models.ForeignKey(MedicineOrder, on_delete=models.CASCADE, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

   
   