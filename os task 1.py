def wait(process,n,bt,wt):
    wt[0]=0
    for i in range(1,n):
        wt[i]=bt[i-1] + wt[i-1]
def turn(process,n,bt,wt,tat):
    for i in range(n):
        tat[i] = bt[i] + wt[i]
def avg(process,n,bt):
    wt=[0]*n
    tat = [0]*n 
    total_wt = 0
    total_tat = 0
    wait(process, n, bt, wt)
    turn(process, n, bt, wt, tat)
    print( "Process Burst time " + " Waiting time " +" Turn around time")
    for i in range(n):
        total_wt = total_wt + wt[i]
        total_tat = total_tat + tat[i]
        print( str(i + 1) + "\t\t" +  str(bt[i]) + "\t " + str(wt[i]) + "\t\t " +str(tat[i]))
    print( "Average waiting time = ",total_wt / n)
    print("Average turn around time = ",total_tat / n)
process = [10,12,87]
n = len(process)
bt = [24,12,99]
avg(process, n, bt)
 
    
