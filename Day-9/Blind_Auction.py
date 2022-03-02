from replit import clear
#HINT: You can call clear() to clear the output in the console.
import art
print(art.logo)
print("Welcome to the Secret Auction Program")
users={}
condition= True
while condition==True:
    ask_user=str(input("What is your name? "))
    user_bid=int(input("What's your bid?: $"))
    users[ask_user]=user_bid
    to_continue=input("Are there any other bidders? Type 'yes' or 'no'. ")
    if to_continue =='no':
        condition=False
    elif to_continue =='yes':
        clear()


all_values=users.values()
max_value=max(all_values)
for key, value in users.items():
    if max_value==value:
        new_key= key
        print(f"The winner is {key} with a bid of ${value}.")

"""
###############The solution given by the Instructor#################

from replit import clear
from art import logo
print(logo)

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  # bidding_record = {"Angela": 123, "James": 321}
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid: 
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $"))
  bids[name] = price
  should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
  if should_continue == "no":
    bidding_finished = True
    find_highest_bidder(bids)
  elif should_continue == "yes":
    clear()
  
"""