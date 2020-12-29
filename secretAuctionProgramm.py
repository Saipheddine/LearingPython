# Secret Auction Programm


keep_bidding = True
first_round = 1

def askForMoreBidders():
    yes_or_no = input("Are there any other bidders? Type 'yes' or 'no'\t")
    return yes_or_no.lower()


def addNewBidder(name, bid):
    new_bidder = {}
    new_bidder["name"] = name
    new_bidder["bid"] = int(bid)
    return new_bidder

bidders = {}
while keep_bidding:
    
    name = input("What's your name?\t")
    bid = input("What's your bid?\t")
    [bidders].append(addNewBidder(name, bid))
    yes_or_no = askForMoreBidders()
    if yes_or_no == "no":
        keep_bidding = False
        #print("The winner is {}".format(filter(bidders["name"] == bid, bidders)))
        print("{}".format([bidders]))




