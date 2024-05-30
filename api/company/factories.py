import uuid
from datetime import date
import factory
from factory.django import DjangoModelFactory

from api.company.models import Company, Measure, KPI, Control


class CompanyFactory(DjangoModelFactory):
    class Meta:
        model = Company

    name = factory.Faker('company')
    description = factory.Faker('text')
    founded_date = factory.Faker('date_this_century')
    website = factory.Faker('url')


class MeasureFactory(DjangoModelFactory):
    class Meta:
        model = Measure

    company = factory.SubFactory(CompanyFactory)
    name = factory.Faker('word')
    value = factory.Faker('pyfloat', positive=True)
    date_recorded = factory.Faker('date_this_year')


class KPIFactory(DjangoModelFactory):
    class Meta:
        model = KPI

    company = factory.SubFactory(CompanyFactory)
    name = factory.Faker('word')
    target_value = factory.Faker('pyfloat', positive=True)
    actual_value = factory.Faker('pyfloat', positive=True)
    date_measured = factory.Faker('date_this_year')


class ControlFactory(DjangoModelFactory):
    class Meta:
        model = Control

    company = factory.SubFactory(CompanyFactory)
    name = factory.Faker('word')
    description = factory.Faker('text')
    status = factory.Faker('random_element', elements=['active', 'inactive'])
    last_reviewed = factory.Faker('date_this_year')
