class DNode:
    def __init__(self, val):
        self.val = val
        self.nxt = None
        self.prev = None

class BrowserHistory:
    def __init__(self, homepage: str):
        self.head = DNode(homepage)
        self.curr = self.head

    def visit(self, url: str) -> None:
        self.curr.nxt = DNode(url)
        self.curr.nxt.prev = self.curr
        self.curr = self.curr.nxt

    def back(self, steps: int) -> str:
        count = 0
        while count < steps:
            if self.curr.prev is None:
                return self.curr.val
            self.curr = self.curr.prev
            count += 1
        return self.curr.val

    def forward(self, steps: int) -> str:
        count = 0
        while count < steps:
            if self.curr.nxt is None:
                return self.curr.val
            self.curr = self.curr.nxt
            count += 1
        return self.curr.val


# Tests
browser = BrowserHistory("leetcode.com")
print('expected output: [null,null,null,null,"facebook.com","google.com","facebook.com",null,"linkedin.com","google.com","leetcode.com"]')
print("actual output: ",
    browser.visit("google.com"),
    browser.visit("facebook.com"),
    browser.visit("youtube.com"),
    browser.back(1),
    browser.back(1),
    browser.forward(1),
    browser.visit("linkedin.com"),
    browser.forward(2),
    browser.back(2),
    browser.back(7),
)
