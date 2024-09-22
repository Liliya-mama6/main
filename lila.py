def is_prime(func):
    def fooot(a, b, c):
        result=func(a, b, c)
        g=True
        for i in range(2, result):
            if result%i==0:
                g=False
        if g:
            f= 'Простое'
        else:
            f= "Составное"
        return f+'\n'+str(result)
    return fooot
@is_prime
def sum_three(a, b, c):
    return a+b+c
print(sum_three(2, 3, 6))
