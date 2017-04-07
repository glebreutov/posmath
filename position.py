import json
from decimal import Decimal

from book import Book, Level
from posmath.side import Side
from marketmaker import MMParams


class Position:
    def __init__(self, pos=None, balance=None, price=None, side=None):
        if balance is None and price is None:
            raise RuntimeError

        if balance and price and pos:
            raise RuntimeError

        if balance is not None and pos is not None:
            self.pos = pos
            self.balance = balance
        elif pos is not None and price is not None:
            self.pos = pos
            self.balance = pos * price
        elif price is not None and balance is not None:
            self.pos = balance / price
            self.balance = balance

        if side is not None:
            self.pos = abs(self.pos) * Side.sign(side)
            self.balance = Side.opposite_sign(side) * abs(self.balance)

    def position(self):
        return self.pos

    def abs_position(self):
        return abs(self.pos)

    def side(self):
        return Side.side(self.pos)

    def opposite(self):
        return Position(-1 * self.pos, -1 * self.balance)

    def price(self):
        if self.pos == 0:
            return 0

        return round(abs(self.balance / self.pos), 4)

    def __add__(self, opposition):
        return Position(pos=self.pos + opposition.pos, balance=self.balance + opposition.balance)

    def __sub__(self, other):
        return self.__add__(other.__mul__(-1))

    def __mul__(self, other):
        return Position(pos=self.position() * other, balance=self.balance * other)

    def __div__(self, other):
        return Position(pos=self.position() / other, balance=self.balance / other)

    def __eq__(self, other):
        return self.pos == other.pos and self.balance == other.balance

    def __gt__(self, other):
        return self.balance > other.balance

    def __lt__(self, other):
        return self.balance < other.balance

    def margin(self, margin):
        return Position(pos=self.pos, balance=self.balance + margin)

    def oppoiste_with_price(self, price):
        return Position(pos=self.pos, price=price, side=Side.opposite(self.side()))

    def opposite_with_margin(self, margin):
        return Position(pos=-1 * self.pos, balance=-1 * self.balance + margin)

    def __str__(self):
        return json.dumps(
            {'balance': str(self.balance),
             'position': str(self.position()),
             'side': self.side(),
             'price': str(self.price())})


def BID(pos=None, balance=None, price=None):
    return Position(pos=pos, balance=balance, price=price, side=Side.BID)


def ASK(pos=None, balance=None, price=None):
    return Position(pos=pos, balance=balance, price=price, side=Side.ASK)






