# -*- coding: utf-8 -*-
from thsauto import ThsAuto

import time

if __name__ == '__main__':
    
    auto = ThsAuto()                                        # 连接客户端

    print('可用资金')
    print(auto.get_balance())                               # 获取当前可用资金
    print('持仓')
    print(auto.get_position())                              # 获取当前持有的股票

    print('卖出')
    print(auto.sell(stock_no='162411', amount=200, price=0.4035))   # 卖出股票
    
    print('买入')
    result = auto.buy(stock_no='162411', amount=100, price=0.41)    # 买入股票
    print(result)

    if result and result['success']:                                # 如果买入下单成功，尝试撤单
        print('撤单')
        print(auto.cancel(entrust_no=result['entrust_no']))

