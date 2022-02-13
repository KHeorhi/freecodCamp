def arithmetic_arranger(problems, see_result = False):

  num_one_list = []
  num_two_list = []
  operator_list = []
  result_list = []
  dash_list = []

  try:
    if len(problems) <= 5:
      for problem in range(len(problems)):
        
        num = problems[problem].split()
        try:
          num_one = int(num[0])
          num_two = int(num[2])
        except:
          return 'Error: Numbers must only contain digits.'

        operator = num[1]

        try:
          if len(str(abs(num_one))) or len(str(abs(num_two)))<= 4:
            pass
        except:
          return 'Error: Numbers cannot be more than four digits.'
        
        try:    
          if operator == '-':
            result = num_one - num_two
          elif operator == '+':
            result = num_one + num_two
        except:
          return 'Error: Operator must be \'+\' or \'-\'.'

        if result > 0 and len(num[0]) < len(str(result)) and len(num[2]) < len(str(result)):
          dash = '-'*(len(str(result))+1)
        elif result > 0:
          dash = '-'*(len(str(result))+2)
        elif result < 0:
          dash = '-'*(len(str(result))+1)
        

        num_one_list.append(num[0]), num_two_list.append(num[2]), operator_list.append(operator), result_list.append(result), dash_list.append(dash)
      
      line_one = []
      line_two = []
      line_three = []
      line_four = []

      for i in range(len(num_one_list)):
        
        len_dash = len(dash_list[i])
        len_num_one = len(num_one_list[i])
        len_num_two = len(num_two_list[i])
        len_operator = len(operator_list[i])
        len_result = len(str(result_list[i]))

        count_dash_one = len_dash - len_num_one
        count_oper_two = len_dash - (len_num_two + len_operator)
        count_result = len_dash - len_result

        new_num_one = ' '*count_dash_one + num_one_list[i]
        line_oper_num_two = operator_list[i] + ' '*count_oper_two + num_two_list[i]
        line_result = ' '*count_result + str(result_list[i])
        line_one.append(new_num_one), line_two.append(line_oper_num_two), line_three.append(dash_list[i])
        line_four.append(line_result)

      print(('    ').join(line_one))
      print(('    ').join(line_two))
      print(('    ').join(line_three))
      if see_result != False:
        print(('    ').join(line_four))
  except:
    return "Error: Too many problems."
  #return arranged_problems