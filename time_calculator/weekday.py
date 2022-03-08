def weekday_calculator(string, day):
  weekday = string.lower()
  weekday = weekday[0].upper() + weekday[1:]
  if day > 0:
    week = day // 7
    week_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    weeks_index = week_list.index(weekday)
    weeks_list = week_list[weeks_index:]+week_list*week + week_list
    return weeks_list[day]
  else:
    return weekday