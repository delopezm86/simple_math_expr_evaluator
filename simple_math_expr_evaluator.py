import operator as oper

oper_dict = {
    '+': (oper.add,2),
    '-': (oper.sub,2),
    '*': (oper.mul,1),
    '/': (oper.truediv,1)
}

def is_number(strnumber):
    try:
        float(strnumber)
        return True
    except Exception:
        return False


def find_closing_parentheses(expr_list, ind):
    pos = 0
    i = ind
    for char in expr_list[ind:]:
        if char == "(":
            pos += 1
        if char == ")":
            pos -= 1
        if pos == 0:
            return i
        i += 1


def eval_prefix(expr):
    e = list(oper_dict.get(e, [e])[0] for e in expr)
    i = 0
    while i + 3 <= len(e):
        o, l, r = e[i:i+3]
        if type(o) == type(oper.add) and is_number(l) and is_number(r):
            e[i:i+3] = [o(l, r)]
            i = 0
        else:
            i += 1
    if len(e) != 1:
        print('Error in expression:', expr)
        return 0
    else:
        return e[0]


def simplify_parentheses(expression):
    for pos, chr in enumerate(expression):
        if chr == '(':
            closing_parentheses_pos = find_closing_parentheses(expression, pos)
            del expression[closing_parentheses_pos]
            expression[pos + 1:closing_parentheses_pos] = [str(eval_prefix(to_polish(''.join(expression[pos + 1:closing_parentheses_pos]))))]
            del expression[pos]


def to_polish(expression, begin=0, end=0):
  expression = list(expression.replace(' ',''))
  polish_list = []
  str_number = ''
  last_oper_pos = 0
  simplify_parentheses(expression)
  for pos, chr in enumerate(expression):
      if is_number(chr):
          str_number += chr
      else:
          polish_list.insert(end,float(str_number))
          str_number = ''
          end += 1
          if is_number(polish_list[begin]):
              polish_list.insert(begin, chr)
              end += 1
          else:
              if oper_dict[polish_list[last_oper_pos]][1] > oper_dict[chr][1]:
                  polish_list.insert(end-1,chr)
                  last_oper_pos = end - 1
              elif oper_dict[polish_list[last_oper_pos]][1] == oper_dict[chr][1]:
                  polish_list.insert(last_oper_pos, chr)
                  begin = last_oper_pos
              else:
                  polish_list.insert(begin, chr)
                  last_oper_pos = begin
              end += 1
  if str_number:
      polish_list.append(float(str_number))
  return polish_list


print(eval_prefix(to_polish('(2 + (1 + 2) * 2 + (1 - (6 + 4)) / 3) - 9')))
