from django.contrib import admin
from .models import (phoneNo, basicInfo, about, services,listProcess, 
                     latestNews, blogComment, centralProcess, proofJapan, 
                     proofNepal, imageSlider, featureItem, sncFeatures, serviceHeading, 
                     customSupport, supportList, clientReview, vacancies, vacanciesWork, enquiryForm, countryList,
                     japanDocument, japanAbout, japanProcess, documentList)



from django.contrib import admin

admin.site.site_header = "Sun & company Admin Portal"
admin.site.site_title = "Sun & company Admin"
admin.site.index_title = "Welcome to Sun & company Admin Dashboard"



admin.site.register(imageSlider)
admin.site.register(featureItem)
admin.site.register(sncFeatures)
admin.site.register(about)
admin.site.register(serviceHeading)
admin.site.register(services)
admin.site.register(centralProcess)
admin.site.register(listProcess)
admin.site.register(customSupport)
admin.site.register(supportList)
admin.site.register(clientReview)
admin.site.register(proofNepal)
admin.site.register(proofJapan)
admin.site.register(phoneNo)
admin.site.register(basicInfo)
admin.site.register(latestNews)
admin.site.register(blogComment)
admin.site.register(vacancies)
admin.site.register(vacanciesWork)
admin.site.register(enquiryForm)
admin.site.register(countryList)
admin.site.register(japanDocument)
admin.site.register(japanAbout)
admin.site.register(japanProcess)
admin.site.register(documentList)
