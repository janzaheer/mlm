from django.contrib.auth import forms as auth_forms
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate
from django.urls import reverse, reverse_lazy

from django.views.generic import (
    TemplateView, FormView, RedirectView, ListView,
    UpdateView, DeleteView, View
)
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Partner, Member
from .forms import MemberForm, PartnerForm


class SuperUserMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_superuser:
            raise Http404('Page not Found')
        return super().dispatch(request, *args, **kwargs)
    

class LoginView(FormView):
    form_class = auth_forms.AuthenticationForm
    template_name = 'login.html'

    
    def form_valid(self, form):
        user = form.get_user()
        auth_login(self.request, user)
        return HttpResponseRedirect(reverse('common:index'))
    
    def form_invalid(self, form):
        return super().form_invalid(form)


class LogoutView(RedirectView):
    def dispatch(self, request, *args, **kwargs):
        auth_logout(self.request)
        return super(LogoutView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return HttpResponseRedirect(reverse('common:login'))


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'
    login_url = reverse_lazy('common:login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        me_member = Member.objects.filter(
            created_user__id=self.request.user.id,
            mobile=self.request.GET.get('user_id')
        )

        context.update({
            'member': me_member,
            'step_kw': self.request.GET.get('step_id', 1)
        })

        # Level One
        level_one = Partner.objects.filter(
            member_parent__step_id=self.request.GET.get('step_id', 1),
            # member_parent__created_user__id=self.request.user.id
        )

        if level_one:
            if self.request.GET.get('user_id') and  not level_one.filter(member_parent__mobile=self.request.GET.get('user_id')).exists():
                level_one = Member.objects.filter(mobile=self.request.GET.get('user_id'))
            elif self.request.GET.get('user_id'):
                level_one = level_one.filter(
                    member_parent__mobile=self.request.GET.get('user_id')
                )
            else:
                level_one = level_one.filter(
                    member_parent__mobile=level_one[0].member_parent.mobile
                )

        if self.request.user.is_superuser:
            if not self.request.GET.get('user_id'):
                level_one = Member.objects.filter(
                    user__id=self.request.user.id, step_id=self.request.GET.get('step_id', 1))
                if level_one and level_one[0].member_as_parent.exists():
                    level_one = level_one[0].member_as_parent.all()
            # else:
            #     level_one = Partner.objects.filter(member_parent__mobile=self.request.GET.get('user_id'))

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
                level_two_a = Partner.objects.filter(
                    member_parent__id=partner_one_left.member_child.id, 
                    member_parent__step_id=self.request.GET.get('step_id', 1),
                    # member_parent__created_user__id=self.request.user.id
                )
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
                level_two_b = Partner.objects.filter(
                    member_parent__id=partner_one_right.member_child.id,
                    member_parent__step_id=self.request.GET.get('step_id', 1),
                    # member_parent__created_user__id=self.request.user.id
                )
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
                level_three_a = Partner.objects.filter(
                    member_parent__id=partner_two_a_left.member_child.id,
                    member_parent__step_id=self.request.GET.get('step_id', 1),
                    # member_parent__created_user__id=self.request.user.id
                )
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
                level_three_b = Partner.objects.filter(
                    member_parent__id=partner_two_a_right.member_child.id,
                    member_parent__step_id=self.request.GET.get('step_id', 1),
                    # member_parent__created_user__id=self.request.user.id
                )
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
                level_three_c = Partner.objects.filter(
                    member_parent__id=partner_two_b_left.member_child.id,
                    member_parent__step_id=self.request.GET.get('step_id', 1),
                    # member_parent__created_user__id=self.request.user.id
                )
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
                level_three_d = Partner.objects.filter(
                    member_parent__id=partner_two_b_right.member_child.id,
                    member_parent__step_id=self.request.GET.get('step_id', 1),
                    # member_parent__created_user__id=self.request.user.id
                )
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
    

from django.contrib.auth import forms as auth_forms
from django.db import transaction

class CreateMemberFormView(LoginRequiredMixin, SuperUserMixin, FormView):
    template_name = 'create_member.html'
    form_class = auth_forms.UserCreationForm

    def form_valid(self, form):
        
        with transaction.atomic():
            try:
                member_parent = Member.objects.get(
                    mobile=self.request.POST.get('parent_phone'),
                    step_id=self.request.POST.get('step_id')
                )
            except:
                member_parent = ''

            user = form.save()
            user.email = self.request.POST.get('email')
            user.save()

            member_form_kwargs = {
                'user': user.id,
                'name': self.request.POST.get('name'),
                'mobile': self.request.POST.get('username'),
                'gender': self.request.POST.get('gender'),
                'step_id': self.request.POST.get('step_id'),
                'created_user': self.request.user.id
            }
            
            member_form = MemberForm(member_form_kwargs)
            if member_form.is_valid():
                member = member_form.save()


            partner_form_kwargs = {
                'member_parent': member_parent.id,
                'member_child': member.id,
                'position': self.request.POST.get('position')
            }

            partner_form = PartnerForm(partner_form_kwargs)
            if partner_form.is_valid():
                partner_form.save()

        return HttpResponseRedirect(reverse('common:list_relations'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context[""] = 
        return context



class MemberUpadateTemplateView(LoginRequiredMixin, SuperUserMixin, TemplateView):
    template_name = 'update_member.html'
    # form_class = auth_forms.UserCreationForm
    # model = Partner

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        partner = Partner.objects.get(id=kwargs.get('pk'))
        context.update({
            'object': partner
        }) 
        return context


class MemberUpdateView(LoginRequiredMixin, SuperUserMixin, View):
     
    def post(self, request, *args, **kwargs):
        username = self.request.POST.get('username')
        parent_phone = self.request.POST.get('parent_phone')
        name = self.request.POST.get('name')
        email_address = self.request.POST.get('email_address')
        gender = self.request.POST.get('gender')
        position = self.request.POST.get('position')
        step_id = self.request.POST.get('step_id')

        partner = Partner.objects.get(id=self.kwargs.get('pk'))
        parent_member = Member.objects.get(mobile=parent_phone)

        partner.position = position
        partner.member_parent = parent_member

        partner.save()

        partner.member_child.gender = gender
        partner.member_child.step_id = step_id
        partner.member_child.mobile = username
        partner.member_child.name = name

        partner.member_child.save()

        if partner.member_child.user:
            user = User.objects.get(
                username=partner.member_child.user.username)
            user.username = username
            user.email = email_address
            user.save()
        else:
            user = User.objects.create(
                username=username, email=email_address)

            partner.member_child.user = user
            partner.member_child.save()
            

        return HttpResponseRedirect(reverse('common:list_relations'))
    

class MemberRelationDeleteView(LoginRequiredMixin, SuperUserMixin, DeleteView):
    model = User
    success_url = reverse_lazy('common:list_relations')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class MemberList(LoginRequiredMixin, SuperUserMixin, ListView):
    model = Member
    template_name='list_member.html'
    paginate_by=20


class MemberRelationsList(LoginRequiredMixin, SuperUserMixin, ListView):
    model = Partner
    template_name='list_relations.html'
    paginate_by=20
