from task2_stack import Stack
import pytest

class TestStack:

    def setup_method(self):
        self.stk = Stack()

    def test_stack_empty(self):
        assert self.stk.is_empty() == True

    def test_increse_siz(self):
        self.stk.push(1)
        assert self.stk.size()==1  

    def test_top(self):
        self.stk.push(1)
        self.stk.push(2)
        self.stk.push(3)
        assert self.stk.top() == 3
        

    def test_pop(self):
        self.stk.push("b")
        self.stk.push("a")
        self.stk.push("v")
        assert self.stk.pop() == "v"

    def test_pop2(self):    
        self.stk.push("b")
        self.stk.push("a")
        self.stk.push("v")
        self.stk.pop()
        assert self.stk.pop() == "a"
        

    def test_siz(Self):
        Self.stk.push(2)
        Self.stk.push(3)
        assert Self.stk.size() == 2

    
    def test_pop_emty(self):
        assert self.stk.pop() == 1

    def test_peeking(self):
        assert self.stk.top() == 1
    
    def test_multiple_push_pop(self):
        for i in range(5):
            self.stk.push(i)
        for i in reversed(range(5)):
            assert self.stk.pop() == i
        assert self.stk.is_empty() == True

if __name__ == "__main__":
    pytest.main(["-v"])
