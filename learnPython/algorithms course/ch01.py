## cpearring 

class sorts(object):
    @staticmethod
    def insertionSort( A ):
        for x in range(1,len(A)): ## IF YOU WERE WONDERING YES COPY PASTA 

            currentval = A[x] ## BECAUSE WHY DO REAL WORK
            pos = x

            while pos>0 and A[pos-1]>currentval:
                A[pos]=A[pos-1]
                pos = pos-1

            A[pos]=currentval
        return A
    
    @staticmethod
    def reverseInsertionSort( A ):
        for x in range(1,len(A)):

            currentval = A[x]
            pos = x

            while pos>0 and A[pos-1]<currentval: ## I think this is what you meant by reverse
                A[pos]=A[pos-1]
                pos = pos-1

            A[pos]=currentval
        return A

    @staticmethod
    def twonumbersort( A ):
        ## also can make an if statement in the insert sort if len(A) == 2
        ## ONLY USE THIS FOR TWO NUMBERS
        if A[1] > A[2]: ## WWWOOOOO IF STATEMENTS
            x = A[2]
            A[2] = A[1]
            A[1] = x
        return A