# class Node(object):
#     def __init__(self, data, left=None, right=None):
#         self.data = data
#         self.left = left
#         self.right = right
#
# tree = Node(1, Node(3, Node(7, Node(0)), Node(6)), Node(2, Node(5), Node(4)))
#
# # 层次遍历
# def lookup(root):
#     print('层次遍历的结果是：')
#     row = [root]
#     while row:
#         current = row.pop(0)
#         print( current.data)
#         if current.left:
#             row.append(current.left)
#         if current.right:
#             row.append(current.right)
#
#
# # 深度遍历
# def deep(root):
#     if not root:
#         return
#     print(root.data)
#     deep(root.left)
#     deep(root.right)
#
#
# if __name__ == '__main__':
#     lookup(tree)
#     print('深度遍历的结果是：')
#     deep(tree)

class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

tree = Node(1, Node(3, Node(7, Node(0)), Node(6)), Node(2, Node(5), Node(4)))


# 中序遍历:遍历左子树,访问当前节点,遍历右子树
def mid_travelsal(root):
    if root is None:
        return
    if root.left is not None:
        mid_travelsal(root.left)
    #访问当前节点
    print(root.value)
    if root.right is not None:
        mid_travelsal(root.right)

# 前序遍历:访问当前节点,遍历左子树,遍历右子树

def pre_travelsal(root):
    print (root.value)
    if root.left is not None:
        pre_travelsal(root.left)
    if root.right is not None:
        pre_travelsal(root.right)

# 后续遍历:遍历左子树,遍历右子树,访问当前节点

def post_trvelsal(root):
    if root.left is not None:
        post_trvelsal(root.left)
    if root.right is not None:
        post_trvelsal(root.right)
    print (root.value)


# 最大树的深度
def maxDepth(root):
    if not root:
        return 0
    return max(maxDepth(root.left), maxDepth(root.right)) + 1


# 求两棵树是否相同
def isSameTree(p, q):
    if p == None and q == None:
        return True
    elif p and q :
        return p.val == q.val and isSameTree(p.left,q.left) and isSameTree(p.right,q.right)
    else :
        return False

if __name__ == '__main__':
    print('中序遍历结果为：')
    mid_travelsal(tree)
    print('前序遍历结果为：')
    pre_travelsal(tree)
    print('后序遍历结果为：')
    post_trvelsal(tree)
    print('最大树深度为：')
    print(maxDepth(tree))