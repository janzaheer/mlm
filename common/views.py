from django.views.generic import TemplateView
from django.contrib.auth.models import User

from .models import Partner

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context.update({
            'users': User.objects.all().order_by('username'),
            'user_kw': User.objects.get(id=self.request.GET.get('user_id', 1)).username.title()
        })

        # Level One
        level_one = Partner.objects.filter(user__id=self.request.GET.get('user_id', 1))
        if level_one:
            try:
                partner_one_left = level_one.get(position=Partner.POSITION_LEFT)
            except:
                partner_one_left = None
            try:
                partner_one_right = level_one.get(position=Partner.POSITION_RIGHT)
            except:
                partner_one_right = None
        else:
            level_one = None
            partner_one_left = None
            partner_one_right = None
        
        context.update({
            'level_one': level_one[0] if level_one else None,
            'partner_one_left': partner_one_left,
            'partner_one_right': partner_one_right
        })
        
        if partner_one_left:
            try:
                level_two_a = Partner.objects.filter(user__id=partner_one_left.partner_user.id)
            except:
                level_two_a = None
            
            try:
                partner_two_a_left = level_two_a.get(position=Partner.POSITION_LEFT)
            except:
                partner_two_a_left = None
            try:
                partner_two_a_right = level_two_a.get(position=Partner.POSITION_RIGHT)
            except:
                partner_two_a_right = None
        else:
            level_two_a = None
            partner_two_a_left = None
            partner_two_a_right = None

        context.update({
            'level_two_a': level_two_a[0] if level_two_a else None,
            'partner_two_a_left': partner_two_a_left,
            'partner_two_a_right': partner_two_a_right,
        })

        # Level Two Right
        if partner_one_right:
            try:
                level_two_b = Partner.objects.filter(user__id=partner_one_right.partner_user.id)
            except:
                level_two_b = None
            
            try:
                partner_two_b_left = level_two_b.get(position=Partner.POSITION_LEFT)
            except:
                partner_two_b_left = None
            try:
                partner_two_b_right = level_two_b.get(position=Partner.POSITION_RIGHT)
            except:
                partner_two_b_right = None
        else:
            level_two_b = None
            partner_two_b_left = None
            partner_two_b_right = None

        context.update({
            'level_two_b': level_two_b[0] if level_two_b else None,
            'partner_two_b_left': partner_two_b_left,
            'partner_two_b_right': partner_two_b_right,
        })

        # Level Three Left A
        if partner_two_a_left:
            try:
                level_three_a = Partner.objects.filter(user__id=partner_two_a_left.partner_user.id)
            except:
                level_three_a = None
            
            try:
                partner_three_left_a_left = level_three_a.get(position=Partner.POSITION_LEFT)
            except:
                partner_three_left_a_left = None
            try:
                partner_three_left_a_right = level_three_a.get(position=Partner.POSITION_RIGHT)
            except:
                partner_three_left_a_right = None
        else:
            level_three_a = None
            partner_three_left_a_left = None
            partner_three_left_a_right = None

        context.update({
            'level_three_a': level_three_a[0] if level_three_a else None,
            'partner_three_left_a_left': partner_three_left_a_left,
            'partner_three_left_a_right': partner_three_left_a_right,
        })

        #Level Three Left B
        if partner_two_a_right:
            try:
                level_three_b = Partner.objects.filter(user__id=partner_two_a_right.partner_user.id)
            except:
                level_three_b = None
            
            try:
                partner_three_left_b_left = level_three_b.get(position=Partner.POSITION_LEFT)
            except:
                partner_three_left_b_left = None
            try:
                partner_three_left_b_right = level_three_b.get(position=Partner.POSITION_RIGHT)
            except:
                partner_three_left_b_right = None
        else:
            level_three_b = None
            partner_three_left_b_left = None
            partner_three_left_b_right = None

        context.update({
            'level_three_b': level_three_b[0] if level_three_b else None,
            'partner_three_left_b_left': partner_three_left_b_left,
            'partner_three_left_b_right': partner_three_left_b_right,
        })

        # Level Three Right A
        if partner_two_b_left:
            try:
                level_three_c = Partner.objects.filter(user__id=partner_two_b_left.partner_user.id)
            except:
                level_three_c = None
            
            try:
                partner_three_right_a_left = level_three_c.get(position=Partner.POSITION_LEFT)
            except:
                partner_three_right_a_left = None
            try:
                partner_three_right_a_right = level_three_c.get(position=Partner.POSITION_RIGHT)
            except:
                partner_three_right_a_right = None
        else:
            level_three_c = None
            partner_three_right_a_left = None
            partner_three_right_a_right = None

        context.update({
            'level_three_c': level_three_c[0] if level_three_c else None,
            'partner_three_right_a_left': partner_three_right_a_left,
            'partner_three_right_a_right': partner_three_right_a_right,
        })

        # Level Three Right B
        if partner_two_b_right:
            try:
                level_three_d = Partner.objects.filter(user__id=partner_two_b_right.partner_user.id)
            except:
                level_three_d = None
            
            try:
                partner_three_right_b_left = level_three_d.get(position=Partner.POSITION_LEFT)
            except:
                partner_three_right_b_left = None
            try:
                partner_three_right_b_right = level_three_d.get(position=Partner.POSITION_RIGHT)
            except:
                partner_three_right_b_right = None
        else:
            level_three_d = None
            partner_three_right_b_left = None
            partner_three_right_b_right = None

        context.update({
            'level_three_d': level_three_d[0] if level_three_d else None,
            'partner_three_right_b_left': partner_three_right_b_left,
            'partner_three_right_b_right': partner_three_right_b_right,
        })

        return context
    

