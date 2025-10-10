# num=[16,17,4,3,5,2]
# lis=[]
# lis.append(num[-1])
# for i in range(len(num)-1,-1,-1):
#     for j in range((len(num)-2),-1,-1):
#         if num[i]>num[j]:
#             print(lis.append(num[i]))
            
# print(lis)


#leader done

lis=[]
num = [16, 17, 4, 3, 5, 2]
max_from_right = num[-1]
lis.append(max_from_right)

for i in range(len(num)-2, -1, -1):
    if num[i] > max_from_right:
        lis.append(num[i])
        max_from_right = num[i]
print(lis)






        
