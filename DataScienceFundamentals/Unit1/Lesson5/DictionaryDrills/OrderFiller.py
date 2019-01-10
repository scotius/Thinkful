def fillable(stock, merch, n):
    #Test if merch is in dictionary
    if merch in stock.keys():
        #Test if merch value less than n
        if stock[merch] < n:
            return False
        else:
            return True
    else:
        return False
