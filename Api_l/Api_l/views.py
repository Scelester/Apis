from django.http import HttpResponse
from django.shortcuts import render

def home_api(request):
    initial_domain = request.build_absolute_uri()
    whole_body = """
        <div>All api lists</div>
        <div style='display:flex;flex-direction:column'>
        <a href='/cakeg/cakes' >CakeG > cakesapi </a> 
        <a href='/cakeg/occation' > CakeG > occation </a>
        <a href='/cakeg/addcake' > CakeG add-cake </a>
        <a href='/cakeg/addoccation'> CakeG add-occation </a>
        </div>
    """
    return HttpResponse(whole_body)