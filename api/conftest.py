from uuid import UUID
import pytest

from rest_framework.test import APIClient

from api.company.factories import CompanyFactory, MeasureFactory, KPIFactory, ControlFactory


COMPANY_TEST_ID = UUID('10a3c664-e5de-4a4a-a7c0-d66b21637d40')


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def company():
    return CompanyFactory.create(id=COMPANY_TEST_ID)


@pytest.fixture
def measures(company):
    return MeasureFactory.create_batch(3, company=company)


@pytest.fixture
def kpis(company):
    return KPIFactory.create_batch(3, company=company)


@pytest.fixture
def controls(company):
    return ControlFactory.create_batch(3, company=company)
