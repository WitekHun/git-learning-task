shopping_list = {'piekarnia':['chleb', 'bułki', 'pączek'], 'warzywniak':['marchew', 'seler', 'rukola']}
products_sum = 0
for i in shopping_list:
    new_list = [elem.capitalize() for elem in shopping_list.get(i)]
    print("Idę do", i.capitalize(), ", kupuję tu następujące rzeczy: ", new_list)
    products_sum += len(shopping_list.get(i))
print("W sumie kupuję", products_sum, 'produktów')
print("'Hiszpańska inkwizycja' to najlepszy skecz grupy Monty Pythona") 
