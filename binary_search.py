


def binary_search(li,x):
    left_index=0
    right_index=len(li)-1
    mid_index=0
    
    while left_index <= right_index:
        mid_index= (left_index+right_index)//2

        mid_num=li[mid_index]

        if mid_num==x:
            return mid_index
        
        if mid_num< x:
            left_index=mid_index +1
        
        else:
            right_index=mid_index-1

    return -1


        
        

    
    
if __name__ =="__main__":
    li=[10,20,30,40,45,50,56,70,78,96]
    x=50
    index=binary_search(li,x)

    print(index)
  
