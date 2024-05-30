from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.company.views import CompanyViewSet, get_company_home_page_data


router = DefaultRouter()
router.register(r'company', CompanyViewSet)

urlpatterns = [
    path('company/home-page-data/', get_company_home_page_data, name='home-page-data'),
    path('company/<int:pk>/measures/', CompanyViewSet.as_view({'get': 'measures'}), name='company-measures'),
    path('company/<int:pk>/kpis/', CompanyViewSet.as_view({'get': 'kpis'}), name='company-kpis'),
    path('company/<int:pk>/controls/', CompanyViewSet.as_view({'get': 'controls'}), name='company-controls'),
]

urlpatterns += router.urls
