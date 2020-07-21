# _*_ coding:utf-8 _*_
# @Author: Bie
# @Time: 2020年07月20日

from collections import namedtuple


class LineItem:

    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.quantity * self.price


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
            discount = self.promotion(self)
        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())


def fidelity_promo(order):
    """为积分为1000或以上的顾客提供5%的折扣"""
    return order.total() * 0.05 if order.customer.fidelity >= 1000 else 0


def bulk_item_promo(order):
    """单个商品为20个或以上时提供10 % 的折扣"""
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * 0.1
    return discount


def large_order_promo(order):
    """订单中的不同商品达到10个或以上时提供7%的折扣"""
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * 0.07
    return 0


def best_promo(order):
    """选择可用的最佳折扣"""
    promos = [fidelity_promo, bulk_item_promo, large_order_promo]
    # discount_dict = {}
    # for promo in promos:
    #     discount_dict[promo.__name__] = promo(order)
    # discount = max(discount_dict[key] for key in discount_dict.keys())
    # for key in discount_dict.keys():
    #     if discount_dict[key] == discount:
    #         print(key)
    return max(promo(order) for promo in promos)


if __name__ == "__main__":
    Customer = namedtuple("Customer", "name fidelity")
    joe = Customer('John Doe', 0)
    ann = Customer('Ann Smith', 1100)
    cart = [LineItem('banana', 4, 0.5),
            LineItem('apple', 10, 1.5),
            LineItem('watermellon', 5, 5.0)]
    order1 = Order(joe, cart, fidelity_promo)
    print("order1: ", order1)
    order2 = Order(ann, cart, fidelity_promo)
    print("order2: ", order2)
    banana_cart = [LineItem('banana', 30, 0.5),
                   LineItem('apple', 10, 1.5)]
    order3 = Order(joe, banana_cart, bulk_item_promo)
    print("order3: ", order3)

    long_order = [LineItem(str(item_code), 1, 1.0)
                  for item_code in range(10)]
    order4 = Order(joe, long_order, large_order_promo)
    print("order4: ", order4)

    order5 = Order(joe, cart, large_order_promo)
    print("order5: ", order5)

    order6 = Order(joe, long_order, best_promo)
    print("order6: ", order6)

    promos = [globals()[name].__name__ for name in globals()
              if name.endswith('_promo')
              and name != 'best_promo']
    print(promos)
