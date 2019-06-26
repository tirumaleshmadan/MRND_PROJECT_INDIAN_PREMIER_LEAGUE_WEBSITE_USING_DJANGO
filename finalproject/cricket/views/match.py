from django.views import View
from cricket.models import Matches,Deliveries
from django.shortcuts import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum,Count,Q

class MatchDetailsView(LoginRequiredMixin,View):
    login_url = '/login/'
    def get(self,request,*args,**kwargs):
        match = Matches.objects.get(match_id=kwargs['match_id'])
        year=kwargs['year']
        deliveries_inning_1 = Deliveries.objects.filter(match_id=match.match_id, inning=1)
        deliveries_inning_2 = Deliveries.objects.filter(match_id=match.match_id, inning=2)
        batting = deliveries_inning_1[0].batting_team
        bowling = deliveries_inning_1[0].bowling_team
        if kwargs['choice']==3:
            top_batsmen_inning_1=Deliveries.objects.filter(match_id=kwargs['match_id'],inning=1).values('batsman').annotate(runs=Sum('batsman_runs')).order_by('-runs')
            top_batsmen_inning_2=Deliveries.objects.filter(match_id=kwargs['match_id'],inning=2).values('batsman').annotate(runs=Sum('batsman_runs')).order_by('-runs')
            top_bowlers_inning_1=Deliveries.objects.filter(Q(match_id=kwargs['match_id'],inning=1),~Q(dismissal_kind="runout"),~Q(dismissal_kind="")).values('bowler').annotate(wickets=Count('bowler')).order_by('-wickets')
            top_bowlers_inning_2=Deliveries.objects.filter(Q(match_id=kwargs['match_id'],inning=2),~Q(dismissal_kind="runout"),~Q(dismissal_kind="")).values('bowler').annotate(wickets=Count('bowler')).order_by('-wickets')
            return render(
                request,
                template_name='match.html',
                context={
                    'match': match,
                    'YEAR': year,
                    'batting': batting,
                    'bowling': bowling,
                    'choice': kwargs['choice'],
                    'page': kwargs['page'],
                    'top_batsmen_inning_1': top_batsmen_inning_1[:3],
                    'top_batsmen_inning_2': top_batsmen_inning_2[:3],
                    'top_bowlers_inning_1': top_bowlers_inning_1[:3],
                    'top_bowlers_inning_2': top_bowlers_inning_2[:3],
                }
            )
        else:
            if(kwargs['choice']==1):
                deliveries=deliveries_inning_1
            else:
                deliveries=deliveries_inning_2
        return render(
            request,
            template_name='match.html',
            context={
                'match': match,
                'YEAR': year,
                'batting':batting,
                'bowling':bowling,
                'choice':kwargs['choice'],
                'page':kwargs['page'],
                'deliveries':deliveries,
            }
        )

