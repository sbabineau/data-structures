import random


class BinaryTree(object):

    def __init__(self, value=None):
        # try:
        #     int(value)
        # except TypeError:
        #     raise
        self.value = value
        self.greater = None
        self.lesser = None

    def insert(self, value):
        """Insert an integer into a binary tree"""
        if value == self.value:
            return
        elif value > self.value:
            if self.greater is None:
                self.greater = BinaryTree(value)
                return
            self.greater.insert(value)
        elif value < self.value:
            if self.lesser is None:
                self.lesser = BinaryTree(value)
                return
            self.lesser.insert(value)

    def contains(self, value):
        """Determine whether value is contained in binary tree"""
        #refactor opportunities
        try:
            if value == self.value:
                return True
            elif value > self.value:
                return self.greater.contains(value)
            elif value < self.value:
                return self.lesser.contains(value)
        except AttributeError:
            return False

    def size(self, total=0):
        """Returns total of all values within binary tree"""
        # doesn't need total at all
        if self.value:
            total += 1
        else:
            return 0

        if self.lesser:
            total += self.lesser.size()
        if self.greater:
            total += self.lesser.size()
        return total

    def depth(self):
        if self.value is None:
            return 0
        a = self.greater.depth() if self.greater else 0
        b = self.lesser.depth() if self.lesser else 0
        return max(a, b) + 1

    def balance(self):
        a = self.greater.depth() if self.greater else 0
        b = self.lesser.depth() if self.lesser else 0
        return a - b

    def get_dot(self):
        """return the tree with root 'self' as a dot graph for visualization"""
        return "digraph G{\n%s}" % ("" if self.data is None else (
            "\t%s;\n%s\n" % (
                self.data,
                "\n".join(self._get_dot())
            )
        ))

    def _get_dot(self):
        """recursively prepare a dot graph entry for this node."""
        if self.left is not None:
            yield "\t%s -> %s;" % (self.data, self.left.data)
            for i in self.left._get_dot():
                yield i
        elif self.right is not None:
            r = random.randint(0, 1e9)
            yield "\tnull%s [shape=point];" % r
            yield "\t%s -> null%s;" % (self.data, r)
        if self.right is not None:
            yield "\t%s -> %s;" % (self.data, self.right.data)
            for i in self.right._get_dot():
                yield
        elif self.left is not None:
            r = random.randint(0, 1e9)
            yield "\tnull%s [shape=point];" % r
            yield "\t%s -> null%s;" % (self.data, r)

if __name__ == '__main__':
    pass
