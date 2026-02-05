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
    subject_list = [
        ('Computer Programming','CP'),
        ('Machine Learning', 'ML'),
        ('Data Science','DS'),
        ('App Developement','AP'),
        ('Web Developement','WD'),
    ]
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="student_profile")
    enrollemet_no = models.CharField(max_length=11, unique=True , editable=False)
    subjects = models.CharField(max_length=50,choices=subject_list,blank=False,null=False)
    date_of_birth = models.DateField(blank=False,null=False)
    gender = models.TextField(max_length=10 ,blank=False,null=False, choices = [('MALE' , 'Male'),('FEMALE' , 'Female')] )
    address = models.TextField(blank=False,null=False)
    father_contact_no = models.CharField(max_length=15,blank = False, null =False)
    father_email= models.EmailField(blank=False,null=False)
    branch = models.CharField(max_length=15,blank=False,null=False,choices = [('COMPUTER' , 'Computer') , ('CIVIL', 'Civil'), ('MECHANICAL' , 'Mechanical') ,('ELECTRICAL' ,'Electrical')])
    aadhar_no = models.IntegerField(unique=True,blank=False,null=False)
    is_tfws = models.BooleanField(default = False,blank=False,null=False)
    cast_catogry = models.CharField(max_length=4,choices = [('GEN','Gen'),('OBC','Obc'),('SC','Sc') ,('ST', 'St') ],blank=False,null=False)
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

class Faculty(models.Model):
    subject_list = [
        ('Computer Programming','CP'),
        ('Machine Learning', 'ML'),
        ('Data Science','DS'),
        ('App Developement','AP'),
        ('Web Developement','WD'),
    ]
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="faculty_profile")
    subjects = models.CharField(max_length=50,choices=subject_list,blank=False,null=False)
    salary = models.IntegerField(blank=False,null=False)
    faculty_id = models.CharField(max_length=11, unique=True , editable=False)
    gender = models.TextField(max_length=10 ,blank=False,null=False, choices = [('MALE' , 'Male'),('FEMALE' , 'Female')] )
    address = models.TextField(blank=False,null=False)
    aadhar_no = models.IntegerField(unique=True,blank=False,null=False)
    date_of_birth = models.DateField(blank=False,null=False)
    graduation_level = models.CharField(max_length=50,choices = [('UG','UG'),('PG','PG'),('PHD','PHD')],blank=False,null=False)
    photo_faculty = models.ImageField(blank=True,null = True,upload_to='pf/')
    updated_at = models.DateTimeField(auto_now_add=True)
    creadted_at = models.DateTimeField(auto_now=True)
    department = models.CharField(max_length=15,null=False,blank=False,choices=[('COMPUTER' , 'Computer') , ('CIVIL', 'Civil'), ('MECHANICAL' , 'Mechanical') ,('ELECTRICAL' ,'Electrical')])

    def save(self, *args, **kwargs):
        if not self.faculty_id:
            last_faculty = Faculty.objects.all().order_by('id').last()
            if last_faculty:
                last_id = int(last_faculty.faculty_id[5:])
                new_id = last_id + 1
            else:
                new_id = 1
            self.faculty_id = f'F26IIT{new_id:05d}'
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name} -  {self.faculty_id}'
    
#Test and Exam Models
class TestExam(models.Model):
    creator = models.ForeignKey(Faculty, on_delete=models.CASCADE,related_name='test_creator')
    en_student = models.ForeignKey(Student,related_name='enrolled_student')
    department = models.CharField(choices=[('COMPUTER' , 'Computer') , ('CIVIL', 'Civil'), ('MECHANICAL' , 'Mechanical') ,('ELECTRICAL' ,'Electrical')], null=False, blank=False)
    test_date = models.DateTimeField()
    syllabus = models.TextField(blank = False, null=False)
    total_marks = models.IntegerField(null=False, blank=False)
    duration = models.IntegerField(null=False, blank=False)
    te_type = models.CharField(choices=[('Test', 'test'),('Exam', 'exam')], null=False, blank=False,max_length=5,verbose_name='type')
    test_id = models.IntegerField(null=False, blank=False)
    


    def save(self, *args, **kwargs):
        if not self.test_id:
            last_test = TestExam.objects.all().order_by('id').last()
            if last_test:
                last_id = int(last_test.test_id)
                new_id = last_id + 1
            else:
                new_id = 1
            self.test_id = f'{new_id:05d}'
        super().save(*args, **kwargs)

    def get_subjects(self):
        return Faculty.objects.fiter(
            te_fsubjects = self.creator.subjects,
        )

    def get_students(self):

        return Student.objects.filter(
            department = self.department,
            te_ssubjects = self.en_student.o
        )
    
