def splictArr(arr,j,k):
    for i in range(0,k):
        x = arr[0]
        for j in range(0,n-1):
            arr[j]=arr[j+1]
            arr[n-1]=x
            arr=[12,10,5,6,53,37]
            n=len(arr)
            position=2
            splictArr(arr,n,position)
            for i in range(0,n):
                print(arr[i],end=' ')
