shopping_list = {'piekarnia':['chleb', 'bułki', 'pączek'], 'warzywniak':['marchew', 'seler', 'rukola']}
for i in shopping_list:
    new_list = [elem.capitalize() for elem in shopping_list.get(i)]
    print("Idę do", i.capitalize(), ", kupuję tu następujące rzeczy: ", new_list)