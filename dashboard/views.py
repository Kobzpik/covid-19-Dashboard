from django.shortcuts import render
import pandas as pd



# Create your views here.

def home(request):
        
        confirmedGlobal=pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv',encoding='utf-8',na_values=None)
        totalCount=confirmedGlobal[confirmedGlobal.columns[5]].sum()
        bardata=confirmedGlobal[['Country/Region',confirmedGlobal.columns[5]]].groupby('Country/Region').sum()
        bardata=bardata.reset_index()
        bardata.columns=['Country/Region','values']
        bardata=bardata.sort_values(by='values',ascending=False)
        countryName=bardata['Country/Region'].values.tolist()
        barVal=bardata['values'].values.tolist()
        context={'totalCount':totalCount,'countryName':countryName,'barVal':barVal}
        return render(request,'index.htm', context)