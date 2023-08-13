# scope of a variable

def check_scope():
    def do_local():
            test = "local test"

    def non_local():
        nonlocal test
        test = "non local test"

    def global_test():
        global test
        test = "global test"

    test = "default"

    do_local()
    print("test value after do local: "+test)
    non_local()
    print("test value after do non local: " + test)
    global_test()
    print("test value after do global: " + test)


check_scope()

print("after main "+test)
