def apply_all_func(int_list, *functions):
    results = {}
    for function in functions:
        result = function(int_list)
        results[function.__name__] = result
    return results

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))

# Это я для себя сохраню, пусть будет
# В примере используются следующие функции:
# min - принимает список, возвращает минимальное значение из него.
# max - принимает список, возвращает максимальное значение из него.
# len - принимает список, возвращает кол-во элементов в нём.
# sum - принимает список, возвращает сумму его элементов.
# sorted - принимает список, возвращает новый отсортированный список на основе переданного.