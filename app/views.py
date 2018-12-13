from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
class Dashboard(TemplateView):
    template_name = "index.html"
    studio_id = '8185'
    def get(self,request):
        print('called get')
        return render(request, self.template_name,{'counts': {'week_count': '0', 'daily_count': '0', 'month_count': 88}})
