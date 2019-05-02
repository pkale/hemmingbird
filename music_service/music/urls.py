from django.urls import path
from .views import ListSongsView, ListCustomersView,ListTailorsView


urlpatterns = [
    path('songs/', ListSongsView.as_view(), name="songs-all"),
    path('customers/', ListCustomersView.as_view(), name="customers-all"),
	path('tailors/', ListTailorsView.as_view(), name="tailors-all"),

]