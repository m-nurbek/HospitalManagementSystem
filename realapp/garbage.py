department= models.CharField(max_length=50,choices=departments,default='Cardiologist')
#department_id = model.CharField(maxlength = 9)
specialization_id = models.CharField(max_length = 9)
experience = models.CharField(max_length = 2)
#profile_pic= models.ImageField(upload_to='profile_pic/DoctorProfilePic/',null=True,blank=True)
category = models.CharField(max_length=9, choices=categories, default='Highest')

price = models.CharField(max_length = 4,null=True)


degree_ed = models.CharField(max_length=25, choices=degrees, default='MD in Medicine')

rating = models.CharField(max_length = 2,null=True)

address = models.CharField(max_length=40,null=True)


status=models.BooleanField(default=False)
