from abc import ABC, abstractmethod

class Console(ABC):
    
    @abstractmethod
    def read(self, prompt: str) -> str:
        pass

    @abstractmethod
    def print(self, line: str) -> None:
        pass

class Terminal(Console):

    def read(self, prompt: str) -> str:
        line = input(prompt)
        return line

    def print(self, line: str) -> None:
        print(line)

class MockConsole(Console):
    
    def __init__(self):
        self.contents = []

    def read(self, prompt: str) -> str:
        if len(self.contents > 0):
            line = self.contents.pop()
            return line
        else:
            return ''

    def print(self, line: str) -> None:
        self.contents.append(line)
