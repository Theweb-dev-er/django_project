from django.shortcuts import render
from django.http import HttpResponse
from query_builder.models import year_class

def insert(request):
    
    # member1 = year_class(class_year='first', stream='civil')
    # member2 = year_class(class_year='second', stream='civil')
    # member3 = year_class(class_year='third', stream='civil')
   
    # members_list = [member1, member2, member3]
    # for x in members_list:
    #     x.save()
        
    data = year_class(class_year='first', stream='extc')
    data.save()  
       
    return HttpResponse('welcome')

# Create your views here.
