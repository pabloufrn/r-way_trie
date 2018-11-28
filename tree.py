class Node:
    def __init__(self, val = None):
        self.val = val
        self.next = None

    def init_next(self, size):
        self.next = [None] * size

    def print_subtree(self, tabs = 0):
        if(self.next == None):
            return

        for idx, node in enumerate(self.next):
            if(node != None):
                symbol = '+' if node.val != None else '-'
                if(tabs > 0):
                    print((tabs-1)*'  ' + ' |' + symbol + chr(idx))
                else:
                    print(tabs*'  ' + symbol + chr(idx))
                node.print_subtree(tabs+1) 

class Tree:

    def __init__(self):
        self.root = Node(None)
        self.degree = 127
        self.root.init_next(self.degree)
        self.size = 0

    def search(self, key):
        current_node = self.root
        for ch in key:
            current_node = current_node.next[self.get_index(ch)]
            if(current_node == None):
                return None

        return current_node.val

    def insert(self, key, value):
        prev_node = self.root
        current_node = self.root
        for ch in key:
            if(current_node.next == None):
                current_node.init_next(self.degree)
            prev_node = current_node
            current_node = current_node.next[self.get_index(ch)]
            if(current_node == None):
                current_node = Node()
                prev_node.next[self.get_index(ch)] = current_node
        if(current_node.val == None):
            self.size += 1
        current_node.val = value

    def remove(self, key):
        self.root = self.delete_rec(self.root, (ch for ch in key))

    def delete_rec(self, current_node, gen_key):
        if(current_node == None):
            return None
        try:
            ch = next(gen_key)
            if(current_node.next == None):
                return current_node if current_node.val != None else None
            next_node = current_node.next
            ch_idx = self.get_index(ch)
            next_node[ch_idx] = self.delete_rec(next_node[ch_idx], gen_key)
        except StopIteration:
            if current_node.val != None:
                self.size -= 1
            current_node.val = None

        if(current_node.val != None):
            return current_node

        if(current_node.next == None):
            return None

        for node in current_node.next:
            if(node != None):
                return current_node

        return None

    def get_index(self, char):
        return ord(char)

    def print_tree(self):
        self.root.print_subtree()


