from django.urls import path
from accounts.views import (
    login_view,
    logout_view,
    reg_view,
    reg2_view,
)

urlpatterns = [
    path('login/',login_view),
    path('logout/',logout_view),
    path('reg/', reg_view),
    path('reg2/', reg2_view),

]