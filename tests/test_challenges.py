from programs.challenges import func_1_methods, func_1_no_methods, func_2, func_3, func_4, func_5

def test_func_1_methods():
    assert func_1_methods("Hello world") == "hello world"
    assert func_1_methods("Hello World!") == "HELLO WORLD!"

def test_func_1_no_methods():
    assert func_1_no_methods("Hello world") == "hello world"
    assert func_1_no_methods("Hello World!") == "HELLO WORLD!"

def test_func_2():
    assert func_2("Home", ["hole", "dome", "dove", "hail"]) == ["hole", "dome"]
    assert func_2("wall", ["Wail", "warmer", "tall", "worn"]) == ["Wail", "tall"]

def test_func_3():
    assert func_3(2, 3, [4, 6, 10, 12]) == [False, True, False, True]
    assert func_3(5, 7, [35, 36, 42, 70]) == [True, False, False, True]

def test_func_4():
    assert func_4("Hello world") == "hllrld"
    assert func_4("python is cool") == "pthnl"

def test_func_5():
    assert func_5([12, 14, 15, 24, 60]) == None
    with open('factors.csv', 'r') as f:
        assert f.readline() == '1,2,3,4,6\n'