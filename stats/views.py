import datetime

from django.db.models import Q, Count, Sum
from django.http import JsonResponse
from rest_framework import generics, status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet

from .models import *
from .serializers import *


class StatisticsMixin(ViewSet):
    def retrieve(self, request: Request, participant):
        params = self.params(request)
        month = params.get('month')
        year = params.get('year')

        result = participant.annotate(
            clients_count=Count('order', filter=Q(order__date__year=year, order__date__month=month)),
            products_count=Count('order__products', filter=Q(order__date__year=year, order__date__month=month)),
            total_sales=Sum('order__price', filter=Q(order__date__year=year, order__date__month=month))
        )

        return result

    @staticmethod
    def params(request: Request):
        month = request.query_params.get('month')
        year = request.query_params.get('year')

        return {'month': month, 'year': year}


class GetStatEmployee(StatisticsMixin):
    def retrieve(self, request, pk) -> JsonResponse:
        employee = Employee.objects.filter(id=pk)
        if not employee.exists():
            return JsonResponse({'detail': 'Employee not found'}, status=status.HTTP_404_NOT_FOUND)

        result = super().retrieve(request, employee)
        return JsonResponse(EmployeeResultSerializer(result.first()).data)

    def list(self, request):
        params = self.params(request)
        month = params.get('month')
        year = params.get('year')

        result = Employee.objects.annotate(
            clients_count=Count('order', filter=Q(order__date__year=year, order__date__month=month)),
            products_count=Count('order__products', filter=Q(order__date__year=year, order__date__month=month)),
            total_sales=Sum('order__price', filter=Q(order__date__year=year, order__date__month=month))

        )
        serializer = EmployeeResultSerializer(result, many=True)
        return Response(serializer.data)


class GetStatClient(StatisticsMixin):
    def retrieve(self, request: Request, pk):
        client = Client.objects.filter(id=pk)
        if not client.exists():
            return JsonResponse({'detail': 'Client not found'}, status=status.HTTP_404_NOT_FOUND)

        result = super().retrieve(request, client)

        return JsonResponse(ClientResultSerializer(result.first()).data)

    def list(self):
        pass