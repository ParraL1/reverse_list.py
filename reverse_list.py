#Name: Lilliana Parra
#Github username: ParraL1
#Date: 02/16/2022
#Description: reverses the elements in a list

def reverse_list(list_1):
    i = 0
    j = len(list_1)-1
    while(i<j):
        tmp = list_1[i]
        list_1[i] = list_1[j]
        list_1[j] = tmp
        i+=1
        j-=1

