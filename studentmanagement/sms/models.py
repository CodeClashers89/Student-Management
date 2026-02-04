from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    Role_Choices = [
        ('Student','Student'),
        ('Faculty','Faculty'),
        ('Admin','Admin'),
    ]
    role = models.CharField(max_length=20, choices=Role_Choices, default='Student')
    institute = models.CharField(max_length=20, default='IITRAM')
    phone_no = models.CharField(max_length = 15, blank = False, null=False)

    def __str__(self):
        return f"{self.username} - {self.role}"
    

#Student models
class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="student_profile")
    enrollemet_no = models.CharField(max_length=11, unique=True , editable=False)
    date_of_birth = models.DateField(blank=False,null=False)
    gender = models.TextField(max_length=10 ,blank=False,null=False, choices = [('MALE' , 'Male'),('FEMALE' , 'Female')] )
    address = models.TextField(blank=False,null=False)
    father_contact_no = models.CharField(max_length=15,blank = False, null =False)
    father_email= models.EmailField(blank=False,null=False)
    branch = models.CharField(blank=False,null=False,choices = [('COMPUTER' , 'Computer') , ('CIVIL', 'Civil'), ('MECHANICAL' , 'Mechanical') ,('ELECTRICAL' ,'Electrical')])
    aadhar_no = models.IntegerField(unique=True,blank=False,null=False)
    is_tfws = models.BooleanField(default = False,blank=False,null=False)
    cast_catogry = models.CharField(choices = [('GEN','Gen'),('OBC','Obc'),('SC','Sc') ,('ST', 'St') ],blank=False,null=False)
    admission_through = models.CharField(max_length=10,choices= [('ACPC','ACPC'),('JOSAA','JOSAA')],blank=False,null=False)
    admission_heads = models.CharField(max_length=40,default='B.Tech',blank=False,null=False)
    level = models.CharField(max_length=50,choices = [('UG','UG'),('PG','PG'),('PHD','PHD')],blank=False,null=False)
    father_name = models.CharField(max_length=50,blank=False,null=False)
    updated_at = models.DateTimeField(auto_now_add=True)
    creadted_at = models.DateTimeField(auto_now=True)
    photo_student = models.ImageField(blank=True,null = True,upload_to='sp/')
    leaving_certificate = models.FileField(upload_to = "lc/",blank=False,null=False)

    def save(self, *args, **kwargs):
        if not self.enrollemet_no:
            last_student = Student.objects.all().order_by('id').last()
            if last_student:
                last_id = int(last_student.enrollemet_no[5:])
                new_id = last_id + 1
            else:
                new_id = 1
            self.enrollemet_no = f'S26IIT{new_id:05d}'
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name} -  {self.enrollemet_no}'
#feculty model


