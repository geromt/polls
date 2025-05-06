from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import PollsAPICreate, PollsAPIRetrieve, ChoiceAPISet, vote

router = DefaultRouter()
router.register('choices', ChoiceAPISet, basename='choices')

urlpatterns = [
    path('create', PollsAPICreate.as_view(), name='polls_create'),
    path('<uuid:pk>', PollsAPIRetrieve.as_view(), name='polls_retrieve'),
    path('vote/<uuid:choice_uuid>', vote, name='polls_vote'),
]
