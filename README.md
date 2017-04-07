# Positon math
Arithmetic operations on market positions.

More precise doc coming soon

## Side

## Position
You can do arithmetic operations on market positions.

## Defining a positions
```Position(pos=10, balance=-100)```

would give you 

```{"balance": "-100", "position": "10", "side": "B", "price": "10.0"}```

this equals to
 
 ```BID(pos=10, balance=100)```
 
 BID is just a wrapper for 
 
 ```Position(pos=10, balance=100, side=Side.BID)```
 
 same for other side
 
 ```Position(pos=-10, balance=100)```
 
 or 
 
 ```ASK(pos=10, balance=100)```
 
 would give you a
 
 ```{"balance": "100", "position": "-10", "side": "S", "price": "10.0"}```
 
 ## Operations on positions
 You can add or substract positons.
 
 For example is you bought something for $99 and sell for $100.
 You'll get a position 0 and balance 1$. Congrats you just get $1!
 
 ```BID(pos=10, balance=99) + ASK(pos=10, balance=100)```
 
 You also can substract positions:
 
 ```BID(pos=10, balance=99) - BID(pos=10, balance=100)```
 
 is equals to 
 
 ```BID(pos=10, balance=99) + ASK(pos=10, balance=100)```
 
 besides that you can multipy and divide positions by numbers
 
 ```BID(pos=10, balance=99) * 0.1```
 
