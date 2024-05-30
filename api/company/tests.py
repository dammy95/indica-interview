from unittest.mock import patch
import pytest

from rest_framework import status
from django.urls import reverse

from api.company.models import Company, Measure, KPI, Control
from api.company.factories import CompanyFactory, MeasureFactory, KPIFactory, ControlFactory


@pytest.mark.django_db
def test_company_creation():
    company = CompanyFactory()

    assert Company.objects.count() == 1
    assert company.name is not None


@pytest.mark.django_db
def test_measure_creation():
    measure = MeasureFactory()

    assert Measure.objects.count() == 1
    assert measure.company is not None
    assert measure.name is not None


@pytest.mark.django_db
def test_kpi_creation():
    kpi = KPIFactory()

    assert KPI.objects.count() == 1
    assert kpi.company is not None
    assert kpi.name is not None


@pytest.mark.django_db
def test_control_creation():
    control = ControlFactory()

    assert Control.objects.count() == 1
    assert control.company is not None
    assert control.name is not None


@patch('api.company.views.COMPANY_TEST_ID', '10a3c664-e5de-4a4a-a7c0-d66b21637d40')
@pytest.mark.django_db
def test_get_company_home_page_data(api_client, company):
    url = reverse('home-page-data')
    
    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert response.data['name'] == company.name
    assert str(response.data['id']) == str(company.id)


@pytest.mark.django_db
def test_company_measures(api_client, company, measures):
    url = reverse('company-measures', args=[company.id])
    
    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 3

    for measure in response.data:
        assert str(measure['company']) == str(company.id)


@pytest.mark.django_db
def test_company_kpis(api_client, company, kpis):
    url = reverse('company-kpis', args=[company.id])
    
    response = api_client.get(url)
    
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 3

    for kpi in response.data:
        assert str(kpi['company']) == str(company.id)


@pytest.mark.django_db
def test_company_controls(api_client, company, controls):
    url = reverse('company-controls', args=[company.id])
    
    response = api_client.get(url)
    
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 3

    for control in response.data:
        assert str(control['company']) == str(company.id)
