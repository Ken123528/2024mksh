a=[
   [1,1,1,2,2,2,2,1,1,1,1,2,2,2,2,1],
   [2,1,1,1,2,2,2,2,1,1,1,1,2,2,2,2],
   [2,2,1,1,1,2,2,2,2,1,1,1,1,2,2,2],
   [2,2,2,1,1,1,2,2,2,2,1,1,1,1,2,2]]
size(480,480)
for i in range (len(a)):
    for j in range(16):
        if a[i][j]==1:
            if(i+j)%2==1:fill(255)
            else:fill(0)
            rect(j*30,i*30,30,30)
            if(i+j)%2==1:fill(0)
            else:fill(255)
            rect(j*30+2,i*30+2,9,9)
            rect(j*30+19,i*30+19,9,9)
    
