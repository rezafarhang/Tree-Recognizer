class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 0


def get_right_child(node: 'Node'):
    if node.right is None:
        return False
    return True


def get_left_child(node: 'Node'):
    if node.left is None:
        return False
    return True


class Tree:
    root: 'Node' = None
    size = 0
    node_list = []  # for adding in my desire : root-left-right
    node_list2 = []  # for having all nodes
    leaf = []  # for having leaves
    height = 1

    def add_item(self, item: 'Node'):
        self.node_list.append(item)
        self.node_list2.append(item)
        if self.root is None:  # add root
            self.root = self.node_list2[0]
            self.size += 1
        else:
            while len(self.node_list) is not 0:
                if not get_left_child(self.node_list[0]):
                    item.height = self.height
                    self.node_list[0].left = item
                    self.size += 1
                    break
                elif not get_right_child(self.node_list[0]):
                    item.height = self.height
                    self.node_list[0].right = item
                    self.size += 1
                    break
                 else:
                    self.height += 1
                    self.node_list.pop(0)

    def is_bst_tree(self):
        for m in range(len(self.node_list2)):
            # print("m:",m)
            if get_left_child(self.node_list2[m]) or get_right_child(self.node_list2[m]):  # if have child
                if (
                        get_left_child(self.node_list2[m]) and self.node_list2[m].left.data > self.node_list2[m].data) \
                        or (
                        get_right_child(self.node_list2[m]) and self.node_list2[m].right.data < self.node_list2[
                    m].data):
                    return False
            return True

    def get_leaves(self):
        for node in self.node_list2:
            if (not get_right_child(node)) & (not get_left_child(node)):
                self.leaf.append(node)

    def is_avl_tree(self):
        if self.is_bst_tree():
            self.get_leaves()
            height_leaf = []
            for leaf in self.leaf:
                height_leaf.append(leaf.height)
            if max(height_leaf) - min(height_leaf) <= 1:
                return True
        return False

    def get_height(self):
        if (not get_right_child(self.root)) & (not get_left_child(self.root)):
            print(0)
        else:
            print(self.height)


def list_to_tree(ls=[]):
    desired_tree = Tree()
    for i in range(len(ls)):
        node = Node(ls[i])
        desired_tree.add_item(node)
    return desired_tree


# my_list = [50, 30, 70]
# my_tree = list_to_tree(my_list)
my_tree = Tree()
my_tree.add_item(Node(6))
my_tree.add_item(Node(5))
my_tree.add_item(Node(7))
my_tree.add_item(Node(3))
my_tree.add_item(Node(4))

print("now")
print(my_tree.is_bst_tree())
print(my_tree.is_avl_tree())
# test_tree = Tree()
# test_tree.add_item(Node(50))
# test_tree.add_item(Node(30))
# test_tree.add_item(Node(70))
# test_tree.add_item(Node(20))
# test_tree.add_item(Node(40))
# print(test_tree.is_bst_tree())
