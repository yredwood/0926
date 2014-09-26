
## FUNCTION :: GUGUDAN
# def timeTable(arg) :
# 	table = [] 
# 	for i in range(1, 10) : 
# 		table.append(str(arg) + " * " + str(i) + " = " + str(arg * i) );
# 	return table


# for j in range(2,6):
# 	for i in range(1,10): 
# 		print timeTable(j)[i-1] + "      " + timeTable(j+4)[i-1]
# 	print "-------------------------------"



# BUBLE SORTING
def bubbleSort(LIST) :
	for i in range(0, len(LIST)-1) :
		for j in range(len(LIST)-1, i,-1) :
			if LIST[j] < LIST[j-1] :
				tmp = LIST[j-1]
				LIST[j-1] = LIST[j]
				LIST[j] = tmp


LIST = [45,20,21,50,10,8,9,7,10]
bubbleSort(LIST)

print LIST



## Anothoer bubbleSort  :: Easy version 
# def a_bubble(my_list) :
# 	for i in range(0, len(my_list)-1):
# 		for j in range(0, len(my_list)-1):
# 			if my_list[j] > my_list[j+1] :
# 				tmp = my_list[j]
# 				my_list[j] = my_list[j+1]
# 				my_list[j+1] = tmp


# LIST = [45,20,21,50,10,8,9,7,10]
# a_bubble(LIST)
# print LIST


## QUICK SORTING
# def select(list, start, end):
#     pivot = list[end]                          
#     bottom = start-1                           
#     top = end                                  
#     dd_ = 0
#     while not dd_:                            
#         while not dd_:                        
#             bottom = bottom+1                  
#             if bottom == top:                 
#                 dd_ = 1                      
#                 break
#             if list[bottom] > pivot:           
#                 list[top] = list[bottom]      
#                 break                         
#         while not dd_:                        
#             top = top - 1                        
#             if top == bottom:                  
#                 dd_ = 1                       
#                 break
#             if list[top] < pivot:              
#                 list[bottom] = list[top]       
#                 break                          
#     list[top] = pivot                          
#     return top                                 


# def quick_sort(list, start, end):
#     if start < end:                            
#         split__ = select(list, start, end)  
#         quick_sort(list, start, split__-1)        
#         quick_sort(list, split__+1, end)
#     else:
#         return

# LIST = [45,20,21,50,10,8,9,7,10]
# quick_sort(LIST, 0, len(LIST)-1)
# print LIST