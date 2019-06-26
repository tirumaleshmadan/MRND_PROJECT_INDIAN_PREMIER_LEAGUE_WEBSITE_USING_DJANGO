from django.views import View
from cricket.models import Matches
from django.shortcuts import render,redirect
from django.core.paginator import Paginator

def teams_list_sort(teams):
    return teams['points']

class PointsTableView(View):
    def get(self,request,*args,**kwargs):
        match_list = Matches.objects.filter(season=kwargs['year'])
        teams=[]
        teams_list=[]
        for match in match_list:
            teams_list.append(match.team1)
            teams_list.append(match.team2)
        teams_list=list(set(teams_list))
        for team in teams_list:
            single_team=dict()
            single_team['team']=team
            single_team['played']=0
            single_team['won']=0
            single_team['loss']=0
            single_team['tie']=0
            single_team['points']=0
            for match in match_list:
                if(match.team1==team or match.team2==team):
                    single_team['played']=single_team['played']+1
                    if(match.result=='normal' or match.result=='tie'):
                        if(match.winner==team):
                            single_team['won']=single_team['won']+1
                            single_team['points']=single_team['points']+2
                        else:
                            single_team['loss']=single_team['loss']+1
                    elif(match.result=='no result'):
                        single_team['tie']=single_team['tie']+1
                        single_team['points']=single_team['points']+1
            teams.append(single_team)
        teams.sort(reverse=True,key=teams_list_sort)
        year=kwargs['year']
        return render(
            request,
            template_name='points_table.html',
            context={
                'teams':teams,
                'YEAR': year,
                'years': [year for year in range(2019, 2007, -1)],
            }
        )
