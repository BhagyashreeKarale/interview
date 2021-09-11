#q1
# num=1
# while num<=10:
#     if num == 2 or num == 3:
#         num=num+1
#         continue
        
#     else:
#         print(num)
#     num=num+1
# #########################################################################################################
# #q2
# sentence = input ("Enter any sentence:\n")
# charlist = list (sentence)
# lower_letter=0
# upper_letter=0
# for i in charlist :
#     if i >= 'a' and i <= 'z' :
#         lower_letter = lower_letter + 1
#     elif i >= 'A' and i <= 'Z':
#         upper_letter=upper_letter+1
# print("In the given sentence there are",lower_letter,"small letters and",upper_letter,"upper letters.")
# ##########################################################################################################
# #q3
# sentence = input ("Enter any sentence:\n")
# charlist = list (sentence)
# for i in charlist:
#     if i == " ":
#         charlist.remove(i)
# for i in charlist:
    # print(i,end="")
##########################################################################################################
#q4
# num=int(input("Enter any number:\n"))
# numlist=list(str(num))
# if numlist[len(numlist)-2] == '3':
#     print("Yes")
# else:
#     print("No")
#########################################################################################################
#q5
# num=int(input("Enter a number:\n"))
# flist=[]
# for i in range(1,num+1):
#     for j in range(1):
#         flist.append(["A"+str(i),"B"+str(i)])
# print(flist)
##########################################################################################################
#q6
# clist=list(input("Enter a word:\n"))
# ulist=[]
# dic={}
# for i in clist:
#     if i not in ulist:
#         ulist.append(i)
#         count=0
#         for k in range(len(clist)):
#             if clist[k]==i:
#                 count=count+1
#         dic[i]=count
# print(dic)
#############################################################################################################
