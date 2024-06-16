n, m = map(int,input().split())

arr = list(map(int,input().split()))[:n]

if(m <= 6):
    n = 1
    
elif(m <= 36):
    n = 2
    
else:
    n = 3
    
divisor = 6

for i in range(n):
    dictionary = dict()
    # temp=[]

    for j in arr:
        dictionary[j] = j % divisor
        # print(dictt)

    divisor *= 6

    sorted_dictt = dict(sorted(dictionary.items(), key = lambda item: item[1]))
        
    print(*sorted_dictt.keys())