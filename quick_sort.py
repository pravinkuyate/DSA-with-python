#it uses divide and concor approch
#there are two types of partition in it 
'''1) hoare partition
2)lomuto partition'''
def swap(a,b,arr):
    if a!=b:
        tmp=arr[a]
        arr[a]=arr[b]
        arr[b]=tmp


def partition(elements):
    pivot_index=0
    pivot=elements[pivot_index]
    start= pivot_index+1
    end=len(elements)-1
    while start<end:
        while elements[start]<=pivot:
            start+=1

        while elements[end]>pivot:
            end -=1
        
        if start<end:
            swap(start,end,elements)
        
    swap(pivot_index,end,elements)


def quick_sort(elements):
    partition(elements)

if __name__=="__main__":
    elements=[11,9,29,7,2,15,28]
    quick_sort(elements)
    print(elements)

