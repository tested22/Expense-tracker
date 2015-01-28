from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from django.db.models import Q

from expense_tracker.serializers import ExpenseSerializer, WeeklySerializer
from weekly_report import AllWeeklyReports


class WeeklyViewSet(ReadOnlyModelViewSet):
    serializer_class = WeeklySerializer

    def get_queryset(self):
        expenses = self.request.user.expenses.all()
        expenses = expenses.order_by('-date')
        expenses = list(expenses)
        all_weekly_reports = AllWeeklyReports()
        weekly = all_weekly_reports.create(expenses)
        return weekly


class ExpenseViewSet(ModelViewSet):
    serializer_class = ExpenseSerializer

    def get_queryset(self):

        min_amount = self.request.GET.get('min_amount', None)
        max_amount = self.request.GET.get('max_amount', None)
        dc_contains = self.request.GET.get('keywords', None)
        min_date = self.request.GET.get('start_date', None)
        max_date = self.request.GET.get('end_date', None)
        min_time = self.request.GET.get('start_time', None)
        max_time = self.request.GET.get('end_time', None)

        expenses = self.request.user.expenses.all()
        if min_amount:
            expenses = expenses.filter(amount__gte=min_amount)
        if max_amount:
            expenses = expenses.filter(amount__lte=max_amount)
        if dc_contains:
            expenses = expenses.filter(Q(description__icontains=dc_contains) | Q(comment__icontains=dc_contains))
        if min_date:
            expenses = expenses.filter(date__gte=min_date)
        if max_date:
            expenses = expenses.filter(date__lte=max_date)
        if min_time:
            expenses = expenses.filter(time__gte=min_time)
        if max_time:
            expenses = expenses.filter(time__lte=max_time)
        return expenses.order_by('date', 'time')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
