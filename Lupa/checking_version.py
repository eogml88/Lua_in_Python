try:
    import lupa.luajit22 as lupa
except ImportError:
    try:
        import lupa.lua54 as lupa
    except ImportError:
        try:
            import lupa.lua53 as lupa
        except ImportError:
            import lupa

print(f'using {lupa.LuaRuntime().lua_implementation} (compiled with {lupa.LUA_VERSION})')
