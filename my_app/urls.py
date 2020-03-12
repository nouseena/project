from django.urls import path
from . import views
from . import array
from . import oop
# from . import oop1


urlpatterns = [
    path('welcome',views.app),
    path('samp',views.fn_sample),
    path('add',views.fn_add),
    path('num',views.fn_number),
    path('list',views.fn_list),
    path('dict',views.fn_dict),
    path('data',views.fn_data),
    path('even',views.fn_num),
    path('odd',views.fn_week),
    path('valid',views.fn_and),
    path('prime',views.fn_prime),

    # path('value',aspyths.fn_display),
    path('fact',views.fn_fact),
    path('part',array.display),
    path('emp',oop.fn_employee),
#     path('cons',oop1.fn_display),

 ]
