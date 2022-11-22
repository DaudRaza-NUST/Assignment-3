# Towers of Hanoi for n = 3 
s = [] #Starting pole
m = [] #Middle pole
e = [] #End Pole
j = 0
# num_of_plates = int(input("Enter the number of plates for Tower of Hanoi: "))
def move(pole1,pole2,num):
    print(num, "Move disc from", pole1, "pole to the", pole2, "pole\n", s, "\n", m, "\n", e)
num_of_plates = 3
min_moves = 2**num_of_plates-1
for i in range(num_of_plates):
    s.append(i+1)
print(s, "\n")
print("Minimum number of steps required:\n", min_moves)
for i in range(1,min_moves+1):
    if i%3==1:
        if j%2==0:
            e.append(s.pop())
            move('start', 'end',i)
        else:
            s.append(e.pop())
            move('end', 'start',i)
    elif i%3==2:
        if j%2==0: 
            s.append(m.pop())
            move('middle', 'start',i)
        else:
            m.append(s.pop())
            move('start', 'middle',i)
    else: 
        if j%2==0: 
            m.append(e.pop())
            move('end', 'middle',i)
        else:
            e.append(m.pop())
            move('middle','end',i)
    j += 1
# e.append(s.pop())
# move('start', 'end')
# s.append(m.pop())
# move('middle', 'start')
# e.append(m.pop())
# move('middle', 'end')
# e.append(s.pop())
# move('start', 'end')

   # elif i%3==1 and len(e)!=0 and s[-1]<e[-1]:
   #     s.append(e.pop())
   #     move('end', 'start')
   # elif i%3==2 and len(s)!=0:
   #     m.append(s.pop())
   #     move('start', 'middle')
   # elif i%3==2 and len(m)!=0 :
   #     s.append(m.pop())
   #     move('middle', 'start')
   # elif i%3==2 and len(s)!=0 and m[-1]<s[-1]:
   #     m.append(s.pop())
   #     move('middle', 'start')
   # elif i%3==0 and len(e)!=0 and e[-1]>m[-1]:
   #     m.append(e.pop())
   #     move('end', 'middle')
   # elif i%3==0 and len(e)!=0 and e[-1]<m[-1]:
   #     e.append(m.pop())
   #     move('middle', 'end')