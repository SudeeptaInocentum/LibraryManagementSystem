from django.db import models

class Building(models.Model):
    name = models.CharField(max_length=50) 
    description = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    floor_Count = models.IntegerField()
    
    def __self__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    floor = models.IntegerField()
    code = models.CharField(max_length=20)
    building_id = models.ForeignKey(Building, default=1, on_delete=models.CASCADE)

    def __self__(self):
        return self.name

class Section(models.Model):
    name = models.CharField(max_length=20)  
    description = models.CharField(max_length=50)
    self_number = models.IntegerField()
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __self__(self):
        return self.name

class Books(models.Model):
    bar_code = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    writer = models.CharField(max_length=20)
    description = models.CharField(max_length=50)
    availabile = models.IntegerField()
    location = models.ForeignKey(Section, on_delete=models.CASCADE)

    def __self__(self):
        return self.name

class Admin(models.Model):
    designation = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=15)

class User(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=12)
    email = models.CharField(max_length=25)
    joining_date = models.DateField()

class Issuence(models.Model):
    member_id = models.ForeignKey(User, on_delete=models.PROTECT)
    Admin_id = models.ForeignKey(Admin, on_delete=models.PROTECT)
    issued_book_id = models.ForeignKey(Books, on_delete=models.PROTECT)
    issue_date = models.DateField()
    retuen_date = models.DateField()
    status = models.CharField(max_length=20)