equ = input("Enter Equation: ")
def equ_to_lst(equ):
     operand_list = ["+", "-", "*", "^", "/", "%"]
     priority = ["^","/", "%", "*", "+", "-"]
     n_list = []
     dummy =""
     count = 0
     for x in equ:
          if x in operand_list:
               if dummy != "":
                    n_list.append(int(dummy))
                    dummy = ""
               n_list.append(x)
          else:
               dummy += x
          if count + 1 == len(equ):
               if dummy != "":
                    n_list.append(int(dummy))
                    dummy = ""
          count += 1
     updated_priority = []
     for x in priority:
          count = n_list.count(x)
          for i in range(count):
               updated_priority.append(x)
     return(n_list, updated_priority)
def lst_to_ans(n_list, updated_priority):               
     for y in updated_priority:
          if y in n_list:
               if y == "^":
                    result = n_list[int(n_list.index(y) - 1)] ** n_list[int(n_list.index(y) + 1)]
                    del(n_list[n_list.index(y) - 1])
                    del(n_list[n_list.index(y) + 1])
                    n_list.insert((n_list.index(y)), result)
                    del n_list[n_list.index(y)]
               if y == "/":
                    result = round((n_list[int(n_list.index(y) - 1)] / n_list[int(n_list.index(y) + 1)]), 1)
                    del(n_list[n_list.index(y) - 1])
                    del(n_list[n_list.index(y) + 1])
                    n_list.insert((n_list.index(y)), result)
                    del n_list[n_list.index(y)]
               if y == "%":
                    result = round(n_list[int(n_list.index(y) - 1)] % n_list[int(n_list.index(y) + 1)], 1)
                    del(n_list[n_list.index(y) - 1])
                    del(n_list[n_list.index(y) + 1])
                    n_list.insert((n_list.index(y)), result)
                    del n_list[n_list.index(y)]
               if y == "*":
                    result = round(n_list[int(n_list.index(y) - 1)] * n_list[int(n_list.index(y) + 1)], 1)
                    del(n_list[n_list.index(y) - 1])
                    del(n_list[n_list.index(y) + 1])
                    n_list.insert((n_list.index(y)), result)
                    del n_list[n_list.index(y)]
               if y == "+":
                    if n_list[int(n_list.index(y) - 2)]  == "-":
                         if n_list[int(n_list.index(y) + 1)] > n_list[int(n_list.index(y) - 1)]:                    
                              result = n_list[int(n_list.index(y) + 1)] - n_list[int(n_list.index(y) - 1)]
                              n_list[int(n_list.index(y) - 2)] = "-"
                              del(n_list[n_list.index(y) - 1])
                              del(n_list[n_list.index(y) + 1])
                              n_list.insert((n_list.index(y)), result)
                              del n_list[n_list.index(y)]
                         else:
                              result = n_list[int(n_list.index(y) - 1)] - n_list[int(n_list.index(y) + 1)]
                              n_list[int(n_list.index(y) - 2)] = "-"
                              del(n_list[n_list.index(y) - 1])
                              del(n_list[n_list.index(y) + 1])
                              n_list.insert((n_list.index(y)), result)
                              del n_list[n_list.index(y)] 
                    else:
                         result = n_list[int(n_list.index(y) - 1)] + n_list[int(n_list.index(y) + 1)]
                         del(n_list[n_list.index(y) - 1])
                         del(n_list[n_list.index(y) + 1])
                         n_list.insert((n_list.index(y)), result)
                         del n_list[n_list.index(y)]
               if y == "-":
                    result = n_list[int(n_list.index(y) - 1)] - n_list[int(n_list.index(y) + 1)]
                    del(n_list[n_list.index(y) - 1])
                    del(n_list[n_list.index(y) + 1])
                    n_list.insert((n_list.index(y)), result)
                    del n_list[n_list.index(y)]
     print("Solution: {}".format(result))
     return(result)

v1,v2 = equ_to_lst(equ)
lst_to_ans(v1, v2)


