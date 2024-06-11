from django.urls import path
from . import views

app_name = 'char_equip'
urlpatterns = [
    path('character/<int:character_id>/', views.character_detail, name='character_detail'),
    path('items/', views.item_list, name='item_list'),
    path('character/<int:character_id>/equip/<int:item_id>/', views.equip_item, name='equip_item'),
    path('character/<int:character_id>/backpack/<int:item_id>', views.move_to_backpack, name='move_to_backpack'),
]