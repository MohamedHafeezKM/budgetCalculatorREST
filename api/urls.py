from django.urls import path,include

from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from api.views import SignUpView,TransactionView

router=DefaultRouter()
router.register(('transactions'),TransactionView,basename='transactions')

urlpatterns=[
    path('register/',SignUpView.as_view()),
    path('generate_token/',views.ObtainAuthToken.as_view())
]+router.urls