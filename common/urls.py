from django.urls import path

from .views import (
    IndexView, LogoutView, LoginView, CreateMemberFormView,
    MemberList, MemberRelationsList
)

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('member/create', CreateMemberFormView.as_view(), name='create_member'),
    path('member/list', MemberList.as_view(), name='list_member'),
    path('relations/list', MemberRelationsList.as_view(), name='list_relations'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
]
