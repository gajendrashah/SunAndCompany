from django.shortcuts import render

from django.http import HttpResponse
from .models import (imageSlider, sncFeatures, featureItem, about, serviceHeading, services, listProcess, centralProcess, 
                     customSupport, supportList, vacancies, vacanciesWork, clientReview, countryList, japanDocument, documentList,
                     japanAbout)

def index(request):
    slide = imageSlider.objects.all()
    featuredis = sncFeatures.objects.first()
    featureitems = featureItem.objects.all()
    aboutsns = about.objects.first()
    servHead = serviceHeading.objects.first()
    allService = services.objects.all()
    process = listProcess.objects.all()
    ctprocess = centralProcess.objects.first()
    custSupport = customSupport.objects.first()
    listSupport = supportList.objects.all()
    review = clientReview.objects.all()
    allCountry = countryList.objects.all()
    return render(request, "index.html", {'slide': slide, 'featuredis': featuredis, 'featureitems':featureitems,
                                          'aboutsns' : aboutsns, 'servHead': servHead, 'allService': allService, 'process':process,
                                          'ctprocess':ctprocess, 'custSupport': custSupport, 'listSupport':listSupport, 'allreview': review, 
                                          'my_range': range(5), 'allCountry':allCountry  })

def aboutus(request):
    return render(request, "about.html", )
def contactus(request):
    return render(request, "contact.html", )

def allservices(request):
    return render(request, "service.html")
#Document Detail
def compDocument(request):
    docList = documentList.objects.all()
    
    return render(request, "document/companyDocument.html", {'docList':docList, } )
def companyProfile(request):
    return render(request, "document/companyProfile.html", )
def companyBrochure(request):
    return render(request, "document/companyBrochure.html", )

# About Detail 
def introductionAbout(request):
    return render(request, "about/introductionAbout.html", )
def msgManagement(request):
    return render(request, "about/msgManagement.html", )
def gallery(request):
    return render(request, "about/gallery.html", )
def testimonial(request):
    review = clientReview.objects.all()
    return render(request, "about/testimonial.html",{'allreview': review,} )
def japan(request):
    docJapan = japanDocument.objects.all()
    aboutJpn = japanAbout.objects.all()
    alldata = {'docJapan': docJapan, 'aboutJpn': aboutJpn}
    return render(request, "japan.html", alldata  )
def demand(request):
    forlotnumber = vacancies.objects.all()
    alldemand = vacanciesWork.objects.all()
    return render(request, "demand.html",{'lotnumber': forlotnumber, 'alldemand':alldemand } )

