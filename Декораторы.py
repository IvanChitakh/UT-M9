def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        flag = False
        for i in range(2, result):
            flag |= result % i == 0
            if flag:
                break
        if flag:
            print('Составное')
        else:
            print('Простое')
        return result
    return wrapper

@is_prime
def sum_three(*args):
    return sum(args)


result = sum_three(998, 3, 6)
print(result)