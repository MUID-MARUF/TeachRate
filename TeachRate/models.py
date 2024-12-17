from django.db import models

class Signup(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    confirm_password = models.CharField(max_length=100)

    def __str__(self):
        return self.name

from django.db import models

class University(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=255)
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    designation = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='teacher_pictures/', null=True, blank=True)
    
    def get_average_rating(self):
        ratings = self.ratings.all()
        if ratings.exists():
            return round(sum(rating.rating for rating in ratings) / ratings.count(), 2)
        return 0
    
    def __str__(self):
        return self.name


class Rating(models.Model):
    teacher = models.ForeignKey(Teacher, related_name='ratings', on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, f'{i} Star') for i in range(1, 6)])

    def __str__(self):
        return f'{self.teacher.name} - {self.rating} Star'
    
    



