''' Задача 1_2.	Напишите программу для проверки истинности утверждения  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат. '''

print('X  Y  Z  F_Left\t\tF_Right\tX  Y  Z')
truth_check = True
for x_predicate in range(2):
    for y_predicate in range(2):
        for z_predicate in range(2):
            left_result = not(x_predicate or y_predicate or z_predicate)        # Все скобки в логических операциях - для наглядности и удобочитаемости
            right_result = not(x_predicate) and not(y_predicate) and not(z_predicate)
            print(f'{x_predicate}  {y_predicate}  {z_predicate}  {(left_result)}\t\t{(right_result)}\t{x_predicate}  {y_predicate}  {z_predicate}')
            truth_check = truth_check and (left_result == right_result)
if(truth_check): print('Логическое утверждение  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z  верно для всех значений предикат')
else: print('Логическое утверждение  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z  является ложью')