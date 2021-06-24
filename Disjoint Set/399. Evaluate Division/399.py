class DisjointSet:
    def __init__(self):
        self.parent = dict()
        self.degree = dict()
        self.weight = dict()

    def add(self, node):
        if node not in self.parent:
            self.parent[node] = node
            self.degree[node] = 1
            self.weight[node] = 1

    def find(self, node):
        if node not in self.parent:
            return None
        if node != self.parent[node]:
            parent = self.find(self.parent[node])
            self.weight[node] *= self.weight[self.parent[node]]
            self.parent[node] = parent
        return self.parent[node]

    def merge(self, node_a, node_b, a_div_b):
        parent_a = self.find(node_a)
        parent_b = self.find(node_b)
        if parent_a != parent_b:
            if self.degree[parent_a] < self.degree[parent_b]:
                self.parent[parent_a] = parent_b
                self.weight[parent_a] = a_div_b * self.weight[node_b] / self.weight[node_a]
            else:
                self.parent[parent_b] = parent_a
                self.weight[parent_b] = self.weight[node_a] / self.weight[node_b] / a_div_b
                if self.degree[parent_a] == self.degree[parent_b]:
                    self.degree[parent_a] += 1

    def evaluate(self, node_a, node_b):
        parent_a = self.find(node_a)
        parent_b = self.find(node_b)
        if parent_a == parent_b and parent_a is not None:
            return self.weight[node_a] / self.weight[node_b]
        return -1


class Solution:
    def calcEquation(self, equations, values, queries):
        ds = DisjointSet()
        for idx, (a, b) in enumerate(equations):
            ds.add(a)
            ds.add(b)
            ds.merge(a, b, values[idx])

        res = list()
        for a, b in queries:
            res.append(ds.evaluate(a, b))

        return res


if __name__ == '__main__':
    equations = [["a", "b"], ["b", "c"]]
    values = [2.0, 3.0]
    queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]

    s = Solution()
    s.calcEquation(equations, values, queries)
