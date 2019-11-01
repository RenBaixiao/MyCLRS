def pre_order(T):
    if T==None:
        return
    stack = []
    stack.append(T)
    while size(stack) > 0:
        node = stack.pop()
        print(node.data)
        if node.right!=None:
            stack.append(node.right)
        if node.left!=None:
            stack.append(node.left)

def in_order(T):
    current = T
    stack = []

    while True:
        if current!=None:
            stack.append(current)
            current = current.left
        elif size(stack)>0:
            current = stack.pop()
            print(current.data)
            current = current.right
        else:
            break

def post_order(root):
    if root==None:
        return
    stack = []
    while True:
        while root!=None:
            if root.right!=None:
                stack.append(root.right)
            stack.append(root)
            root = root.left

        root = stack.pop()
        if root.right!=None and size(stack)>0 and stack[-1]==root.right:
            stack.pop()
            stack.append(root)
            root = root.right
        else:
            print(root.data)
            root = None

        if len(stack)<1:
            break
