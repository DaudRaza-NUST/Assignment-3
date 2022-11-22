def move(pole1,num):
    print("Move disc", num, "to the", pole1, "pole\n")

def H_tower(n):
    for i in range(1,n**2):
        j = 1
        k = i
        while (k%2==0):
            j += 1
            k = k/2
        if ((k + 1)/2%3==0):
            move("A", n+1-j)
        elif ((n+1-j)%2==1 and (k+1)/2%3==1 or (n+1-j)%2==0 and (k+1)/2%3==2):
            move("C", n+1-j)
        elif (n+1-j)!=0:
            move("B", n+1-j)
H_tower(int(input("Enter the number of discs:")))