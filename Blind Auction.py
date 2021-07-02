bids = {}                           #empty dict
bidding_finished = False

def highest_bidder(bidding_record):
    highest_bidder = 0
    winner = ""

    for bidder in bidding_record:
        bidding_amount = bidding_record[bidder]
        if bidding_amount > highest_bidder:
            highest_bid = bidding_amount
            winner = bidder
    print(f"The winner is {winner} with winning bids of {highest_bid}")

while not bidding_finished:
    # take input from user and add name and amount to dictionary
    bidder = input("Enter your name: ")
    bid_amount = int(input("Enter bids amount: "))
    bids[bidder] = bid_amount

    choice = input("are there more bidders: (y/n)")
    if choice == "n":
        bidding_finished = True             #breaks the while loop
        highest_bidder(bids)
