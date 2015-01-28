from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from expense_tracker.models import Expense
from weekly_report import WeeklyReport


class WeeklySerializer(serializers.Serializer):
    week_of = serializers.DateField()
    total = serializers.DecimalField(max_digits=65, decimal_places=2)
    average = serializers.DecimalField(max_digits=65, decimal_places=2)

    def create(self, validated_data):
        return WeeklyReport(**validated_data)

    def update(self, instance, validated_data):
        instance.week_of = validated_data.get('week_of', instance.week_of)
        instance.total = validated_data.get('total', instance.total)
        instance.average = validated_data.get('average', instance.average)
        instance.save()
        return instance


class ExpenseSerializer(ModelSerializer):
    class Meta:
        model = Expense
        fields = ('id', 'date', 'time', 'description', 'amount', 'comment')
