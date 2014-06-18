# aqi/search/tables.py
import django_tables2 as tables
from django_tables2_reports.tables import TableReport
from search.models import Location,Hourlydata

class LocationTable(TableReport):
    locationid = tables.Column(verbose_name="Location ID")
    latitude=tables.Column(verbose_name="Latitude")
    longitude=tables.Column(verbose_name="Longitude")
    stationname=tables.Column(verbose_name="Station")
    parentcity = tables.Column(verbose_name="Parent City")
    
    class Meta:
        model=Location
        attrs={"class":"paleblue"}
        exclude=("sourceurl",)

class HourlydataTable(TableReport):
    locationid=tables.Column(verbose_name="Location ID")
    stationname=tables.Column(verbose_name="Station")
    chinesename=tables.Column(verbose_name="Chinese Name")
    latitude=tables.Column(verbose_name="Latitude")
    longitude=tables.Column(verbose_name="Longitude")
    pm25=tables.Column(verbose_name="PM2.5 mcg/m"+u"\u00B3")
    pm10=tables.Column(verbose_name="PM10 mcg/m"+u"\u00B3")
    o3=tables.Column(verbose_name="O3 pphm")
    no2=tables.Column(verbose_name="NO2 pphm")
    so2=tables.Column(verbose_name="SO2 pphm")
    co=tables.Column(verbose_name="CO ppm")
    temperature=tables.Column(verbose_name="Temp "+u"\u2103")
    dewpoint=tables.Column(verbose_name="Dew Point "+u"\u2103")
    pressure=tables.Column(verbose_name="Pressure Pa")
    humidity=tables.Column(verbose_name="Humidity %")
    wind=tables.Column(verbose_name="Wind m/s")
    est_time=tables.Column(verbose_name="UTC Time yyMMddHHmmss")
    
    class Meta:
        model=Hourlydata
        attrs={"class":"paleblue"}
        exclude=("rowid","unix_time")

