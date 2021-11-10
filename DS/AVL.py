import bst


def update_height(node):
    if node:
        node.h = 1+max(node.left.h if node.left else -1,
                       node.right.h if node.right else -1)
    else:
        return 0


def height(node):
    return node.h if node else 0


class AVL(bst.BST):

    def rebalance(self, node):
        while(node):
            update_height(node)
            if(height(node.left)-height(node.right) >= 2):
                print('Left heavy:', node.val)
                if(node.left.right):
                    print('LR\nL')
                    self.left_rotate(node.left)
                    print('LR\nR')
                    self.right_rotate(node)
                else:
                    print('R')
                    self.right_rotate(node)
            if(height(node.right)-height(node.left) >= 2):
                print('Right heavy:', node.val)
                if(node.right.left):
                    print('RL\nR')
                    self.right_rotate(node.right)
                    print('RL\nL')
                    self.left_rotate(node)
                else:
                    print('L')
                    self.left_rotate(node)
            node = node.parent

    def right_rotate(self, oldRoot):
        newRoot = oldRoot.left
        orphan = newRoot.right
        if oldRoot.parent is None:
            self.root = newRoot
        else:
            if oldRoot.parent.left is oldRoot:
                oldRoot.parent.left = newRoot
            elif oldRoot.parent.right is oldRoot:
                oldRoot.parent.right = newRoot
        newRoot.right = oldRoot
        newRoot.parent = oldRoot.parent
        oldRoot.parent = newRoot
        oldRoot.left = orphan
        update_height(oldRoot)
        update_height(newRoot)

    def left_rotate(self, oldRoot):
        newRoot = oldRoot.right
        orphan = newRoot.left
        if oldRoot.parent is None:
            self.root = newRoot
        else:
            if oldRoot.parent.left is oldRoot:
                oldRoot.parent.left = newRoot
            elif oldRoot.parent.right is oldRoot:
                oldRoot.parent.right = newRoot
        newRoot.left = oldRoot
        newRoot.parent = oldRoot.parent
        oldRoot.parent = newRoot
        oldRoot.right = orphan
        update_height(oldRoot)
        update_height(newRoot)

    def insert(self, key):
        node = super(AVL, self).insert(key)
        print('Inserted: ', key)
        print('Without rebalance\n', str(self.root))
        self.rebalance(node)
        print('With rebalance\n', str(self.root))


avl = AVL()
arr = [12, 15, 2, 34, 20, 43, 3, 17]
for i in arr:
    avl.insert(i)
# avl.inorder()
