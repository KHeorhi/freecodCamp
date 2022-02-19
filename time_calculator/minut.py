def convert(hour_two, minut_two):
  try:
    hour_two, minut_two = int(hour_two), int(minut_two)
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
  if minut < 10:
    return f'Returns: {hour}:0{minut} {pm}'
  else:
    return f'Returns: {hour}:0{minut} {pm}'