class BSTNode(object):
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.parent = None
        self.size = 1
    rankVar = 0

    def _str(self):
        """Internal method for ASCII art."""
        label = str(self.val)
        if self.left is None:
            left_lines, left_pos, left_width = [], 0, 0
        else:
            left_lines, left_pos, left_width = self.left._str()
        if self.right is None:
            right_lines, right_pos, right_width = [], 0, 0
        else:
            right_lines, right_pos, right_width = self.right._str()
        middle = max(right_pos + left_width - left_pos + 1, len(label), 2)
        pos = left_pos + middle // 2
        width = left_pos + middle + right_width - right_pos
        while len(left_lines) < len(right_lines):
            left_lines.append(' ' * left_width)
        while len(right_lines) < len(left_lines):
            right_lines.append(' ' * right_width)
        if (middle - len(label)) % 2 == 1 and self.parent is not None and \
           self is self.parent.left and len(label) < middle:
            label += '.'
        label = label.center(middle, '.')
        if label[0] == '.':
            label = ' ' + label[1:]
        if label[-1] == '.':
            label = label[:-1] + ' '
        lines = [' ' * left_pos + label + ' ' * (right_width - right_pos),
                 ' ' * left_pos + '/' + ' ' * (middle-2) +
                 '\\' + ' ' * (right_width - right_pos)] + \
            [left_line + ' ' * (width - left_width - right_width) + right_line
             for left_line, right_line in zip(left_lines, right_lines)]
        return lines, pos, width

    def __str__(self):
        return '\n'.join(self._str()[0])

    def height(self):
        if self:
            if self.left:
                self.left.height()
            if self.right:
                self.right.height()
            self.h = 1+max(self.left.h if self.left else -1,
                           self.right.h if self.right else -1)

    def inorder(self):
        if self:
            if self.left:
                self.left.inorder()
            print(self.val)
            if self.right:
                self.right.inorder()

    def rank(self, key):  # key is the time here
        if(self.left != None and key < self.val):
            return self.left.rank(key)
        if(key >= self.val):
            BSTNode.rankVar = BSTNode.rankVar+1 +\
                (self.left.size if self.left != None else 0)
            # print(self.val, BSTNode.rankVar)
        if(self.right != None):
            return self.right.rank(key)

        print('Rank of ', key, ' is ', BSTNode.rankVar)
        return BSTNode.rankVar

    def add_size(self):
        if self:  # post order traversal Left->Right->Root
            if self.left:
                self.left.add_size()
            if self.right:
                self.right.add_size()
            self.size = self.size+(self.left.size if self.left != None else 0) + \
                (self.right.size if self.right != None else 0)
            # print(self.val, self.size)

    def next_large_node(self):
        # root=root.right.right #arbitrary node to check
        # If right element is present the next large surely exist and is the minimum of right subtree
        root = self
        if(self == None):
            return
        if self.right != None:
            root = self.right
            while(root.left != None):
                root = root.left
            print(root.val)
            return
        # Checking if any parent is the left child in which case the super parent is our solution
        # Edge case for right most element, the loop reaches root and terminates in If
        while root.parent.left != root:
            root = root.parent
            if(root.parent == None):
                print(None)
                return
        print(root.parent.val)
        return

    def next_large_value(self, key):
        # Find the value
        if self == None:
            return None
        if(key != self.val):
            if(key < self.val):
                if(self.left != None):
                    self.left.next_large_value(key)
            if(key > self.val):
                if(self.right != None):
                    self.right.next_large_value(key)
        else:
            return self.next_large_node()

    def insert(self, node):
        if(node.val < self.val):
            if(self.left != None):
                self.left.insert(node)
            else:
                node.parent = self
                self.left = node
        else:
            if(self.right != None):
                self.right.insert(node)
            else:
                node.parent = self
                self.right = node


class BST(object):
    def __init__(self):
        self.root = None
    rankVar = 0

    def __str__(self):
        if self.root is None:
            return '<empty tree>'
        return str(self.root)

    def height(self):
        self.root.height()

    def inorder(self):
        if self.root:
            self.root.inorder()

    def rank(self, key):  # key is the time here
        self.root.add_size()
        return self.root.rank(key)

    def add_size(self):
        self.root.add_size()

    def next_large_node(self, node):
        node.next_large_node()

    def next_large_value(self, key):
        self.root.next_large_value(key)

    def insert(self, key):
        node = BSTNode(key)
        if(self.root == None):
            self.root = node
        else:
            self.root.insert(node)
        self.root.height()
        return node


bst = BST()

arr = [12, 15, 2, 34, 20, 43, 3, 17]
for i in arr:
    bst.insert(i)
# bst.inorder()
# bst.next_large_node(bst.root)
# bst.next_large_value(43)
# bst.rank(43)
# bst.height()
