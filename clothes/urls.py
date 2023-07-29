from django.urls import path
from .views import ClotheListView, ClotheDetailView, ClotheCreateView, ClotheUpdateView, ClotheDeleteView

urlpatterns = [
    path('', ClotheListView.as_view(), name='clothe_list'),
    path('<int:pk>/', ClotheDetailView.as_view(), name='clothe_detail'),
    path('create/', ClotheCreateView.as_view(), name='clothe_create'),
    path('<int:pk>/update/', ClotheUpdateView.as_view(), name='clothe_update'),
    path('<int:pk>/delete/', ClotheDeleteView.as_view(), name='clothe_delete'),
]