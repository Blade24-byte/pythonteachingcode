# create, call and test fishstore() function 

# function used earlier in module
def title_it_rtn(msg):
    return msg.title()

def fishstore(fish, price):
    return ('Fish Type: ' + title_it_rtn(fish) + ' costs $' + price)

fish_entry = input("Fish name? ")
price_entry = input("Price? ")
fish_log = fishstore(fish_entry, price_entry)
print (fish_log)


