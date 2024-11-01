from lupa.lua54 import LuaRuntime

lua = LuaRuntime(unpack_returned_tuples=True)

import time

def func(n):
    temp = 1
    for i in range(1, n): temp *= i
    return temp

start = time.time_ns()
print(func(100001) % 1000000)
print(f'elapsed time = {time.time_ns() - start}')

lua_script = '''
function(n)
    local temp = 1
    for i = 1, n - 1 do
        temp = temp * i
    end
    return temp
end
'''
lua_func = lua.eval(lua_script)
start = time.time_ns()
print(lua_func(100001) % 1000000)
print(f'elapsed time = {time.time_ns() - start}')