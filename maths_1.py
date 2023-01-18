# 1.GCD of numbers
# 2.Prime Numbers
# 2.LCM of numbers
# 3.Combinations of numbers
# 4.Permutations of numbers

from math import sqrt

class Math:

    def GCD(self,a,b):
        #25,50->25
        #30 45-> 15
        sol=1
        for i in range(min(a,b),2,-1):
            if(a%i==0 and b%i==0):
                sol=i
                break

        return sol
        #Time complexity-> O(min(a,b))

    def gcd1(self,a,b):
        if a==b:
            return a

        if(a<b):
            return self.gcd(a,b-a)
        else:
            return self.gcd(a-b,b)

    def gcd2(self,a,b):

        if(b==0):
            return a

        return self.gcd2(b,a%b)    
        #Eucliedian Formula-> O(log(min(a,b)))
        

    ##Sieve of erastosis   
    # if N is prime -> 1 Underroot N -> no factor
    def prime(self,a):
        for i in range(1,sqrt(a)):
            if a%i==0:
                return False

        return True

     ##Sieve of erastosis
     #Mainly used for finding prime numbers in a specific range
     #Comlexity->o(sqrt(n))
    def prime2(self,n):
        isPrime=[False]*(n+1)
        isPrime[0]=True
        isPrime[1]=True
        for i in range(2,int(sqrt(n))+1):
            for j in range(2*i,n+1,i):
                isPrime[j]=True
        return isPrime
        #Complexity: prime-> O(nlog(log(n)))


    
    def fast_power(self,base,power):
        mod=1000000007
        result=1
        while(power>0):
            if(power%2==1): #b&1 -> binary less expesnive
                result=(result*base%mod)%mod
            
            base=(base%mod*base%mod)%mod
            power=power//2   
           
            #print(result)
        return result
        #complexity->O(log(power))

    def combination_numbers(self,arr,n):

            pass

    def permutation_numbers(self,arr,n):
            pass

if __name__ == "__main__":
    math=Math()        
    arr=math.prime2(10)
    for i in range(0,len(arr)):
        if(arr[i]==False):
            print(i)
    print(math.gcd2(15,20))   
    print(math.fast_power(2,5))     






