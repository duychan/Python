class Tree:
    def __init__(self, data, cost=100000):
        self.data = data 
        self.cost = cost
        self.children = []
        self.parent = None
    def add_child(self, child):
        child.parent = self
        self.children.append(child)
    def get_data(self):
        return self.data
    def get_children(self):
        return self.children
    def get_parent(self):
        return self.parent
    def __lt__(self, other):
        return self.cost < other.cost