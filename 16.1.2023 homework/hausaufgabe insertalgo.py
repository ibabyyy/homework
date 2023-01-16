mylist = [1,4,7,5,3,21,6,45,67,9]


index = 1


while index < len(mylist):
    index2 = 0
    while index-index2 >= 1:
        if mylist[index-index2] < mylist[index-1-index2]:
            mylist[index-index2], mylist[index-1-index2] = mylist[index-1-index2], mylist[index-index2]
        else:
            break 
        index2 = index2+1 
            

    index = index+1


print(mylist)





#while index 1 > oder == als index links daneben dann vertausche index 1 mit links daneben, wenn nicht
#springe zu nächsten index und vergleiche mit links daneben solange bis du bei index0bist
#dann springe zu nächsten index, weiderhole solange bis (len(mylist)) durch ist