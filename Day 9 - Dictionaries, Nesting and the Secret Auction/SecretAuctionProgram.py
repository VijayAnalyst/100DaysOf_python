from replit import clear # import clear function from replit

from art import logo #import logo from art.py

print(logo) #print logo

bids = {} #create empty dictionary
bidding_finished = False #create variable to check if bidding is finished
 
def find_highest_bidder(bidding_record): #create function to find highest bidder
  highest_bid = 0 #create variable to store highest bid
  winner = "" #create variable to store winner
  # bidding_record = {"Angela": 123, "James": 321}
  for bidder in bidding_record: #loop through each bidder in bidding_record
    bid_amount = bidding_record[bidder] #create variable to store bid amount
    if bid_amount > highest_bid: #check if bid amount is greater than highest bid
      highest_bid = bid_amount #if so, set highest bid to bid amount
      winner = bidder #set winner to bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}") #print winner and highest bid

while not bidding_finished: #while bidding is not finished
  name = input("What is your name?: ") #ask for name
  price = int(input("What is your bid?: $")) #ask for bid
  bids[name] = price #add name and bid to bids dictionary
  should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n") #ask if there are other bidders
  if should_continue == "no": #if no, set bidding_finished to True
    bidding_finished = True #if no, set bidding_finished to True
    find_highest_bidder(bids) #call find_highest_bidder function
  elif should_continue == "yes": #if yes, clear screen and start loop again
    clear() #if yes, clear screen and start loop again