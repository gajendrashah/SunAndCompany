from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.aboutus, name="about"),
    path("contact", views.contactus, name="contact"),
    path("document", views.compDocument, name="document"),
    path("profile", views.companyProfile, name="profile"),
    path("brochure", views.companyBrochure, name="brochure"),
    path("introduction", views.introductionAbout, name="introduction"),
    path("management", views.msgManagement, name="management"),
    path("gallery", views.gallery, name="gallery"),
    path("testimonial", views.testimonial, name="testimonial"),
    path("japan", views.japan, name="japan"),
    path("demand", views.demand, name="demand"),
    path("services", views.allservices, name="services"),
]