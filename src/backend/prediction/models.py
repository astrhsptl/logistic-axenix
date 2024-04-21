from uuid import uuid4

from django.db import models

# class (models.Model):
#     id = models.UUIDField(
#         primary_key=True,
#         db_index=True,
#         default=uuid4,
#         editable=False
#     )

#     def __str__(self):
#         return str()



class BestProduct(models.Model):
    id = models.UUIDField(
        primary_key=True,
        db_index=True,
        default=uuid4,
        editable=False
    )
    name = models.CharField(max_length=128, blank=False, null=False, verbose_name='Название')
    date = models.DateField(auto_now_add=True, null=True)


    def __str__(self) -> str:
        return self.name

class BadProduct(models.Model):
    id = models.UUIDField(
        primary_key=True,
        db_index=True,
        default=uuid4,
        editable=False
    )
    name = models.CharField(max_length=128, blank=False, null=False, verbose_name='Название')
    date = models.DateField(auto_now_add=True, null=True)


    def __str__(self) -> str:
        return self.name

