class TreeNode:
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None

def is_valid_avl(node):
    if node is None:
        return True

    # Verifica se a altura da subárvore esquerda e direita diferem no máximo em 1
    if abs(get_height(node.left) - get_height(node.right)) > 1:
        return False

    # Verifica recursivamente as subárvores esquerda e direita
    return is_valid_avl(node.left) and is_valid_avl(node.right)

def get_height(node):
    if node is None:
        return 0
    return node.height

# Exemplo de uso
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(2)
root.left.right = TreeNode(7)

# A árvore exemplo é válida como AVL, então a função deve retornar True
print(is_valid_avl(root))


