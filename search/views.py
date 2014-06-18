from django.shortcuts import render,redirect,render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from search.models import Location,Hourlydata
from search.tables import LocationTable,HourlydataTable
from django_tables2 import RequestConfig
from django_tables2_reports.config import RequestConfigReport as RequestConfig
from django_tables2_reports.utils import create_report_http_response
import time,csv


# Create your views here.
def index(request):
    return HttpResponse('Hello aqi')

def search_form(request):
    return render(request,'search_form.html')

def search_station(request):
    if 'city' in request.GET and request.GET['city']:
        city=request.GET['city'].lower()
        table=LocationTable(Location.objects.filter(parentcity__icontains=city))
        table_to_report=RequestConfig(request).configure(table)
        if table_to_report:
            return create_report_http_response(table_to_report,request)
        return render(request,'search_results.html',
                      {"location":table,"city":city})        
    else:
        return render(request,'search_form.html',{"alert":'Please enter a city.'})
    
def search_aqi(request):
    global table_model
    if ('dt' in request.GET and request.GET['dt']) or ('st' in request.GET and request.GET['st']):
        dt=request.GET['dt']
        st=request.GET['st'][0:1].upper()+request.GET['st'][1:].lower()
        if dt=='':
            table_model=Hourlydata.objects.filter(stationname__icontains=st)
            table=HourlydataTable(table_model)
        elif st=='':
            table_model=Hourlydata.objects.filter(est_time=dt)
            table=HourlydataTable(table_model)
        else:
            table_model=Hourlydata.objects.filter(est_time=dt).filter(stationname__icontains=st)
            table=HourlydataTable(table_model)
        table_to_report=RequestConfig(request).configure(table)
        if table_to_report:
            return create_report_http_response(table_to_report,request)
        return render(request,'search_results.html',
                      {"aqi":table,"dt":dt,"st":st})
    else:
        return render(request,'search_form.html',{"alert":'Please enter a station or a timestamp.'})

def search_aqis(request):    
    global table_model
    if ('dtF' in request.GET and request.GET['dtF']) or ('dtT' in request.GET and request.GET['dtT']) or ('sts' in request.GET and request.GET['sts']):
        dtF=request.GET['dtF']
        dtT=request.GET['dtT']
        sts=request.GET['sts'][0:1].upper()+request.GET['sts'][1:].lower()
        if dtF=='' and dtT=='' :
            table_model=Hourlydata.objects.filter(stationname__icontains=sts)
            table=HourlydataTable(table_model)
        elif sts=='' and dtF=='':
            dtF='20140102000000'
            table_model=Hourlydata.objects.filter(est_time__gte=long(dtF)).filter(est_time__lte=long(dtT))
            table=HourlydataTable(table_model)
        elif sts=='' and dtT=='':
            dtT=time.strftime("%Y%m%d%H0000")
            table_model=Hourlydata.objects.filter(est_time__gte=long(dtF)).filter(est_time__lte=long(dtT))
            table=HourlydataTable(table_model)
        elif dtF=='':
            dtF='20140102000000'
            table_model=Hourlydata.objects.filter(est_time__gte=long(dtF)).filter(est_time__lte=long(dtT)).filter(stationname__icontains=sts)
            table=HourlydataTable(table_model)
        elif dtT=='':
            dtT=time.strftime("%Y%m%d%H0000")
            table_model=Hourlydata.objects.filter(est_time__gte=long(dtF)).filter(est_time__lte=long(dtT)).filter(stationname__icontains=sts)
            table=HourlydataTable(table_model)
        elif sts=='':
            table_model=Hourlydata.objects.filter(est_time__gte=long(dtF)).filter(est_time__lte=long(dtT))
            table=HourlydataTable(table_model)
        else:
            table_model=Hourlydata.objects.filter(est_time__gte=long(dtF)).filter(est_time__lte=long(dtT)).filter(stationname__icontains=sts)
            table=HourlydataTable(table_model)
        table_to_report=RequestConfig(request).configure(table)
        if table_to_report:
            return create_report_http_response(table_to_report,request)
        return render(request,'search_results.html',
                      {"aqis":table,"dtF":dtF,"dtT":dtT,"sts":sts})
    else:
        return render(request,'search_form.html',{"alert":'Please enter a station or a timestamp.'})

## Use django-tables-reports, deprecate exp2csv view.    
#def exp2csv(request):
#    response=HttpResponse(mimetype='text/csv')
#    response['Content-Disposition']='attachment;filename="aqi_export.csv"'
#    
#    writer=csv.writer(response)
#    fields=Hourlydata._meta.fields
#    customisedList=[]
#    fieldList=[]
#    for each in fields:
#        print each.get_attname_column()
#        fieldList.append(each.get_attname_column()[1])
#    writer.writerow(fieldList)
#    
#    for each in table_model:
#        row=[]
#        for field in fields:
#            if type(getattr(each,field.name))<>unicode:
#                row.append(str(getattr(each,field.name)))
#            else:
#                uni=getattr(each,field.name)
#                row.append(uni.encode('utf8'))
#        print row
#        writer.writerow(row)
#    
#    return response
