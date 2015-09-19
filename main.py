def usdtry():
    
    import os
    os.system("cls")
    print("USDTRY Long Position Calculations")
    print("Leverage is taken 100  by default")
    print("=================================")
    first = float(input("Buy  price: "))
    last  = float(input("Sell price: "))
    lot   = float(input("Lot: "))
    position = lot * 100000
    margin = 2 * lot * 100000 / 100
    print("Required margin: ",margin, " USD")
    print("Position volume: ", position, " USD")
    profit = (last - first) * position
    print("Profit", "%.2f" % profit ,"TRY or ",  "%.2f" %(profit / last) , " USD")
    print("In order to lose all of your margin, the currency should fall to ", "%.4f" %(50 * first / 51))
    input()
    usdtry()
    

usdtry()
