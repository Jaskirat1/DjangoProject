from msilib.schema import ListView
#from pyexpat import model
from urllib import request
from django.shortcuts import render
#from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from TODO.models import Student
#from .forms import StudentForm
from django.views import generic
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView, DeleteView


class StudentCreate(CreateView):
    model = Student
    fields = '__all__'
    success_url= '/list'

class StudentListView(ListView):
    template_name ='student_list.html'
    model = Student
    
    def get_queryset(self):
        qs = Student.objects.all()
        return qs


class StudentDetailView(DetailView):
    model= Student
    template_name = 'student_detail.html'

class StudentUpdateView(UpdateView):
    model = Student
    template_name= 'student_form.html'
    fields = '__all__'
    success_url = '/list'

class StudentDeleteView(DeleteView):
    model = Student
    template_name= 'student_delete.html'
    success_url = '/list'


"""
    def StudentDetailView(request):  
        student = Student.objects.all()  
        return render(request,"student_detail.html",{'Student': student}) 
"""


    




    
