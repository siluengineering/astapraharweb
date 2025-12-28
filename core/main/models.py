from django.db import models

class Membership(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    plan = models.CharField(max_length=50, choices=[('basic', 'Basic'), ('premium', 'Premium')])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name