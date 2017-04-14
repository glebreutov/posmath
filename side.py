class Side:
    BID = 'B'
    ASK = 'S'
    NONE = 'N'
    sides = (BID, ASK)

    @classmethod
    def check_fail(cls, side):
        if side not in Side.sides:
            raise RuntimeError

    @classmethod
    def sign(cls, side):
        return 1 if side == Side.BID else -1

    @classmethod
    def opposite_sign(cls, side):
        return Side.sign(side)*-1

    @classmethod
    def apply_sides(cls, func):
        map(func, Side.sides)

    @classmethod
    def side(cls, position):
        return Side.BID if position > 0 else Side.ASK

    @classmethod
    def opposite_side(cls, pos):
        return Side.opposite(Side.side(pos))

    @classmethod
    def opposite(cls, side):
        return Side.BID if side == Side.ASK else Side.ASK

    @classmethod
    def closer_to_quote(cls, side, price1, price2):
        if price1 - price2 == 0:
            return price1

        delta = (price1 - price2) / abs(price1 - price2)

        if delta == Side.sign(side):
            return price1
        elif delta == Side.sign(Side.opposite(side)):
            return price2
        else:
            raise RuntimeError