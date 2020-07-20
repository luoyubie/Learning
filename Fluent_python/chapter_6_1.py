# _*_ coding:utf-8 _*_
# @Author: Bie
# @Time: 2020年07月14日

from abc import ABC, abstractmethod
from collections import namedtuple

Customer = namedtuple('Customer', 'name fidelity')


class LineItem:
    def __init__(self, product, quantity, price):
        self.product = product # 产品
        self.quantity = quantity # 数量
        self.price = price # 价格

    def total(self):
        return self.price * self.quantity


class Order:  # 上下文

    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion

    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion.discount(self)
        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())


class Promotion(ABC):  # 策略：抽象基类

    @abstractmethod
    def discount(self, order):
        """ 返回折扣金额(正值)"""


class FidelityPromo(Promotion):  # 第一个具体策略
    """为积分为1000或以上的顾客提供5%的折扣"""

    def discount(self, order):
        return order.total() * 0.05 if order.customer.fidelity >= 1000 else 0


class BulkItemPromo(Promotion):  # 第二个具体策略
    """单个商品为20个或以上时提供10%的折扣"""

    def discount(self, order):
        discount = 0
        for item in order.cart:
            if item.quantity >= 20:
                discount += item.total() * 0.1
        return discount


class LargeOrderPromo(Promotion):  # 第三个具体策略
    """订单中的不同商品达到10个或以上时提供7%的折扣"""

    def discount(self, order):
        distinct_items = {item.product for item in order.cart}
        if len(distinct_items) >= 10:
            return order.total() * 0.07
        return 0


if __name__ == "__main__":
    joe = Customer('John Doe', 0)
    ann = Customer('Ann Smith', 1100)
    cart = [LineItem('banana', 4, 0.5),
            LineItem('apple', 10, 1.5),
            LineItem('watermellon', 5, 5.0)]
    order1 = Order(joe, cart, FidelityPromo())
    print("order1: ",order1)
    order2 = Order(ann, cart, FidelityPromo())
    print("order2: ", order2)
    banana_cart = [LineItem('banana', 30, 0.5),
                   LineItem('apple', 10, 1.5)]
    order3 = Order(joe, banana_cart, BulkItemPromo())
    print("order3: ", order3)

    long_order = [LineItem(str(item_code), 1, 1.0)
                  for item_code in range(10)]
    order4 = Order(joe, long_order, LargeOrderPromo())
    print("order4: ",order4)

    order5 = Order(joe, cart, LargeOrderPromo())
    print("order5: ",order5)