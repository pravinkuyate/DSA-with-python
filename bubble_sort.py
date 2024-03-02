def bubble_sort(elements):                          
    counter=0
    size=len(elements)
    print("size is ",size+1)
    swapped=False
    for j in range(int(size/2)-1):
        for i in range(size-1-j):
            if elements[i] >elements[i+1]:
            #swap 
                tmp=elements[i]
                elements[i]=elements[i+1]
                elements[i+1]=tmp
                counter+=1
                swapped=True
        if not swapped:
            break
    print(counter)


if __name__=="__main__":

    elements=[88,78,1,89,56,1,3,54,6,8,9,7,98,95,8,58,1,3]
    bubble_sort(elements)
    print(elements)
    
