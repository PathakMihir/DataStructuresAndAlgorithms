"""
Find the pattern and analyze all the questions
Number of questions doesnt matter

"""
9/15
Backlogs 

1.# You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation. Pattern evaluate Post fix
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[] 
        #print(tokens)
        mapper={}
        mapper["*"]="*"
        mapper["-"]="-"
        mapper["+"]="+"
        mapper["/"]="/"
        while(len(tokens)!=0):
            if tokens[0] not in mapper:
                stack.append(tokens.pop(0))
               
            else:
        
                #print(stack)
                y=int(stack.pop())
                x=int(stack.pop())
                #print(x,y)
                if tokens[0]=="*":
                    sol=x*y

                if tokens[0]=="/":
                    sol=int(x/y)

                if tokens[0]=="+":
                    sol=x+y

                if tokens[0]=="-":
                    sol=x-y

                tokens.pop(0)
                stack.append(str(sol))
                
       
        return int(stack[0])
            
2.# Combination Sum with a twist. Pattern recursion
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        self.ans=[]
        self.helper(k,n,1,[])
        return self.ans
        
    def helper(self,k,n,t,sol):
        
        if(n<0):
            return 
        
        if(len(sol)>k):
            return 
        
        if(len(sol)==k and n==0):
            self.ans.append(sol[::])
        
        for i in range(t,10):
            #print(i)
            sol.append(i)
            self.helper(k,n-i,i+1,sol)
            sol.pop()

3.# Bulls and Cows 

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls=0
        cows=0
        mapper={}
        correct=[]
        temp=guess
        count=set()
        for i in range(0,len(secret)):
            if(secret[i]==guess[i]):
                count.add(i)
                bulls+=1
            else:
                if(secret[i] not in mapper):
                    mapper[secret[i]]=1
                else:
                    mapper[secret[i]]+=1
 
        for i in range(0,len(guess)):
            if(guess[i] in mapper and i not in count):
                mapper[guess[i]]-=1
                if(mapper[guess[i]]==0):
                    del mapper[guess[i]]
                cows+=1
            

        return str(bulls)+"A"+str(cows)+"B"

4.# You are given an integer array nums of length n. Return maximum length of Rotation Function. Pattern Prefix Sum
class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        
        total=sum(nums)
        print(total)
        prefix_sum=0
        for i in range(0,len(nums)):
            prefix_sum+=nums[i]*i
        
        sol=prefix_sum
        for i in range(1,len(nums)):
            print(prefix_sum)
            prefix_sum=prefix_sum+total-(nums[-i]*(len(nums)))
            sol=max(prefix_sum,sol)
        
        return sol    

5.# Largest Divisible Subset. hard
#334. Increasing Triplet Subsequence
# Longest Increasing Subsequence-> pattern 
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if(len(nums)==1):
            return nums
        nums.sort()
        print(nums)
        dp=[1]*len(nums)
        temp=[-1]*len(nums)
        
        imax=0
        
        for i in range(1,len(nums)):
            
            for j in range(0,i):                
                 if(nums[i]%nums[j]==0):
                    #print(i,j)
                    if(dp[j]+1>dp[i]):
                        dp[i]=dp[j]+1
                        temp[i]=j
            
            if dp[imax]<dp[i]:
                imax=i
                
            
        sol=[]
        print(temp)
        print(dp)
        count=0
                
                
        
        while(imax!=-1):
            sol.append(nums[imax])
            imax=temp[imax]
            
        return sol[::-1]           
            
6.# How to find a perfect Rectangle. hard

7.# Scheduling a Course. Pattern Topological Sorting and Detect cycle
class Solution: 
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        self.graph={}
        
        for i in range(0, numCourses):
            self.graph[i]=[]
        
        for x,y in prerequisites:
            self.graph[x].append(y)
        self.cycle=0
        visited=[0]*numCourses
        
        for vertex in self.graph:
            
            if self.cycle==1:
                return False
            self.dfs(vertex,visited)
                
        return True     
         
    def dfs(self,source,visited):
        
        if self.cycle==1:
            return 
        
        if visited[source]==1:
            self.cycle=1
        
        if visited[source]==0:    
            visited[source]=1
            if source in self.graph:
                for vertex in self.graph[source]:
                    self.dfs(vertex,visited)

                visited[source]=2        

8.# Profitable Path in a Tree.

9.# Number of Pairs satisfying Inequality.

10.# Shortest Unsorted continuous Subarray.

11.# Number of ways to arrive at a Destination. Pattern Djiskstra 
class Node:
    def __init__(self,vertex,weight):
        self.vertex=vertex
        self.weight=weight
        
    def __lt__(self,other):
        return self.weight<other.weight
    
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph=defaultdict(list)
        for u,v,t in roads:
            graph[u].append([v,t])
            graph[v].append([u,t])
            
        
        heap=[]
        dist=[float("inf")]*n
        dist[0]=0
        heappush(heap,Node(0,0))
       
        
        ways=[0]*n
        ways[0]=1
        seen=set()
        
        while(len(heap)!=0):
            
            node=heappop(heap)
            
            if node in seen:
                continue
            
            for neighbours in graph[node.vertex]:
                next_weight=neighbours[1]+node.weight
                
                if dist[neighbours[0]]>next_weight:
                    dist[neighbours[0]]=next_weight
                    heappush(heap,Node(neighbours[0],next_weight))
                    ways[neighbours[0]]=ways[node.vertex]
                    
                elif dist[neighbours[0]]==next_weight :
                    ways[neighbours[0]]=(ways[neighbours[0]]+ways[node.vertex])%(pow(10,9)+7)
            seen.add(node)     
        return ways[n-1]

12.# Longest Happy Prefix
   #KMP algorithm

13.# Seat Arrangement in a SpiceJet Problem - Online OA February ‘22 Pattern Probability
    #Maths



14.# Deletions to make an array divisible. ->Pattern  GCD
class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        g=gcd(*numsDivide)
        nums.sort()
        for i in range(0,len(nums)):
            if g%nums[i]==0:
                return i
        return -1    
    def gcd(self,a,b):
        if(a==0):
            return b
        else:
            return self.gcd(b%a,a)

15.# Substrings containing all three Characters Pattern Hashmap

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        mapper={}
        i=0
        j=0
        count=0
        
        while(i<len(s)):
            #print(i,j)
            while(len(mapper)<3 and j<len(s)):
                if(s[j] not in mapper):
                    mapper[s[j]]=0
                mapper[s[j]]+=1
                j+=1
            #print(mapper)    
                

            if(len(mapper)==3):
                count+=len(s)-j+1
            
            mapper[s[i]]-=1
            if mapper[s[i]]==0: 
                del mapper[s[i]]
            i+=1
        
        return count
    
            



#Patterns which you learn from these problems and how to use them.
#              
                
            
            


