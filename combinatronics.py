prices = [10,3,25,30,30,25,12,25,18,
            # 18,18,18,18,25,15,22,10,30,
            # 40,25,25,28,28,28,28,50,25,
            # 25,25,35,30,8,6,6,6,6,18,
            # 16,12,10,15,15,15,16,12,
            ]

# FUNTION TO GET COMBINATIONS OF n LENGTH
def n_length_combo(input_list, n):
    # IF N IS EQUAL TO 0
    if n == 0:
        # RETURN LIST OF LISTS
        return [[]]
    # CREATE LIST OF COMBINATIONS (SETS)
    sets_list = []
    # ITERATE OVER LIST RANGE
    for i in range(0, len(input_list)):
        # M IS THE ITEM AT INDEX
        m = input_list[i]
        # REMAINING LIST
        remLst = input_list[i + 1:]
        # SET VARIABLE RECURSIVELY
        remainlst_combo = n_length_combo(remLst, n-1)
        # ITERATE OVER REMAINING NUMBERS
        for p in remainlst_combo:
            # APPEND M, *P TO LIST VARIABLE
            sets_list.append([m, *p])
    # RETURN LIST
    return sets_list

# FUNCTION TO GET COMBINATIONS WITHIN BOUNDARIES
def combination_check(low, high):
    # CALL THE N LENGTH COMBO FUNCTION TO GET ALL COMBINATIONS
    combinations = n_length_combo(prices, 3)
    # FILTER ONLY COMBINATIONS WITHIN BOUNDS, CONVER TO TUPLE TO USE set()
    correct_sets = [tuple(list) for list in combinations if sum(list) >= low and sum(list) <= high]
    # DELETE DUPLICATES
    correct_sets = set(correct_sets)
    # PRINT CORRECT COMBINATIONS
    for correct_set in correct_sets:
        print(correct_set)
    # PRINT MESSAGE
    print("There are {} possible combinations between {} and {}".format(len(correct_sets), low, high))

combination_check(70, 75)
