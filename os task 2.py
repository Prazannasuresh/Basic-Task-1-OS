def deadornot(process):
    p=len(process)
    n=int(input("Enter the need or number of resources requred for each process for optimal processing:"))
    g=int(input("Enter the available number of resources:"))
    min= p*(n-1) + 1
    if g<min:
         print("Possibility of deadlock detected!")
    else:
        print("Safe from deadlock")
process=[2,3,4,5]
deadornot(process)

      
