from decimal import Decimal

from posmath.position import Position
from posmath.side import Side


def test_fee():
    def test_case(pos, order):
        fee_pos = order.fee_pos('0.18')
        print("pos " + str(pos))
        print("order " + str(order))
        print("fee " + str(fee_pos))
        wo_fee = pos + order
        w_fee = pos + order + fee_pos
        print("wo_fee " + str(wo_fee))
        print("w_fee " + str(w_fee))
        assert wo_fee.balance >= w_fee.balance, "pos "+str(pos) + " order" + str(order)
        assert (abs(fee_pos.balance) < abs(order.balance)) or (order.balance ==0 and fee_pos.balance==0)\
            , "fee " + fee_pos.balance+" order cost " + order.balance

    pos = Position(pos=Decimal('1'), balance=Decimal('1199'), side=Side.BID)
    order = Position(pos=Decimal('1'), balance=Decimal('1200'), side=Side.ASK)
    test_case(order, pos)
    print('---------')
    test_case(pos, order)
    print('---------')
    pos = Position(pos=Decimal('0.01'), balance=Decimal('1199'), side=Side.BID)
    order = Position(pos=Decimal('0.01'), balance=Decimal('1200'), side=Side.ASK)
    test_case(pos, order)
    print('---------')
    pos = Position(pos=Decimal('0.01'), balance=Decimal('12'), side=Side.BID)
    order = Position(pos=Decimal('0.01'), price=Decimal('1201'), side=Side.ASK)
    test_case(order, pos)
    print('---------')
    test_case(pos, order)
    print('---------')
    pos = Position(pos=Decimal('0'), balance=Decimal('0'), side=Side.BID)
    order = Position(pos=Decimal('0.01'), price=Decimal('1201'), side=Side.ASK)
    print("order fee " + str(order.fee_pos(Decimal('0.18')).balance))
    test_case(pos, order)
    print('---------')
    test_case(order, pos)
    assert pos + order == pos + order + order.fee_pos(0)