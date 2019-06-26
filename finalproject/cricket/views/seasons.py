from django.views import View
from cricket.models import Matches
from django.shortcuts import render,redirect
from django.core.paginator import Paginator

class SeasonView(View):
    def get(self,request,*args,**kwargs):
        if kwargs:
            match_list = Matches.objects.filter(season=kwargs['year'])
            pages=Paginator(match_list, 8)
            year=kwargs['year']
        else:
            match_list = Matches.objects.filter(season=2019)
            pages = Paginator(match_list, 8)
            year=2019

        next_page=kwargs['page']+1
        prev_page=kwargs['page']-1
        if(prev_page==0):
            prev_page=1
        if(next_page==pages.num_pages+1):
            next_page=pages.num_pages

        return render(
            request,
            template_name='home.html',
            context={
                'pages': pages.page(kwargs['page']),
                'page_count':pages.num_pages,
                'page_no':kwargs['page'],
                'next':next_page,
                'prev':prev_page,
                'page_list':[i for i in range(1,pages.num_pages+1)],
                'YEAR': year,
                'years': [year for year in range(2019, 2007, -1)],
            }
        )
