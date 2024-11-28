from django.db import models

# Create your models here.
class EmployeeAPI(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=50)
    department=models.CharField(max_length=50)
    salary=models.IntegerField()

    class Meta:
        db_table="Employeeapi"