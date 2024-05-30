from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action, api_view

from api.company.models import Company, Measure, KPI, Control
from api.company.serializers import CompanySerializer, MeasureSerializer, KPISerializer, ControlSerializer


COMPANY_TEST_ID = 'c55762fa-a3ca-4dbb-a0aa-ba1b070ad8a5'


@api_view(['GET'])
def get_company_home_page_data(request):
    company = Company.objects.get(pk=COMPANY_TEST_ID)

    return Response({
        'name': company.name,
        'id': company.id,
    }, status=status.HTTP_200_OK)


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    @action(detail=True, methods=['get'])
    def measures(self, request, pk=None):
        company = self.get_object()
        measures = Measure.objects.filter(company=company)
        serializer = MeasureSerializer(measures, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def kpis(self, request, pk=None):
        company = self.get_object()
        kpis = KPI.objects.filter(company=company)
        serializer = KPISerializer(kpis, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def controls(self, request, pk=None):
        company = self.get_object()
        controls = Control.objects.filter(company=company)
        serializer = ControlSerializer(controls, many=True)
        return Response(serializer.data)
