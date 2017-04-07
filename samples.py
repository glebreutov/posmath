from posmath.position import Position, BID, ASK

print(Position(pos=10, balance=-100))
print(BID(pos=10, balance=100))
print(Position(pos=-10, balance=100))
print(ASK(pos=10, balance=100))
print(BID(pos=10, balance=99) + ASK(pos=10, balance=100))