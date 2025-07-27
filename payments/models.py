from django.db import models
from django.conf import settings

# Create your models here.

class Transaction(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='transactions')
    amount = models.PositiveIntegerField()
    transaction_type = models.CharField(max_length=10, choices=[
        ('recharge', 'Recharge'),
        ('deduct', 'Deduct'),
        ('bonus', 'Signup Bonus')
    ])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"[{self.transaction_type}] {self.user.username} : {self.amount}"