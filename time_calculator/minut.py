from weekday import weekday_calculator

def convert(hour_two, minut_two):
  try:
    hour_two, minut_two = int(hour_two), int(minut_two)
  except:
    return 'Please, cheack input valuable!'
  conv_hour_to_min = hour_two * 60 + minut_two
  hour = conv_hour_to_min // 60 
  minut = conv_hour_to_min - hour * 60
  
  return hour, minut


def time_calculate(pm, *args):
  hour = args[0][0] + args[1][0]
  minut = args[0][1] + args[1][1]

  if minut >= 60:
    full_hour = minut // 60
    hour = full_hour + hour
    minut = minut - full_hour * 60
  
  day = hour // 24
  #hours = hour - day * 24
  if day > 1 and hour%24 > 0:
    day = day + 1

  hours = abs(hour - day * 24)
  
  if day == 0:
    if 0 < hours < 12 and pm == 'AM':
      pm = 'AM'
      if minut > 10:
        return f'{hours}:{minut} {pm}'
      else:
        return f'{hours}:0{minut} {pm}'
    elif 0 < hours < 12 and pm == 'PM':
      pm = 'PM'
      if len(args) > 2:
        name_day = weekday_calculator(args[2], day)
        if minut > 10:
          return f'{hours}:{minut} {pm}, {name_day}'
        else:
          return f'{hours}:0{minut} {pm}, {name_day}'
      else:
        if minut > 10:
          return f'{hours}:{minut} {pm}'
        else:
          return f'{hours}:0{minut} {pm}'
    elif hours > 12 and pm == 'AM':
      hou = hours - 12
      pm = 'PM'
      if minut > 10:
        return f'{hou}:{minut} {pm}'
      else:
        return f'{hou}:0{minut} {pm}'
    elif hours > 12 and pm == 'PM':
      pm = 'AM'
      hou = hours - 12
      if minut > 10:
        return f'{hou}:{minut} {pm} (next day)'
      else:
        return f'{hou}:0{minut} {pm} (next day)'
    elif hours == 12 and pm == 'AM':
      pm = 'PM'
      if minut > 10:
        return f'{hours}:{minut} {pm}'
      else:
        return f'{hours}:0{minut} {pm}'
    elif hours == 12 and pm == 'PM':
      pm = 'AM'
      if minut > 10:
        return f'{hours}:{minut} {pm}'
      else:
        return f'{hours}:0{minut} {pm}'
  elif args[0][1] == 0 and hour == 24:
    hours = args[0][0]
    if minut > 10:
      return f'{hours}:{minut} {pm} (next day)'
    else:
      return f'{hours}:0{minut} {pm} (next day)'
  
  elif args[0][1] > 0 and args[1][0] == 24:
    if args[1][1] != 0:
      pm = 'AM'
      day = day + 1
      if len(args) > 2:
        name_day = weekday_calculator(args[2], day)
        if minut > 10:
          return f'{hours}:{minut} {pm}, {name_day} ({day} days later)'
        else:
          return f'{hours}:0{minut} {pm}, {name_day} ({day} days later)'
      else:
        if minut > 10:
          return f'{hours}:{minut} {pm} ({day} days later)'
        else:
          return f'{hours}:0{minut} {pm} ({day} days later)'
    else:
      pm = 'AM'
      if len(args) > 2:
        name_day = weekday_calculator(args[2], day)
        if minut > 10:
          return f'{hours}:{minut} {pm}, {name_day} (next day)'
        else:
          return f'{hours}:0{minut} {pm}, {name_day} (next day)'
      else:
        if minut > 10:
          return f'{hours}:{minut} {pm} (next day)'
        else:
          return f'{hours}:0{minut} {pm} (next day)'
      
  elif day > 1:
    if hours < 12:
      pm = 'AM'
      if len(args) > 2:
        name_day = weekday_calculator(args[2], day)
        if minut > 10:
          return f'{hours}:{minut} {pm}, {name_day} ({day} days later)'
        else:
          return f'{hours}:0{minut} {pm}, {name_day} ({day} days later)'
      else:         
        if minut > 10:
          return f'{hours}:{minut} {pm} ({day} days later)'
        else:
          return f'{hours}:0{minut} {pm} ({day} days later)'
    elif 12 < hours < 24:
      pm = 'PM'
      hours = hours - 12
      if minut > 10:
        return f'{hours}:{minut} {pm} ({day} days later)'
      else:
        return f'{hours}:0{minut} {pm} ({day} days later)'
    elif hours == 12:
      pm = 'PM'
      if minut > 10:
        return f'{hours}:{minut} {pm} ({day} days later)'
      else:
        return f'{hours}:0{minut} {pm} ({day} days later)'
    elif hours == 0:
      pm = 'AM'
      if minut > 10:
        return f'{hours}:{minut} {pm} ({day} days later)'
      else:
        return f'{hours}:0{minut} {pm} ({day} days later)'