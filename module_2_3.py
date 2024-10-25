my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
null = 0
while null < len(my_list):
    if my_list[null] < 0:
        break
    elif my_list[null] == 0:
        null += 1
        continue
    print(my_list[null])
    null +=1