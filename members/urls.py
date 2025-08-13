"""URLs for the members app in the project"""

from django.urls import path, include
from . import views
from rest_framework.routers import  DefaultRouter
from .views import MemberViewSet, CoachViewSet, MembershipViewSet, MatchViewSet

router = DefaultRouter()
router.register(r'members', MemberViewSet)
router.register(r'coaches', CoachViewSet)
router.register(r'memberships', MembershipViewSet)
router.register(r'matches', MatchViewSet)

urlpatterns = [
   # path('', views.main, name='main'),
    # path('members/', views.members, name='members'),
    # path('members/details/<int:member_id>', views.details, name='details'),
    # path('testing/', views.testing, name='testing'),
    path('api/', include(router.urls)),

]
