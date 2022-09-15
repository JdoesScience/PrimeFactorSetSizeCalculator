#Purpose of this code: this code can find the number of elements in a factor set based on the exponents of
#of the prime factors obtained from prime factorization
#
#Example: What is the size of the factor set of the integer 112?
#First we prime factorize 112 into its prime factors:
#
# 112 = 2**4 * 7**1
#
#The factor set is the set containing all possible multiplication combinations of the factors and exponents.
#We start with the  first combination, given by
#
# 2**0 * 7**0 = 1.
#
# 1 is thus an element of the factor set. The next element of the factor set is found from
#
# 2**1 * 7**0 = 2
#
#making 2 part of the factor set. Again we go to the next exponent and find the next element is
#
# 2**2 * 7**0 = 4
#
# so the next element is 4. Continuing in this manner until all possible combinations of factors and exponents up to the
#larget exponent for each given prime factor is reached and thus yields the set
#
# {1, 2, 4, 7, 8, 14, 16, 28, 56, 112}
#
#in this case it's easy to count the total number of elements in the factor set. There are 10 elements.
#
#However it is possible to find the number of elements/size of the set without having to calculate and list every factor in the set. Looking
#at the exponents of the prime factors, we notice that multiplying all the exponents of the prime facotrs after adding
# one to each exponent will also give the factor set size. Returning to the example, the prime factorization of 112 is given by
#
# 112 = 2**4 * 7**1
#
#so the size of the factor set can be found by multiplying the exponents after adding 1 to each, in other words
#
# (4 + 1) * (1 + 1) = (5) * (2) = 10
#
#which we know from above is the number of elements/size of our factor set. The extra ones in the algorithm are added
#in order to account for the 0 exponent each time.
#
#This algorithm is helpful because often larger integers can have huge factor sets but simpler prime factorizations.
#Thus this algorithm can be used to find factor set sizes fairly quickly.
#
#
#For example, the number 1663200 has the prime factorization:
#
# 1663200 = 2**5 * 3**3 * 5**2 * 7**1 * 11**1
#
#using the algorithm, the size of the factor set is then:
#
# (5 + 1) * (3 + 1) * (2 + 1) * (1 + 1) * (1 + 1) = 288
#
#in other words, to find the factor set by hand requires doing 288 different multiplications just to
# find the number of elements in the factor set. So the algorithm is extremely helpful in this regard.

#taken from https://stackoverflow.com/questions/28911925/exponential-form-of-prime-factorization-in-python

#n = int(raw_input())
#n = 140

import numpy as np
import matplotlib.pylab as plt

#This function creates the prime factors of some integer input n. Note that it  does not check the input
#as this is very crude code which I plan to add to the primefactorization fork.
#The output is a list of lists, with each inner list containing two elements, the first element
# is the prime factor, say 1, 2, 3, 5, 7, etc while the second element is the exponent
#For example, if the integer 6 is the input, then the function would return [[2, 1], [3, 1]]
#since the prime factorization of 6 = 2**1 * 3**1
#Note that the the output is in increasing order of prime factors.
def get_prime_factors(n):
    prime_factors = []
    start = 2

    while start * start <= n:
        if n % start == 0:
            expo = 0
            while n % start == 0:
                expo = expo + 1
                n = n / start
            prime_factors.append([int(start), expo])
        start = start + 1
    if n > 1:
        prime_factors.append([int(n), 1])

    return prime_factors

#This function performs the algorithm above and finds the size of the factor set from the prime factorization
#Note that here n is list of lists that must come out of the previous 'get_prime_factors()' function
def calculate_factor_set_size(n):
    products_of_exponents = 1
    for i in range(len(n)):
        exponent = n[i][1] + 1 #add + 1 to account for counting to 0 exponent
        products_of_exponents = products_of_exponents * exponent

    return products_of_exponents



#main code
factor_set_sizes = []
number = []
for i in range(1,101):
    number.append(i)
    size = calculate_factor_set_size(get_prime_factors(i))
    factor_set_sizes.append(size)

print(factor_set_sizes)

plt.plot(number, factor_set_sizes)
plt.xlabel('Integer Number')
plt.ylabel('Number of elements in factor set')
plt.show()



myprime = get_prime_factors(140)
print(myprime)
setsize = calculate_factor_set_size(myprime)
print(setsize)
# prime_factors = []
# start = 2
# while start * start <= n:
#     if n % start == 0:
#         expo = 0
#         while n % start == 0:
#             expo = expo + 1
#             n = n / start
#         prime_factors.append([int(start), expo])
#     start = start + 1
#
# if n > 1:
#     prime_factors.append([int(n), 1])
# print(prime_factors)