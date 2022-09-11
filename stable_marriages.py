import numpy as np

women = ['A', 'B', 'C', 'D']
men = ['a', 'b', 'c', 'd']

pref = {'A':[0,1,2,3],'B':[1,0,2,3],'C':[1,2,3,0],'D':[0,3,2,1],
        'a':[1,3,0,2],'b':[0,1,2,3],'c':[1,0,2,3],'d':[0,1,3,2]}

m_matches = [0,0,0,0]
w_matches = [0,0,0,0]
is_rejected = [1,1,1,1]
engaged = np.zeros([len(men),len(women)])
print("Start with all men in the rejected state")
round = 0
while sum(is_rejected)>0:
    round += 1
    print("\nRound",round)
    for m in range(len(men)):
        if is_rejected[m]==1:
            pref_list = pref[men[m]]
            pref_list = np.argsort(pref_list)
            for w in pref_list:
                if engaged[m,w]==0:
                    engaged[m,w]=1
                    print(men[m],"proposes to",women[w])
                    is_rejected[m]=0
                    break

    for w in range(len(women)):
        pref_list = pref[women[w]]
        pref_list = np.argsort(pref_list)
        flag = 0
        for m in pref_list:
            if flag==0 and engaged[m,w]==1:
                flag = 1
            elif flag==1 and engaged[m,w]==1:
                engaged[m,w] = -1
                print(women[w],"rejects",men[m])
                is_rejected[m] = 1

    for m in range(len(is_rejected)):
        if is_rejected[m]==1:
            print(men[m],"is still rejected.")
            
#print(engaged)
print("\nDone!\n")
for m in range(engaged.shape[0]):
    for w in range(engaged.shape[1]):
        if engaged[m,w]==1:
            print(men[m],"<-->",women[w])
    
            
            
        
                
            
