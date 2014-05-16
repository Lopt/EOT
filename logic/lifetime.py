# -*- coding: utf-8 -*-

def Calculate(seconds=0, minutes=0, hours=0, days=0, months=0, years=0, decade=0, centuries=0, millenniums=0):
    centuries += millenniums
    decade += centuries * 10
    years += decade * 10
    months += years * 12
    days += months * 30
    hours += days * 24
    minutes += hours * 60
    seconds += minutes * 60
    return seconds

if __name__ == "__main__":
    print Calculate(years=50)