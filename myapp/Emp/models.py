from django.db import models

# Create your models here.
class Emp(models.Model):
    name=models.CharField(max_length=20)
    emp_id=models.CharField(max_length=10)
    phone=models.CharField(max_length=10)
    address=models.CharField(max_length=60)
    working=models.BooleanField(default=True)
    department=models.CharField(max_length=20)

    def __str__(self):
        return self.name

#Testimonial app
class Testimonial(models.Model):
    name=models.CharField(max_length=60)
    testimonials=models.TextField()
    picture=models.ImageField(upload_to="testimonials/")
    RATING_CHOICES = [(i, str(i)) for i in range(1,6)]
    rating=models.PositiveSmallIntegerField(
        choices=RATING_CHOICES, default=5
    )

    def __str__(self):
        return self.testimonials
    

