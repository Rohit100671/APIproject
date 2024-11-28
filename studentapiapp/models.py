from django.db import models

# Create your models here.
class StudentAPI(models.Model):
    rno=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=50)
    marks=models.IntegerField()

    class Meta:
        db_table='stdapidata'