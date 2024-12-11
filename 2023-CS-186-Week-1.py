                          # 2023-Cs-186 Task 1
                
def  SearchA(array , number,emptyArray=None,index=0):
    
    if(emptyArray is  None):
      emptyArray=[]
        
    if(index == len(array)) :
        return emptyArray
    
    else :
     
        if(array[index] == number):
            emptyArray.append(index)
    return SearchA(array,number,emptyArray,index+1)

array = [22,2,1,7,11,13,5,2,9]
number = 2

print(' Index:',SearchA(array, number) )


                       # 2023-Cs-186 Task 2
                       
#if input array in question number 1 is already sorted [1,2,2,5,7,9,11,13,22] , so by applying
# binary search  , 
# so by O(log n ) , where n = 9   
# log₂(9) ≈ 3.17
# so in the worst case, binary search will check 4 elements.

 
                        # 2023-Cs-186 Task 3
                        
def Minimum(array,StartingIndex,EndingIndex,min =0):
    if(min == 0 ) :
        min = array[StartingIndex]
    if(StartingIndex == EndingIndex+1) :
        return min
    else :
        if(min > array[StartingIndex]):
            min = StartingIndex
         
    return Minimum(array,StartingIndex + 1 , EndingIndex,min)
                            
array = [3,4,7,8,0,1,23,-2,-5]
StartingIndex= 4
EndingIndex= 8
print('Output : ',Minimum(array,StartingIndex,EndingIndex))



                        
                       # 2023-Cs-186 Task 4
                       
def sort(array,currIndex=0):
    if(currIndex == len(array)-1):
        return array
    
    minIndex = currIndex
    for i in range(currIndex+1,len(array)):
        if(array[i]<array[minIndex]):
            minIndex = i 
    array[currIndex ],array[minIndex] = array[minIndex],array[currIndex ]
    return sort(array,currIndex+1)   

array =  [3,4,7,8,0,1,23,-2,-5]   
print('Sorted array : ' , sort(array) )    
 
                   # 2023-Cs-186 Task 5
                   
def StringReverse(str, starting, ending,newStr="")  :
   if(ending == starting-1):
       return newStr
   else :
       newStr = newStr + str[ending]

   return  StringReverse(str,starting,ending-1,newStr) 

print(StringReverse("University of Engineering and Technology Lahore",0,17))

            #    2023-Cs-186 Task 6

   
def SumRecursive(number,n=0):
    
    if(number == 0):
        return n 
    else :
        n = n + (number % 10 )
    
    return SumRecursive(number // 10,n )

number = 1524
print(SumRecursive(number) )


def SumIterative(num):
   n = 0
   while(num != 0):
     n = n + (num % 10)
     num = num //10
    
   return n
    
num = 1524
print(SumIterative(num) )   

                   # 2023-Cs-186 Task 7
                   
def   RowWiseSum(Mat,numRows=0,array=[]) :
    sum = 0
    rows =   len(Mat)
    if(numRows == rows):
        return array
   
    else :
        for i in range(rows):
           sum = sum + Mat[numRows][i]
        array.append(sum)     
    return RowWiseSum(Mat,numRows+1,array)



Mat =[[1,13,13],[5,11,6],[4,4,9]]                 
print('Row-wise : ',RowWiseSum(Mat)  )

def   ColumnWiseSum(Mat,numColumns=0,array=[]) :
    sum = 0
    columns =   len(Mat[0])
    if(numColumns == columns):
        return array
   
    else :
        for i in range(columns):
           sum = sum + Mat[i][numColumns]
        array.append(sum)     
    return ColumnWiseSum(Mat,numColumns+1,array)

Mat =[[1,13,13],[5,11,6],[4,4,9]]                 
print('Column-wise : ',ColumnWiseSum(Mat)  )


                         # 2023-Cs-186 Task 8
                         #Iteratively
                         
def SortedMerge(arr1, arr2):
   sortedArray = []
   indexA = 0
   indexB  = 0 
   
   while(indexA < len(arr1) and indexB < len(arr2)):
       if(arr1[indexA] <= arr2[indexB]):
           sortedArray.append(arr1[indexA])
           indexA+=1
       else:
             sortedArray.append(arr2[indexB])
             indexB+=1
         
   while(indexA < len(arr1))  :
        sortedArray.append(arr1[indexA])
        indexA+=1   
   while(indexB < len(arr2)) :
        sortedArray.append(arr2[indexB])
        indexB+=1  
                 
   return sortedArray   
                    #   Recursively     
def SortedMerge(arr1, arr2,newArray=[],i=0,j=0):
    
    if(len(newArray) == len(arr1)+len(arr2))  :
        return newArray
    
    while(i < len(arr1) and j < len(arr2)):
        if(arr1[i] <= arr2[j]) :
            newArray.append(arr1[i]) 
            i=i+1
        else :
            newArray.append(arr2[j]) 
            j=j+1 
    if(i < len(arr1))  :
              newArray.append(arr1[i]) 
              i=i+1
    if(j < len(arr2)) :
            newArray.append(arr2[j]) 
            j=j+1         
    return    SortedMerge(arr1, arr2,newArray,i,j)       


A = [0, 3, 4, 10, 11]
B = [1, 8, 13, 24]
print(SortedMerge(A, B))

                           # 2023-Cs-186 Task 9
                           
def PaLindRomRecursive(str):
   if(len(str) <=1):
       return 1
   if(str[0]==str[-1]):
       return PaLindRomRecursive(str[1:-1])
   else:
       return 0  


result = PaLindRomRecursive('radar')
if(result):
    print('palindrome')
else:
    print('not a palindrome')    

                                     # 2023-Cs-186 Task 10
                                     
def Sort10(posArray,negArray,i=0,j=0,newArray=[]):
    if(len(newArray) == len(negArray)+ len(posArray)) :
        return newArray
   
   
    if(i < len(posArray) and j < len(negArray)):
        newArray.append(negArray[j])
        newArray.append(posArray[i])
        return Sort10(posArray, negArray, i + 1, j + 1, newArray)
    if(i < len(posArray)) :
           newArray.append(posArray[i])
           return Sort10(posArray, negArray, i + 1, j, newArray)
    if(j < len(negArray)) :
        newArray.append(negArray[j]) 
        return Sort10(posArray, negArray, i , j+1, newArray)     
      
    
                                     
def sorting(Arr):
       posArray =[]
       negArray=[]
       for i in Arr:
        if(i < 0 ):
            negArray.append(i)
        else: 
             posArray.append(i) 
        negArray.sort() 
        posArray.sort() 
       return Sort10(posArray,negArray)
  
Arr =[10, -1, 9, 20, -3, -8, 22, 9, 7]
print(sorting(Arr))
                        