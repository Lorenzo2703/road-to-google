from typing import List, Optional
from collections import deque

class Node:
    # Constructor to create a new node
    def __init__(self, cost: int):
        self.cost: int = cost
        self.children: List['Node'] = []
        self.parent: Optional['Node'] = None

def get_cheapest_cost(node: Node) -> int:
    # Caso base: se non ho figli, sono una foglia. Il costo è solo il mio.
    if not node.children:
        return node.cost
    
    # Passo ricorsivo: chiedo a ogni figlio il costo minimo del suo sotto-albero
    min_child_cost = float("inf")
    for child in node.children:
        min_child_cost = min(min_child_cost, get_cheapest_cost(child))
        
    # Il costo totale è il mio costo + il minimo trovato tra i figli
    return node.cost + min_child_cost

def get_cheapest_cost_1(rootNode):
    if not rootNode:
        return 0
    minCost = 0xfffff
    stack = [(rootNode,rootNode.cost)]
    while stack:
        node, cost = stack.pop(-1)
        if node.children:
            for child in node.children:
                stack.append((child, child.cost + cost))
        else:
            minCost = min(cost, minCost)
    
    return minCost

def get_cheapest_paths(node: Node) -> (int, List[List[int]]):
    # Caso base: foglia
    if not node.children:
        return node.cost, [[node.cost]]
    
    min_cost = float("inf")
    all_paths = []
    
    for child in node.children:
        child_cost, child_paths = get_cheapest_paths(child)
        
        # Se troviamo un nuovo minimo, resettiamo la lista dei percorsi
        if child_cost < min_cost:
            min_cost = child_cost
            all_paths = [[node.cost] + path for path in child_paths]
        # Se troviamo un percorso con lo stesso minimo, lo aggiungiamo
        elif child_cost == min_cost:
            all_paths.extend([[node.cost] + path for path in child_paths])
            
    return node.cost + min_cost, all_paths

def get_longest_path(node: Node) -> int:
    # Caso base: se sono una foglia, il percorso è composto da me stesso (1 nodo)
    if not node.children:
        return 1
    
    # Cerchiamo il percorso più lungo tra i figli
    max_depth = 0
    for child in node.children:
        max_depth = max(max_depth, get_longest_path(child))
        
    # Restituiamo il valore del figlio più "profondo" + 1 (per includere il nodo attuale)
    return 1 + max_depth

def get_longest_path_nodes(node: Node) -> List[int]:
    if not node.children:
        return [node.cost]
    
    best_path = []
    for child in node.children:
        current_path = get_longest_path_nodes(child)
        if len(current_path) > len(best_path):
            best_path = current_path
            
    return [node.cost] + best_path

def get_shortest_path_to_leaf(root: Node) -> int:
    if not root:
        return 0
    
    # La coda contiene tuple: (nodo, lunghezza_percorso)
    queue = deque([(root, 1)])
    
    while queue:
        node, depth = queue.popleft()
        
        # Se è una foglia, abbiamo trovato il percorso più breve
        if not node.children:
            return depth
        
        # Aggiungiamo i figli alla coda
        for child in node.children:
            queue.append((child, depth + 1))


# debug your code below
root = Node(0)
root.children = [Node(5), Node(3), Node(6)]
root.children[0].children = [Node(4)]
root.children[1].children = [Node(2), Node(0)]
root.children[2].children = [Node(1), Node(5)]
root.children[1].children[0].children = [Node(1)]
root.children[1].children[0].children[0].children = [Node(1)]
root.children[1].children[1].children = [Node(10)]
root.children[2].children[0].children = [Node(1), Node(5)]



print(get_cheapest_cost(root))
print(get_cheapest_cost_1(root))
print(get_cheapest_paths(root))
print(get_longest_path(root))
print(get_longest_path_nodes(root))
print(get_shortest_path_to_leaf(root))






def get_cheapest_cost_brute_force(root: Node) -> float:
    # 1. Troviamo tutti i percorsi (lista di liste)
    all_paths = []
    
    def find_all_paths(node, current_path_costs):
        # Aggiungiamo il costo del nodo corrente
        new_path = current_path_costs + [node.cost]
        
        # Se siamo arrivati a una foglia, salviamo il percorso completo
        if not node.children:
            all_paths.append(new_path)
            return
        
        # Altrimenti continuiamo a scendere ricorsivamente
        for child in node.children:
            find_all_paths(child, new_path)
            
    # Avviamo la ricerca
    find_all_paths(root, [])
    
    # 2. Calcoliamo la somma di ogni percorso trovato
    costs = [sum(path) for path in all_paths]
    
    # 3. Restituiamo il minimo
    return min(costs)

from collections import deque

def get_cheapest_cost_bfs(root: Node) -> float:
    if not root: return 0
    
    min_cost = float('inf')
    # Coda contiene (nodo, costo_accumulato)
    queue = deque([(root, root.cost)])
    
    while queue:
        node, current_cost = queue.popleft()
        
        if not node.children:
            min_cost = min(min_cost, current_cost)
        else:
            for child in node.children:
                queue.append((child, current_cost + child.cost))
                
    return min_cost

def get_cheapest_cost_iterative(root: Node) -> float:
    if not root: return 0
    
    min_cost = float('inf')
    # Stack contiene (nodo, costo_accumulato_fino_qui)
    stack = [(root, root.cost)]
    
    while stack:
        node, current_cost = stack.pop()
        
        # Se è una foglia, aggiorniamo il minimo
        if not node.children:
            min_cost = min(min_cost, current_cost)
        else:
            # Se ha figli, aggiungiamoli allo stack
            for child in node.children:
                stack.append((child, current_cost + child.cost))
                
    return min_cost

def get_cheapest_cost_recursive(node: Node) -> float:
    if not node.children:
        return node.cost
    
    min_cost = float('inf')
    for child in node.children:
        min_cost = min(min_cost, get_cheapest_cost(child))
        
    return node.cost + min_cost