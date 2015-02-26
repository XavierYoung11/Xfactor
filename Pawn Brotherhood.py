def safe_pawns(pawns):
    pawns_indexes = set()
    for i in pawns:
        row = int(i[1]) - 1
        #how the computer recoqnizes numbers
        col = ord(i[0]) - 97
        print (row,col)
        
        pawns_indexes.add((row, col))
        count = 0
        for row, col in pawns_indexes:
            #row - 1 = down left, down two over to the left
            is_safe = ((row - 1,col - 1) in pawns_indexes or (row -1, col + 1) in pawns_indexes)
            if is_safe:
                count += 1 
                
    return count 
    

