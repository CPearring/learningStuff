## cpearring

class alg(object):
    @staticmethod
    def fib(x):
        if x == 1:
            return 0
        elif x == 2:
            return 1
        else:
            return alg.fib(x-2) + alg.fib(x-1)

#print(fib(1))
#print(fib(2))
#print(fib(5))
#print(fib(20))