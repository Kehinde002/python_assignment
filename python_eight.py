for digit_one in range(1, 10):
    for digit_two in range(0, 10):
        for digit_three in range(0, 10):
            digit_one_square = digit_one * digit_one
            digit_two_square = digit_two * digit_two
            digit_three_square = digit_three * digit_three
            
            sum_digit_square = digit_one_square + digit_two_square + digit_three_square
            
            hundred = 100 * digit_one
            tenth = 10 * digit_two
            unit = digit_three
            number = hundred + tenth + unit
            
            if sum_digit_square == number:
                print(number, end="")

