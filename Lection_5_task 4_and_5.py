#task_4
import random
def dice_roll():
    roll=random.randint(1, 6)
    return(roll)

print(dice_roll())


#Task_5
n_1,n_2,n_3 ,n_4 ,n_5 ,n_6=0,0,0,0,0,0
for i in range (1000):
    a=dice_roll()
    if a == 1:
        n_1 += 1
    elif a == 2:
        n_2 += 1
    elif a == 2:
        n_2 += 1
    elif a == 3:
        n_3 += 1
    elif a == 4:
        n_4 += 1
    elif a == 5:
        n_5 += 1
    elif a == 6:
        n_6 += 1
    
print(n_1 , n_2 , n_3 , n_4 ,n_5 ,n_6)