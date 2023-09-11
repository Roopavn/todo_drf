from django.urls import path
from . import views

# we map the generic views to specific URLs.
#  You can customize the URLs and view names as needed.

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('candidatedirectory-list/', views.CandidatedirectoryListView.as_view(), name='candidatedirectory-list'),
    path('candidatedirectory/<int:pk>/', views.CandidatedirectoryDetailView.as_view(), name='candidatedirectory-detail'),
    path('candidatedirectory/create/', views.CandidatedirectoryCreateView.as_view(), name='candidatedirectory-create'),
#   path('candidatedirectory-list/<int:pk>/', views.CandidatedirectoryUpdateView.as_view(), name='update_model'),
]



