from django.db import models
import uuid
from usermanage.models import BaseModel, Customer

# Create your models here.

class Comment(BaseModel):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    message = models.TextField(null=False, blank=False)