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
    new_list = []
    greatest_num = list[0]
    for i in range(0,len(list)):
        if list[i] < 0:
            continue
        if list[i] > greatest_num:
            new_list.append(list[i])
            greatest_num = list[i]
    print(new_list)
    return new_list

visible_buildings([-1,1,5,3,4,7,6])

    #ZIP IT
    