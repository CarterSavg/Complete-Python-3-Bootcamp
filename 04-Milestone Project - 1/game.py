Board = [["", "", ""], ["", "", ""], ["", "", ""]]
end = False
while end == False:
    move = -1
    while 0 > int(move) < 8:
        try:
            move = input("Please enter a the square you want to use (eg, 0 - 8)")
        except ValueError:
            move = -1
    print(move)