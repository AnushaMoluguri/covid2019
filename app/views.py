from django.shortcuts import render
from covid19.settings import covid_19_file
import json

# Create your views here.
def index(request):
    dict_data=json.loads(open(covid_19_file).read())
    states=[x for x in dict_data]
    states.pop(0)
    #print(states)
    return render(request,'index.html',{"data":states})


def open_state(request):
    sname=request.GET.get("state_name")
    #print(sname)
    dict_data=json.loads(open(covid_19_file).read())
    return render(request,"state.html",{"sname":sname,"data":dict_data[sname]})