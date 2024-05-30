import random
from uuid import UUID

from datetime import date, timedelta
from django.core.management.base import BaseCommand
from api.company.models import Company, Measure, KPI, Control


FAKE_UUIDS = [
    UUID('c55762fa-a3ca-4dbb-a0aa-ba1b070ad8a5'),
    UUID('1b1f6741-8ef5-4690-9bc6-c46b4efb5a68'),
    UUID('22237326-9980-4b3b-afa7-368c21e4ee48'),
    UUID('507fbd3c-8bc7-401e-ad5f-96d8558f671f'),
    UUID('c9f26fea-592e-4ff6-9d6b-882b15ab48b6'),
]


class Command(BaseCommand):
    help = 'Generate test data for Company, Measure, KPI, and Control models'

    def handle(self, *args, **kwargs):
        # Create some companies
        companies = []
        for index, id in enumerate(FAKE_UUIDS):
            company = Company.objects.create(
                id=id,
                name=f'Company {index}',
                description=f'Description for Company {index}',
                founded_date=date.today() - timedelta(days=random.randint(1, 10000)),
                website=f'https://www.company{index}.com'
            )
            companies.append(company)
            self.stdout.write(self.style.SUCCESS(f'Created {company.name}'))

        # Create measures for each company
        for company in companies:
            for j in range(3):
                measure = Measure.objects.create(
                    company=company,
                    name=f'Measure {j+1} for {company.name}',
                    value=random.uniform(10.0, 100.0),
                    date_recorded=date.today() - timedelta(days=random.randint(1, 100))
                )
                self.stdout.write(self.style.SUCCESS(f'Created {measure.name} for {company.name}'))

        # Create KPIs for each company
        for company in companies:
            for k in range(3):
                kpi = KPI.objects.create(
                    company=company,
                    name=f'KPI {k+1} for {company.name}',
                    target_value=random.uniform(50.0, 200.0),
                    actual_value=random.uniform(10.0, 150.0),
                    date_measured=date.today() - timedelta(days=random.randint(1, 100))
                )
                self.stdout.write(self.style.SUCCESS(f'Created {kpi.name} for {company.name}'))

        # Create controls for each company
        for company in companies:
            for l in range(2):
                control = Control.objects.create(
                    company=company,
                    name=f'Control {l+1} for {company.name}',
                    description=f'Description for Control {l+1} for {company.name}',
                    status=random.choice(['active', 'inactive']),
                    last_reviewed=date.today() - timedelta(days=random.randint(1, 365))
                )
                self.stdout.write(self.style.SUCCESS(f'Created {control.name} for {company.name}'))

        self.stdout.write(self.style.SUCCESS('Successfully generated test data'))
