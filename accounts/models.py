from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
from django.db.models.expressions import Value
# Create your models here.

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     ROLE_CHOICE = (
#         ('S', 'Seller'),
#         ('B', 'Bidder'),
#     )
#     role = models.CharField(max_length=5, choices=ROLE_CHOICE, default=ROLE_CHOICE[1][0])

#     def __str__(self):
#         return self.user.username
