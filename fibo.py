# -*- coding: utf-8 -*-

""" 
fibonacci
"""

import profile

def simple_fibo(num):
    if num <= 2:
        return 1
    else:
        return simple_fibo(num - 1) + simple_fibo(num - 2)

def fibo(num):
    result_strage = {}
    def _fibo(num):
        if num in result_strage:
            return result_strage[num]
        if num <= 2:
            result_strage[num] = 1
            return result_strage[num]
        else:
            temp_result = _fibo(num - 1) + _fibo(num - 2)
            result_strage[num] = temp_result
            return temp_result
    return _fibo(num)

def yield_fibo(num):
    def _fibo():
        a , b = 1 , 1
        while 1:
            yield a
            a, b = b, a + b

    g = _fibo()
    for i in range(num):
        result = g.next()
    return result

if __name__ == '__main__':
    n = 40

    profile.run('simple_fibo(n)')
    print '--------------------------'
    profile.run('fibo(n)')
    print '--------------------------'
    profile.run('yield_fibo(n)')
    print '--------------------------'

