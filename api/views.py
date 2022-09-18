from rest_framework import generics, permissions
from datetime import datetime

from rest_framework.response import Response
from rest_framework.views import APIView

from db.models import Restaurant, Employee, Menu, Vote
from .serializers import (RestaurantSerializer,
                          EmployeeSerializer,
                          MenuSerializer, ResultSerializer,
                          )


class EmployeeAPIView(generics.CreateAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()


class RestaurantAPIView(generics.CreateAPIView):
    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.all()


class MenuAPIView(generics.CreateAPIView):
    serializer_class = MenuSerializer
    queryset = Menu.objects.all()


class TodayMenuAPIView(generics.ListAPIView):
    serializer_class = MenuSerializer
    queryset = Menu.objects.filter(created_at__iso_week_day=datetime.today().isoweekday())


class VoteAPIView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, menu_id):
        employee = request.user
        print(employee)
        menu = Menu.objects.get(id=menu_id)
        if Vote.objects.filter(
                employee__email=employee,
                created_at=datetime.today()).exists():
            res = {'message': 'voted'}
            return Response(res)
        else:
            Vote.objects.create(
                employee=employee,
                menu=menu,
            )
            menu.save()
            res = {'success': 'True'}
            return Response(res)


class ResultAPIView(generics.ListAPIView):
    serializer_class = ResultSerializer
    queryset = Menu.objects.filter(created_at=datetime.today()).order_by('votes')