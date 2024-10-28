from django.urls import path
from userApp.views import XodimView

urlpatterns = [
    path('xodim/', XodimView.as_view(), name='xodim'),
]
