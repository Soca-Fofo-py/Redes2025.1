'''
Summation of Primes
Problem 10
The sum of the primes below 10 is 2+3+5+7 = 17
Find the sum of all the primes below two million.
'''
somadosprimos = 0
for z in range(1,2000000+1):
############################
    n = z
    x = 1
    divisores=1
    while x <= n/2:
        if n %x==0:
            divisores+=1
        x=x+1
    #print('O número',n,'tem',divisores,'divisores')
    if divisores == 2:
        somadosprimos +=n
############################
print(somadosprimos)