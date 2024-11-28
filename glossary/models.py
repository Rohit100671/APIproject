from django.db import models

# Create your models here.
class Glossary(models.Model):
    sr=models.IntegerField(primary_key=True)
    items=models.CharField(max_length=50)
    quantity=models.IntegerField()
    price=models.IntegerField()

    class Meata:
        db_table="glossary_glossary"