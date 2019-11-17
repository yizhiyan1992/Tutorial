import numpy as np
import os
print(os.getcwd())
import matplotlib.pyplot as plt
plt.plot([0,5000],[0.9,0.9],c='r')
plt.xlim(0,5000)
plt.ylim(0.5,1)
vote_p=[1]*520000
vote_n=[-1]*480000
vote=vote_p+vote_n
#np.random.seed(42)
Final_Result=[]
for k in range(50):
    number=(k+1)*100
    print(number)
    Result=0
    Iteration=1000
    for _ in range(Iteration):
        R = np.random.randint(0, len(vote), number)
        #print(Result)
        temp=0
        for i in R:
            if vote[i]==1:
                temp+=1
        #print(temp)
        if temp>=0.5*number:
            Result+=1
    Final_Result.append(Result/Iteration)
    print(number,Final_Result)
plt.plot([(i+1)*100 for i in range(50)],Final_Result)
plt.xlabel('Sample Size')
plt.ylabel('Probability')
plt.savefig(r'C:/Users/Zhiyan/Desktop/Ad.png')
plt.show()
