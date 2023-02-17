from django.db import models

# Create your models here.
class Department(models.Model):
    dep_name=models.CharField(max_length=100)
    dep_descrip=models.TextField()
    img=models.ImageField(upload_to='media/')
    def __str__(self):
        return self.dep_name
class Doctors(models.Model):
    name=models.CharField(max_length=150)
    dep_name=models.ForeignKey(Department,on_delete=models.CASCADE)
    specialzation=models.CharField(max_length=100)
    img=models.ImageField(upload_to='media/')

    def __str__(self):
        return 'Dr.' + self.name + '-('+self.specialzation+')-'
class Booking(models.Model):
    p_name=models.CharField(max_length=100)
    p_number=models.CharField(max_length=100)
    p_email=models.EmailField()
    name=models.ForeignKey(Doctors,on_delete=models.CASCADE)
    booking_date=models.DateField()
    booked_on=models.DateField(auto_now=True)


