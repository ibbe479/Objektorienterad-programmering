from Task2_stack import Stack
import pytest

class TestStack:
   

    def setup_method(self):

        self.stack = Stack()

    def test_is_empty(self):
        assert self.stack.is_empty() == True

    def test_push(self):
        self.stack.push(1)
        assert self.stack.size() == 1
    
    def test_top(self):
        self.stack.push(1)
        assert self.stack.top() == 1

    def test_pop(self):
        self.stack.push(1)
        assert self.stack.pop() == 1
        assert self.stack.is_empty() == True

    def test_size(self):
        self.stack.push(1)
        self.stack.push(2)
        assert self.stack.size() == 2

    def test_pop_empty(self):
        assert self.stack.pop() == 1

    def test_top_empty(self):
        assert self.stack.top() == -1
    
    def test_multiple_push_pop(self):
        for i in range(5):
            self.stack.push(i)
        for i in reversed(range(5)):
            assert self.stack.pop() == i
        assert self.stack.is_empty() == True


if __name__ == "__main__":
    pytest.main(["-v"])



        