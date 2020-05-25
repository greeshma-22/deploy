from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,DeleteView,
                                UpdateView)
from . import models


class IndexView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self,**kwargs):
        context  = super().get_context_data(**kwargs)
        context['injectme'] = "Basic Injection!"
        return context


class SchoolListView(ListView):
    model=models.School

class SchoolDetailView(DetailView):
    context_object_name = 'school_details'
    model=models.School
    template_name = 'student_app/school_detail.html'

class SchoolCreateView(CreateView):

    fields=("name","location")
    model=models.School

class SchoolUpdateView(UpdateView):
    fields=("name","location")
    model=models.School

class SchoolDeleteView(DeleteView):
    model=models.School
    success_url=reverse_lazy('student_app:list')

class StudentCreateView(CreateView):
    fields = ("studentName","stuentRegisterNo","studentPhoneNo","studentStandard")
    model=models.Student

class StudentUpdateView(UpdateView):
    fields = ("studentName","stuentRegisterNo","studentPhoneNo","studentStandard")
    model=models.Student

class StudentDeleteView(DeleteView):
    model=models.Student
    success_url=reverse_lazy('student_app:detail')
