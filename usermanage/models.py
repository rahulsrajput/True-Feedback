from django.db import models
import uuid
from django.contrib.auth.models import User

# Create your models here.
class BaseModel(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Customer(BaseModel):
    user = models.OneToOneField(User, blank=False, null=False, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)