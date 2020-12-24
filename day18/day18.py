def do_math(expression):
    # Assumes expression starts with a number
    args = expression.split()
    res = int(args[0])
    while len(args) > 2:
        op = args[1]
        num2 = int(args[2])
        res = (res + num2) if op == '+' else (res * num2)
        args = args[2:]
        args[0] = res
    return res

def replace_parentheses(expression, expr_eval_function):
    # Evaluates expression within rightmost or most-nested parentheses
    open_idx = expression.rfind('(')
    close_idx = expression.find(')', open_idx)
    if open_idx == -1 or close_idx == -1:  # No parentheses
        return str(expr_eval_function(expression))
    else:
        inside = expression[open_idx:close_idx+1]
        replaced = expression.replace(inside, str(expr_eval_function(inside[1:-1])))
        return replace_parentheses(replaced, expr_eval_function)

# Process input data
results = []
with open('day18/input.txt', 'r') as file:
    for line in file:
        results.append(int(replace_parentheses(line, do_math)))
print('Part 1:', sum(results))


# Part 2
def do_math_pt2(expression):
    # do_math, prioritizing addition over multiplication
    args = expression.split()
    res = 0
    if len(args) >= 5:
        # Check to see if we need to evaluate the second operation first
        num1, op1, num2, op2, num3 = args[:5]
        if (op1 != '+') and (op2 == '+'):
            # Do operation 2 first
            eval_first = ' '.join(args[2:5])
            args[2] = str(do_math(eval_first))
            del args[3:5]
            return do_math_pt2(' '.join(args))
        else:
            # Do operation 1 first like in Part 1
            res += do_math(' '.join(args[:3]))
            args = args[2:]
            args[0] = str(res)
            return do_math_pt2(' '.join(args))
    elif len(args) == 3:
        res += do_math(' '.join(args))
    elif len(args) == 1:
        res = int(expression)
    return res

# Process input data
results2 = []
with open('day18/input.txt', 'r') as file:
    for line in file:
        results2.append(int(replace_parentheses(line, do_math_pt2)))
print('Part 2:', sum(results2))
