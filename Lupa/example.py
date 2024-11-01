
from lupa.lua54 import LuaRuntime

lua = LuaRuntime(unpack_returned_tuples=True)
print(lua.eval('1+1'))
lua_func = lua.eval('function(f, a, b) return f(a, b) end')
def myadd(a, b): return a + b
print(lua_func(myadd, 1, 2))
print(lua.eval('python.eval(" 3 ** 2 ")'))
print(lua.eval('python.builtins.str(4)') == '4')

import lupa
print(lupa.lua_type(lua_func))
print(lupa.lua_type(lua.eval('{}')))

print(lupa.lua_type(123))
print(lupa.lua_type('abc'))
print(lupa.lua_type({}))

lua.execute('a, b, c = python.eval("(1, 2)")')
g = lua.globals()
print(g.a)
print(g.b)
print(g.c)

non_explode_lua = lupa.LuaRuntime(unpack_returned_tuples=False)
non_explode_lua.execute('a, b, c = python.eval("(1, 2)")')
g = non_explode_lua.globals()
print(g.a)
print(g.b)
print(g.c)

wrapped_type = lua.globals().type
print(wrapped_type(1))
print(wrapped_type('abc'))