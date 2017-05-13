import json
from decimal import Decimal


from posmath.side import Side


class Position:
    def __init__(self, pos=None, balance=None, price=None, side=None):
        assert pos is None or type(pos) in (str, Decimal, int)
        assert balance is None or type(balance) in (str, Decimal, int)
        assert price is None or type(price) in (str, Decimal, int)
        assert side is None or side in Side.sides
        if pos:
            pos = Decimal(pos)
        if balance:
            balance = Decimal(balance)
        if price:
            price = Decimal(price)

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

    def raw_price(self):
        if self.pos == 0:
            return 0

        return abs(self.balance / self.pos)

    #price rounded by 4 digits to side of quote
    def price(self):
        if self.pos == 0:
            return Decimal('0')

        prec = Decimal('10000')
        price, reminder = divmod(prec * abs(self.balance), abs(self.pos))
        price /= prec
        if reminder != 0:
            price += Side.sign(self.side()) * Decimal('0.0001')
        return round(price, 4)

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

    def fee_pos(self, fee):
        if fee > 0:
            return Position(pos=0, balance=self.balance / 100 * fee, side=Side.BID)
        else:
            return Position(pos=0, balance=0)


def BID(pos=None, balance=None, price=None):
    return Position(pos=pos, balance=balance, price=price, side=Side.BID)


def ASK(pos=None, balance=None, price=None):
    return Position(pos=pos, balance=balance, price=price, side=Side.ASK)






