from rest_framework import serializers

from api.company.models import Company, Measure, KPI, Control


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'description', 'founded_date', 'website']


class MeasureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measure
        fields = ['id', 'company', 'name', 'value', 'date_recorded']


class KPISerializer(serializers.ModelSerializer):
    class Meta:
        model = KPI
        fields = ['id', 'company', 'name', 'target_value', 'actual_value', 'date_measured']


class ControlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Control
        fields = ['id', 'company', 'name', 'description', 'status', 'last_reviewed']
