output_debug = False


def debug(msg):
    if output_debug:
        print(msg)


class Node(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self):
        self.root = None

    def insert(self, key, value):
        if self.root is None:
            self.root = Node(key, value)
            self.root.left = BinaryTree()
            self.root.right = BinaryTree()
            debug('Inserted: {} {}'.format(key, value))

        elif key < self.root.key:
            self.root.left.insert(key, value)
        elif key > self.root.key:
            self.root.right.insert(key, value)

        else:
            debug('{} already exists'.format(key))

        # TODO: self.rebalance()

    def remove(self, key):
        # debug("Trying to delete at node: " + str(self.node.key))
        if self.root is not None:
            if self.root.key == key:
                debug("Deleting {} ".format(key))
                if self.root.left.root is None and self.root.right.root is None:
                    self.root = None  # leaves can be killed at will

                # if only one subtree, take that
                elif self.root.left.root is None:
                    self.root = self.root.right.root
                elif self.root.right.root is None:
                    self.root = self.root.left.root

                # worst-case: both children present. Find logical successor
                else:
                    replacement = self.root.right.min_value_node()
                    if replacement is not None:  # sanity check
                        debug("Found replacement for {} -> {}".format(key, replacement.key))
                        self.root.key = replacement.key
                        self.root.value = replacement.value

                        # replaced. Now delete the key from right child
                        self.root.right.remove(replacement.key)

                # TODO: self.rebalance()
                return
            elif key < self.root.key:
                self.root.left.remove(key)
            elif key > self.root.key:
                self.root.right.remove(key)

            # TODO: self.rebalance()
        else:
            return

    # Given a non-empty binary search tree, return the node
    # with minum key value found in that tree. Note that the
    # entire tree does not need to be searched
    def min_value_node(self):
        current = self.root

        # loop down to find the leftmost leaf
        while current.left.root is not None:
            current = current.left.root

        return current

    def max_value_node(self):
        current = self.root

        # loop down to find the leftmost leaf
        while current.right.root is not None:
            current = current.right.root

        return current

    def print(self):
        node = self.root
        out = []
        if node is not None:
            out += node.left.print()
            out.append(node.key)
            out += node.right.print()
        return out

    def __str__(self):
        out = ''
        if self.root is not None:
            out = ' '.join([str(x) for x in self.print()])
        return out


class AVLTree(object):
    def __init__(self):
        self.root = None
        self.height = -1
        self.balance = 0

    def height(self):
        if self.root:
            return self.root.height
        else:
            return 0

    def is_leaf(self):
        return self.root.height == 0

    def insert(self, key, value):
        new_node = Node(key, value)

        if self.root is None:
            self.root = new_node
            self.root.left = AVLTree()
            self.root.right = AVLTree()
            debug('Inserted: {} {}'.format(key, value))

        elif key < self.root.key:
            self.root.left.insert(key, value)
        elif key > self.root.key:
            self.root.right.insert(key, value)

        else:
            debug('{} already exists'.format(key))

        self.rebalance()

    def remove(self, key):
        # debug("Trying to delete at node: " + str(self.node.key))
        if self.root is not None:
            if self.root.key == key:
                debug("Deleting {} ".format(key))
                if self.root.left.root is None and self.root.right.root is None:
                    self.root = None  # leaves can be killed at will
                # if only one subtree, take that
                elif self.root.left.root is None:
                    self.root = self.root.right.root
                elif self.root.right.root is None:
                    self.root = self.root.left.root

                # worst-case: both children present. Find logical successor
                else:
                    replacement = self.root.right.min_value_node()
                    if replacement is not None:  # sanity check
                        debug("Found replacement for {} -> {}".format(key, replacement.key))
                        self.root.key = replacement.key
                        self.root.value = replacement.value

                        # replaced. Now delete the key from right child
                        self.root.right.remove(replacement.key)

                self.rebalance()
                return
            elif key < self.root.key:
                self.root.left.remove(key)
            elif key > self.root.key:
                self.root.right.remove(key)

            self.rebalance()
        else:
            return

    def rebalance(self):
        self.update_heights(False)
        self.update_balances(False)
        while self.balance < -1 or self.balance > 1:
            if self.balance > 1:
                if self.root.left.balance < 0:
                    self.root.left.left_rotate()
                    self.update_heights()
                    self.update_balances()
                self.right_rotate()
                self.update_heights()
                self.update_balances()
            elif self.balance < -1:
                if self.root.right.balance > 0:
                    self.root.right.right_rotate()
                    self.update_heights()
                    self.update_balances()
                self.left_rotate()
                self.update_heights()
                self.update_balances()

    def right_rotate(self):
        A = self.root
        B = self.root.left.root
        T = B.right.root

        self.root = B
        B.right.root = A
        A.left.root = T

    def left_rotate(self):
        A = self.root
        B = self.root.right.root
        T = B.left.root

        self.root = B
        B.left.root = A
        A.right.root = T

    def update_heights(self, recurse=True):
        if self.root is None:
            self.height = -1
            return None
        elif recurse:
            if self.root.left is not None:
                self.root.left.update_heights()
            if self.root.right is not None:
                self.root.right.update_heights()

        self.height = max(self.root.left.height, self.root.right.height) + 1

    def update_balances(self, recurse=True):
        if self.root is None:
            self.balance = 0
            return None
        elif recurse:
            if self.root.left is not None:
                self.root.left.update_balances()
            if self.root.right is not None:
                self.root.right.update_balances()

        self.balance = self.root.left.height - self.root.right.height

    # Given a non-empty binary search tree, return the node
    # with minum key value found in that tree. Note that the
    # entire tree does not need to be searched
    def min_value_node(self):
        current = self.root

        # loop down to find the leftmost leaf
        while current.left.root is not None:
            current = current.left.root

        return current

    def max_value_node(self):
        current = self.root

        # loop down to find the leftmost leaf
        while current.right.root is not None:
            current = current.right.root

        return current

    def print_recursive(self):
        node = self.root
        out = []
        if node is not None:
            out += node.left.print_recursive()
            out.append(node.key)
            out += node.right.print_recursive()
        return out

    def __str__(self):
        out = ''
        if self.root is not None:
            out = ' '.join([str(x) for x in self.print_recursive()])
        return out


class TreeNode(object):
    def __init__(self, key=None):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None
        self.size = 0

    def insert(self, key, value):
        if self.key is None:
            self.key = key
            return None
        if key == self.key:
            debug('{} already exists'.format(key))
            return None
        if key < self.key:
            if self.left is None:
                self.set_left_child(TreeNode(key))
            else:
                self.left.insert(key, value)
        else:
            if self.right is None:
                self.set_right_child(TreeNode(key))
            else:
                self.right.insert(key, value)
        self.size += 1

    def set_left_child(self, left):
        self.left = left
        if left is not None:
            left.parent = self

    def set_right_child(self, right):
        self.right = right
        if right is not None:
            right.parent = self

    def find(self, key):
        if key == self.key:
            return self
        elif key < self.key and self.left is not None:
            self.left.find(key)
        elif key > self.key and self.right is not None:
            self.right.find(key)

    def remove(self, key):
        # Base Case
        if key is None:
            return key

        # If the val to be deleted is smaller than the node's
        # val then it lies in  left subtree
        if key < self.key:
            self.left = self.left.remove(key)

        # If the val to be delete is greater than the node's val
        # then it lies in right subtree
        elif key > self.key:
            self.right = self.right.remove(key)

        # If val is same as node's val, then this is the node
        # to be deleted
        else:
            # Node with only one child or no child
            if self.left is None:
                temp = self.right
                node = None
                return temp

            elif self.right is None:
                temp = self.left
                node = None
                return temp

            # Node with two children: Get the inorder successor
            # (smallest in the right subtree)
            temp = self.right.min_value_node()

            # Copy the inorder successor's content to this node
            self.key = temp.key

            # Delete the inorder successor
            self.right = self.right.remove(temp.key)

        return self

    # Given a non-empty binary search tree, return the node
    # with minum key value found in that tree. Note that the
    # entire tree does not need to be searched
    def min_value_node(self):
        current = self

        # loop down to find the leftmost leaf
        while current.left is not None:
            current = current.left

        return current

    def max_value_node(self):
        current = self

        # loop down to find the leftmost leaf
        while current.right is not None:
            current = current.right

        return current

    def print(self):
        node = self
        out = []
        if node is not None:
            out += node.left.print() if node.left is not None else []
            if node.key is not None:
                out.append(node.key)
            out += node.right.print() if node.right is not None else []
        return out

    def __str__(self):
        out = ''
        if self is not None:
            out = ' '.join([str(x) for x in self.print()])
        return out


class AVLTreeNode(object):
    def __init__(self, key=None):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None
        self.size = 0

    def insert(self, key, value):
        if self.key is None:
            self.key = key
            return None
        if key == self.key:
            debug('{} already exists'.format(key))
            return None
        if key < self.key:
            if self.left is None:
                self.set_left_child(TreeNode(key))
            else:
                self.left.insert(key, value)
        else:
            if self.right is None:
                self.set_right_child(TreeNode(key))
            else:
                self.right.insert(key, value)
        self.size += 1

    def set_left_child(self, left):
        self.left = left
        if left is not None:
            left.parent = self

    def set_right_child(self, right):
        self.right = right
        if right is not None:
            right.parent = self

    def find(self, key):
        if key == self.key:
            return self
        elif key < self.key and self.left is not None:
            self.left.find(key)
        elif key > self.key and self.right is not None:
            self.right.find(key)

    def remove(self, key):
        # Base Case
        if key is None:
            return key

        # If the val to be deleted is smaller than the node's
        # val then it lies in  left subtree
        if key < self.key:
            self.left = self.left.remove(key)

        # If the val to be delete is greater than the node's val
        # then it lies in right subtree
        elif key > self.key:
            self.right = self.right.remove(key)

        # If val is same as node's val, then this is the node
        # to be deleted
        else:
            # Node with only one child or no child
            if self.left is None:
                temp = self.right
                node = None
                return temp

            elif self.right is None:
                temp = self.left
                node = None
                return temp

            # Node with two children: Get the inorder successor
            # (smallest in the right subtree)
            temp = self.right.min_value_node()

            # Copy the inorder successor's content to this node
            self.key = temp.key

            # Delete the inorder successor
            self.right = self.right.remove(temp.key)

        return self

    # Given a non-empty binary search tree, return the node
    # with minum key value found in that tree. Note that the
    # entire tree does not need to be searched
    def min_value_node(self):
        current = self

        # loop down to find the leftmost leaf
        while current.left is not None:
            current = current.left

        return current

    def max_value_node(self):
        current = self

        # loop down to find the leftmost leaf
        while current.right is not None:
            current = current.right

        return current

    def print(self):
        node = self
        out = []
        if node is not None:
            out += node.left.print() if node.left is not None else []
            if node.key is not None:
                out.append(node.key)
            out += node.right.print() if node.right is not None else []
        return out

    def __str__(self):
        out = ''
        if self is not None:
            out = ' '.join([str(x) for x in self.print()])
        return out
