from rest_framework import generics
from datetime import datetime
from db.models import Restaurant, Employee, Menu, Vote
from .serializers import (RestaurantSerializer,
                          EmployeeSerializer,
                          MenuSerializer, VoteSerializer, ResultSerializer,
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


class VoteAPIView(generics.ListCreateAPIView):
    serializer_class = VoteSerializer
    queryset = Vote.objects.all()

    def perform_create(self, serializer):
        serializer.save(employee=self.request.user)


'''
class VoteAPIView(generics.ListCreateAPIView):
    serializer_class = VoteSerializer

    def get_queryset(self):
        employee = self.request.user
        menu = Menu.objects.filter(id=menu_id)
        if Vote.objects.filter(
                menu__id=menu_id,
                employee__email=employee,
                created_at__date=datetime.today()).exists():
            return {'message': 'voted'}
        else:
            Vote.objects.create(
                employee=employee,
                menu=menu
            )
            menu.save()
            return {'success': 'True'}
'''


class ResultAPIView(generics.ListAPIView):
    serializer_class = ResultSerializer
    queryset = Menu.objects.filter(created_at=datetime.today()).order_by('-votes')