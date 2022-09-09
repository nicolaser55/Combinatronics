
food_prices = [5, 18,25,25, 50, 23,12, 12, 12,
                # 10,3,25,30,30,25,12,25,18,
                # 18,18,18,18,25,15,22,10,30,
                # 40,25,25,28,28,28,28,50,25,
                # 25,25,35,30,8,6,6,6,6,18,16,
                # 16,12,10,15,15,15,16,12,15,
                ]


# CHECK LIST OF NUMBERS
def set_check(list):
    # IF NUMBERS ARE ABOVE 60 BUT BELOW OR EQUAL TO 75
    if sum(list) > 60 and sum(list) <= 75:
        # RETURN TRUE BECAUSE IT FITS
        return True
    else:
        # RETURN FALSE BECAUSE IT DOES NOT FIT
        return False

correct_sets = []

# ITERATE OVER FOOD PRICES
for price1 in food_prices:
    # ASSIGN VARIABLE LIST 1
    list1 = [price1]
    # CHECK IF LIST FITS
    if set_check(list1) == True:
        # CHECK IF LIST NOT IN CORRECT SETS
        if list1 not in correct_sets:
            # APPEND LIST TO CORRECT SETS
            correct_sets.append(list1)
            # BREAK TO RESTART THE LOOP
            break
    # ITERATE OVER FOOD PRICES A SECOND TIME
    for price2 in food_prices:
        # ASSIGN VARIABLE LIST 2
        list2 = [price1, price2]
        # CHECK IF LIST FITS
        if set_check(list2) == True:
            # CHECK IF LIST NOT IN CORRECT SETS
            if list2 not in correct_sets:
                # APPEND LIST TO CORRECT SETS
                correct_sets.append(list2)
                # BREAK TO RESTART THE LOOP
                break
        # ITERATE OVER FOOD PRICES A THIRD TIME
        for price3 in food_prices:
            # ASSIGN VARIABLE LIST 3
            list3 = [price1, price2, price3]
            # CHECK IF LIST FITS
            if set_check(list3) == True:
                # CHECK IF LIST NOT IN CORRECT SETS
                if list3 not in correct_sets:
                    # APPEND LIST TO CORRECT SETS
                    correct_sets.append([price1, price2, price3])
                    # BREAK TO RESTART THE LOOP
                    break
            # ITERATE OVER FOOD PRICES A FOURTH TIME
            for price4 in food_prices:
                # ASSIGN VARIABLE LIST 4
                list4 = [price1, price2, price3, price4]
                # CHECK IF LIST FITS
                if set_check([price1, price2, price3, price4]) == True:
                    # CHECK IF LIST NOT IN CORRECT SETS
                    if list4 not in correct_sets:
                        # APPEND LIST TO CORRECT SETS
                        correct_sets.append([price1, price2, price3, price4])
                        # BREAK TO RESTART THE LOOP
                        break

print(correct_sets)
print("Length:",len(correct_sets))

str_list = ["".join(str(i)) for i in correct_sets]

print(str_list)

print("Set Length:",len(set(str_list)))



# set_check([12,32,43,32,5])
