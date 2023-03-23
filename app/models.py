from django.db import models

# Create your models here.


class Province(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class District(models.Model):
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Local(models.Model):
    province = models.ForeignKey(Province,on_delete=models.CASCADE)
    district = models.ForeignKey(District,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class Project(models.Model):
    province = models.ForeignKey(Province,on_delete=models.CASCADE)
    district = models.ForeignKey(District,on_delete=models.CASCADE)
    local = models.ForeignKey(Local, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name 
