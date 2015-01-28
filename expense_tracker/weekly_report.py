from datetime import date, timedelta
from decimal import Decimal


class AllWeeklyReports(object):
    def __init__(self):
        self.weeks = []
        self.weekly = []

    def get_sunday(self, day):
        difference = (date.weekday(day) + 1) % 7
        return day - timedelta(days=difference)

    def create(self, expenses):
        for expense in expenses:
            start = self.get_sunday(expense.date)
            if start in self.weeks:
                self.weekly[self.weeks.index(start)].increase_total(expense.amount)
            else:
                self.weeks.append(start)
                self.weekly.append(WeeklyReport(start, expense.amount))
        return self.weekly


class WeeklyReport(object):
    def __init__(self, start, amount):
        self.week_of = start
        self.total = amount
        self.average = self.total/Decimal(7)

    def set_week_of(self, start):
        self.week_of = start

    def increase_total(self, amount):
        self.total += amount
        self.average += amount/Decimal(7)
