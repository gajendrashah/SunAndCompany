from django.db import models
from ckeditor.fields import RichTextField

class imageSlider(models.Model):
    imageup = models.ImageField(upload_to='sayImag', null=True)
    title = models.CharField(max_length=200)
    sub_title = models.CharField(max_length=200)
    def __str__(self):
        return self.title
    
class featureItem(models.Model):
    title_feature = models.CharField(max_length=200)
    description_feature = models.CharField(max_length=200)
    def __str__(self):
        return self.title_feature
class sncFeatures (models.Model):
    short_description = models.CharField(max_length=200)
    feature_image = models.ImageField(upload_to='featureimage')
    def __str__(self):
        return self.short_description
    
class about(models.Model):
    aboutdetail = models.TextField()
    mission = models.TextField()
    vision = models.TextField()
    objectiveabout = models.TextField()
    msgFounder  = models.TextField()
    bulletPoint = models.TextField()
    yrexperiance = models.IntegerField()
    founderName = models.CharField(max_length=200)
    founderimage = models.ImageField(upload_to='founder')
    firstimage = models.ImageField(upload_to='aboutone')
    secondimage = models.ImageField(upload_to='abouttwo')
    def __str__(self):
        return self.aboutdetail

class serviceHeading(models.Model):
    shortDescription = models.TextField()
    serviceHeadImage = models.ImageField(upload_to='servicehead')
    def __str__(self):
        return self.shortDescription 
    
class services(models.Model):
    titleService = models.CharField(max_length=200)
    serviceDescription = models.TextField()
    serviceTitleImage = models.ImageField(upload_to='serviceImage')
    def __str__(self):
        return self.titleService  
    
class centralProcess (models.Model):
    shotrDescription = models.TextField()
    def __str__(self):
        return self.shotrDescription
    
class listProcess (models.Model):
    titleProcess = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    def __str__(self):
        return self.titleProcess

class customSupport(models.Model):
    titleDesc = models.TextField()
    def __str__(self):
        return self.titleDesc
class supportList(models.Model):
    userSupport = models.ImageField(upload_to='Support_image')
    userName = models.CharField(max_length=200)
    userProfession = models.CharField(max_length=200)
    userFacebook = models.URLField()
    userInstagram = models.URLField()
    def __str__(self):
        return self.userName

class clientReview (models.Model):
    reviewName = models.CharField(max_length=200)
    reviewImage = models.ImageField(upload_to="reviewimage")
    reviewProfession = models.CharField(max_length=200)
    reviewReview= models.TextField()
    reviewStart = models.IntegerField()
    def __str__(self):
        return self.reviewName

class proofNepal(models.Model):
    docTitle = models.CharField(max_length=200)
    docDesc = models.CharField(max_length=200)
    docImage = models.ImageField(upload_to='proofImageNepal', null=True)
    def __str__(self):
        return self.docTitle
    
class proofJapan(models.Model):
    docTitle = models.CharField(max_length=200)
    docDesc = models.CharField(max_length=200)
    docImage = models.ImageField(upload_to='proofImageJapan', null=True)
    def __str__(self):
        return self.docTitle
    
       
class phoneNo (models.Model):
    number = models.IntegerField()
    def __str__(self):
        return self.number
        
class basicInfo(models.Model):
    comp_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    email = models.EmailField()
    contact = models.ForeignKey(phoneNo, on_delete=models.CASCADE)
    def __str__(self):
        return self.comp_name
    

class latestNews(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    datetime = models.DateTimeField(auto_now=True)
    blogImg = models.ImageField(upload_to='blogImage')
    def __str__(self):
        return self.title
    
class blogComment(models.Model):
    username = models.CharField(max_length=200)
    commentBlog = models.CharField(max_length=200)
    rateBlog = models.IntegerField()
    def __str__(self):
        return self.username

class vacancies(models.Model):
    vacanciesImage = models.ImageField(upload_to='vacancy')
    countryName = models.CharField(max_length=200) 
    interviewLocation = models.TextField()
    lotNo = models.IntegerField()
    approvalDate = models.DateField()
    def __str__(self):
        return self.countryName

class vacanciesWork(models.Model):
    vacanciesSlect = models.ForeignKey(vacancies, on_delete=models.CASCADE)
    position = models.CharField(max_length=200)
    noOfVacancyMale = models.IntegerField()
    noOfVacancyFemale = models.IntegerField()
    salery = models.IntegerField()
    food  = models.BooleanField()
    accomodation = models.BooleanField()
    transportaion = models.BooleanField()
    overtime = models.CharField(max_length=200)
    def __str__(self):
        return self.position

class enquiryForm(models.Model):
    enquiryName = models.CharField(max_length=200)
    enquiryEmail = models.EmailField()
    enquiryPhone = models.IntegerField()
    enquiryProfession = models.CharField(max_length=200)
    enquirySubject = models.CharField(max_length=300)
    enquiryMessage = models.TextField()
    def __str__(self):
        return self.enquiryName
class countryList(models.Model):
    imageCountry = models.ImageField(upload_to='contList')
    nameCountry = models.CharField(max_length=200)
    def __str__(self):
        return self.nameCountry

class japanDocument(models.Model):
    certificationJapan = models.ImageField(upload_to='japanDoc')
    japanDocName = models.CharField(max_length=100)
    def __str__(self):
        return self.japanDocName
class japanAbout(models.Model):
    aboutJapan = RichTextField(blank=True, null=True)
    aboutjapanImg = models.ImageField(upload_to='japanAboutimg')
    
class japanProcess(models.Model):
    japanProcessImg = models.ImageField(upload_to='jpnPro')
    japanProcessDetail = RichTextField(blank=True, null=True)
    def __str__(self):
        return self.japanProcessDetail

class documentList(models.Model):
    uploadDocument = models.ImageField(upload_to='docimg')
    docName = models.CharField(max_length=200)
    def __str__(self):
        return self.docName