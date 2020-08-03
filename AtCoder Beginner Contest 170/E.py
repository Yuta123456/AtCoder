class Node(object):
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None
        self.height = 0
class AVL(object):
    def __init__(self):
        self.root = None
    def get_height(self, node):
        if not node:
            return -1
        return node.height
    def get_balance(self, node):
        '''
        返り値が1より大きい場合、左の部分木が重い　→　右回転
        返り値が-1より小さい場合、右の部分木が重い　→　左回転
        '''
        if not node:
            return 0
        return self.get_height(node.left_child) - self.get_height(node.right_child)
    def rotate_right(self, node):
        temp_left_child = node.left_child
        temp_left_right_child = temp_left_child.right_child
        temp_left_child.right_child = node
        node.left_child = temp_left_right_child
        node.height = max(self.get_height(node.left_child), self.get_height(node.right_child)) + 1
        temp_left_child.height = max(self.get_height(temp_left_child.left_child), self.get_height(temp_left_child.right_child)) + 1
        return temp_left_child
    def rotate_left(self, node):
        temp_right_child = node.right_child
        temp_right_left_child = temp_right_child.left_child
        temp_right_child.left_child = node
        node.right_child = temp_right_left_child
        node.height = max(self.get_height(node.left_child), self.get_height(node.right_child)) + 1
        temp_right_child.height = max(self.get_height(temp_right_child.left_child), self.get_height(temp_right_child.right_child)) + 1
        return temp_right_child
    def insert(self, data):
        self.root = self._insert(data, self.root)
 
    def _insert(self, data, node):
        if not node:
            return Node(data)
        if data < node.data:
            node.left_child = self._insert(data, node.left_child)
        else:
            node.right_child = self._insert(data, node.right_child)
        
        node.height = max(self.get_height(node.left_child), self.get_height(node.right_child)) + 1
        return self.settle_unbalance(data, node)
    def settle_unbalance(self, data, node):
        balance = self.get_balance(node)
        # balace >1 -> 左の方が重い
        # data < node.left_child.data 左の子より左側にデータが挿入されたので、左の子の左の子の方が重い
        # つまり、left-left heavy　右回転を行う
        if balance > 1 and data < node.left_child.data:
            return self.rotate_right(node)
        # balace > -1 -> 右の方が重い
        # data > node.right_child.data 右の子より右側にデータが挿入されたので、右の子の右の子の方が重い
        # つまり、right-right heavy　左回転を行う
        if balance < -1 and data > node.right_child.data:
            return self.rotate_left(node)
        # balace >1 -> 左の方が重い
        # data > node.left_child.data 左の子より右側にデータが挿入されたので、左の子の右の子の方が重い
        # つまり、left-right heavy　左回転を行い右回転を行う
        if balance > 1 and data > node.left_child.data:
            node.left_child = self.rotate_left(node.left_child)
            return self.rotate_right(node)
        # balace > -1 -> 右の方が重い
        # data < node.right_child.data 右の子より左側にデータが挿入されたので、右の子の左の子の方が重い
        # つまり、right-left heavy　右回転を行い左回転を行う
        if balance < -1 and data < node.right_child.data:
            node.right_child = self.rotate_right(node.right_child)
            return self.rotate_left(node)
        return node
    def traverse_inorder(self):
        if self.root:
            self._traverse_inorder(self.root)
            # 改行対策
            print()
        else:
            print('木は空です。')
    def _traverse_inorder(self, node):
        if node.left_child:
            self._traverse_inorder(node.left_child)
        print(node.data, end=' ')
        if node.right_child:
            self._traverse_inorder(node.right_child)
    def remove(self, data):
        if self.root:
            self.root = self._remove(data, self.root)
    def _remove(self, data, node):
        if data < node.data:
            node.left_child = self._remove(data, node.left_child)
        elif data > node.data:
            node.right_child = self._remove(data, node.right_child)
        else:
            # 削除ノードが子を持たない場合は、ノードを削除する。
            if not node.right_child and not node.left_child:
                del node
                # None を返すことで、親ノードの削除子ノードへのポインタを None に変更
                return None
            
            # 削除ノードが左の子だけを持つ場合、ノードを削除し、左の子のノードを返す
            if not node.right_child:
                temp = node.left_child
                del node
                # 左の子のノードを返すことで、親ノードの削除子ノードへのポインタを新しい子ノードに変更
                return temp
            
            # 削除ノードが右の子だけを持つ場合、左の子だけの場合の逆の操作を行う
            if not node.left_child:
                temp = node.right_child
                del node
                return temp
            # 削除ノードが左右の子を持つ場合、ここでは、左側のsubtreeの最大のノードを代わりのノードにすることにする。
            #  subtreeの最大のノードを取得するヘルパー関数
            def _get_max_node(node):
                if node.right_child:
                    return _get_max_node(node.right_child)
                return node
            temp = _get_max_node(node.left_child)
            node.data = temp.data
            # 左側のsubtreeから削除ノードと入れ替えたノードを削除
            node.left_child = self._remove(temp.data, node.left_child)
        
        # 単体の木の場合
        if not node:
            return node
        node.height = max(self.get_height(node.left_child), self.get_height(node.right_child)) + 1
        balance = self.get_balance(node)
        if balance > 1 and self.get_balance(node.left_child) >= 0:
            return self.rotate_right(node)
        if balance < -1 and self.get_balance(node.left_child) <= 0:
            return self.rotate_left(node)
        if balance > 1 and self.get_balance(node.left_child) < 0:
            node.left_child = self.rotate_left(node.left_child)
            return self.rotate_right(node)
        if balance < -1 and self.get_balance(node.left_child) > 0:
            node.right_child = self.rotate_right(node.right_child)
            return self.rotate_left(node)
        return node
    def maxkey(self):
        node = self.root
        if node == None:
            return None
        while node.right_child != None:
            node = node.right_child
        return node.data
    def minkey(self):
        node = self.root
        if node == None:
            return 10**10
        while node.left_child != None:
            node = node.left_child
        return node.data
################################################################

n ,q = map(int, input().split())
rate = [0 for j in range(n+1)]
belongs = [0 for j in range(n+1)]
k_garden = [AVL() for i in range(2*10**5 + 2)]
k_garden_max = [None for i in range(2*10**5 + 2)]
max_AVL = AVL()
for i in range(1,n+1):
    a, b = map(int, input().split())
    rate[i] = a
    belongs[i] = b
    k_garden[b].insert(a)
for i in range(2*10**5 + 2):
    if k_garden[i].root != None:
        a = k_garden[i].maxkey()
        k_garden_max[i] = a
        print(a)
        max_AVL.insert(a)
for i in range(q):
    c, d = map(int, input().split())
    src = belongs[c]
    belongs[c] = d
    k_garden[src].remove(rate[c])
    if k_garden_max[src] != k_garden[src].maxkey():
        if k_garden_max[src]:
            max_AVL.remove(rate[c])
        k_garden_max[src] = k_garden[src].maxkey()
        if  k_garden_max[src]:
            max_AVL.insert(k_garden_max[src])
    k_garden[d].insert(rate[c])
    if k_garden_max[d] != k_garden[d].maxkey():
        if k_garden_max[d]:
            max_AVL.remove(k_garden_max[d])
        k_garden_max[d] = k_garden[d].maxkey()
        if k_garden_max[d]:
            max_AVL.insert(k_garden_max[d])
    #max_AVL.traverse_inorder()
    print(max_AVL.minkey())



    
