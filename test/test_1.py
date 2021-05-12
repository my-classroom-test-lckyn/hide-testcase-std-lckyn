
import sys
sys.path.insert(1, './1/')
import sol1

def test_1_1():
    assert sol1.f(5) == 25
def test_1_2():    
    assert sol1.f(4) == 16
def test_1_3():
    assert sol1.f(3) == 9
def test_1_4():
    assert sol1.f(2) == 4
def test_1_5():
    assert sol1.f(1) == 1
    