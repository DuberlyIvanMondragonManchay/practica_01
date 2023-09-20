from django.urls import path
from .views import get_foods_view,create_food_view,delete_food_view,update_food_view
urlpatterns = [
    path('',get_foods_view , name='foods'),
    path('create/',create_food_view, name='create_food_view'),
    path('delete/<int:food_id>/', delete_food_view, name='delete_food_view'),
    path('update/<int:food_id>/', update_food_view, name='update_food_view'),
]
