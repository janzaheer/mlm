from django.urls import path

from .views import (
    IndexView, LogoutView, LoginView, CreateMemberFormView,
    MemberList, MemberRelationsList, MemberUpadateTemplateView,
    MemberUpdateView, MemberRelationDeleteView
)

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    
    path('member/create', CreateMemberFormView.as_view(), name='create_member'),
    path('member/<int:pk>/update/form', MemberUpadateTemplateView.as_view(), name='update_member_form'),
    path('member/<int:pk>/update', MemberUpdateView.as_view(), name='update_member'),
    path('member/<int:pk>/delete', MemberRelationDeleteView.as_view(), name="delete_relations"),
    
    path('member/list', MemberList.as_view(), name='list_member'),
    path('relations/list', MemberRelationsList.as_view(), name='list_relations'),
    
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
]
