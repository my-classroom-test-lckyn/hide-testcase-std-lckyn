
import sys
sys.path.insert(2, './2/')
import sol2

def test_2_1():
    assert sol2.g(5) == 10
def test_2_2():    
    assert sol2.g(4) == 8
def test_2_3():
    assert sol2.g(3) == 6
def test_2_4():
    assert sol2.g(2) == 4
def test_2_5():
    assert sol2.g(1) == 2
    