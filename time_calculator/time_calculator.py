from minut import convert
from minut import time_calculate

def add_time(start, duration, *weekday):
  day_one = start.split(' ')
  day_one_time = day_one[0].split(':')
  day_two = duration.split(':')
  list_day_one = convert(day_one_time[0], day_one_time[1])
  list_day_two = convert(day_two[0], day_two[1])
  return time_calculate(day_one[1], list_day_one, list_day_two)
  #return new_time

print(add_time("3:00 PM", "3:10"))