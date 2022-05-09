import random

#SHUFFLE
def shuffle(list):
    new_list = []
    for i in range(0,len(list),1):
        rand_num = random.randint(0,len(list)-1)
        new_list.append(list[rand_num])
        temp = list[rand_num]
        list[rand_num] = list[len(list)-1]
        list[len(list)-1] = temp
        list.pop()
    print(new_list)

shuffle([1,2,3,4,5])

#SKYLINE HEIGHTS
def visible_buildings(list):
    visible_list = []
    for i in range(0,len(list)):
        if : #value is greater than zero AND greater than the number that comes before it in the list
            visible_list.append(i)
        else:
            continue
    print(visible_list)

    visible_buildings([-1,1,1,7,3])

    #ZIP IT
    