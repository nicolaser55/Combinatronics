prices = [5, 18,25,25, 50, 23,12, 12, 12,
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

# ITERATE OVER PRICES
def combinatronics(prices):
    # CREATE LIST OF CORRECT SETS
    correct_sets = []
    # ITERATE OVER NUMBERS
    for number in prices:
        print(number)


combinatronics(prices)
