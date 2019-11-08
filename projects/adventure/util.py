class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist.")

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create an empty queue and enqueue the starting vertex ID
        q = Queue()
        q.enqueue(starting_vertex)
        # Create an empty Set to store visited vertices
        visited = set()
        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first vertex
            v = q.dequeue()
            # If that vertex has not been visited...
            if v not in visited:
                # Mark it as visited
                print(v)
                visited.add(v)
                # Then add all of its neighbors to the back of the queue
                for neighbor in self.vertices[v]:
                    q.enqueue(neighbor)




    def dft_recursive(self, starting_vertex, visited = None, directions = None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        if directions is None:
            directions = []
        if visited is None:
            visited = set()
        if starting_vertex not in visited:
            print(starting_vertex)
            visited.add(starting_vertex)
            for neighbor in self.vertices[starting_vertex]:
                if neighbor not in visited:
                    self.dft_recursive(neighbor, visited)
                    
            
    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create an empty stack and push the starting vertex ID
        s = Stack()
        s.push(starting_vertex)
        # Create a Set to store visited vertices
        visited = set()
        # While the stack is not empty...
        while s.size() > 0:
            # Pop the first vertex
            v = s.pop()
            # If that vertex has not been visited...
            if v not in visited:
                # Mark it as visited...
                print(v)
                visited.add(v)
                # Then add all of its neighbors to the top of the stack
                for neighbor in self.vertices[v]:
                    s.push(neighbor)                    


    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty queue and enqueue A PATH TO the starting vertex ID
        # Create a Set to store visited vertices
        # While the queue is not empty...
            # Dequeue the first PATH
            # Grab the last vertex from the PATH
            # If that vertex has not been visited...
                # CHECK IF IT'S THE TARGET
                  # IF SO, RETURN PATH
                # Mark it as visited...
                # Then add A PATH TO its neighbors to the back of the queue
                  # COPY THE PATH
                  # APPEND THE NEIGHOR TO THE BACK
        
                # Create an empty queue and enqueue the starting vertex ID
        q = Queue()
        q.enqueue([starting_vertex])
        # Create an empty Set to store visited vertices
        visited = set()
        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first vertex
            v = q.dequeue()
            # If that vertex has not been visited...
            if v is not None:
                if v[-1] not in visited:
                    # Mark it as visited
                    if v[-1] == destination_vertex:
                        return v
                    visited.add(v[-1])
                    # Then add all of its neighbors to the back of the queue
                    for neighbor in self.vertices[v[-1]]:
                        z = v[:]
                        z.append(neighbor)
                        q.enqueue(z)

    def find_ancestor(self, starting_vertex):
        q = Queue()
        q.enqueue([starting_vertex])
        # Create an empty Set to store visited vertices
        visited = set()
        earliest_ancestor = starting_vertex
        longest_path = 1
        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first vertex
            path = q.dequeue()
            # If that vertex has not been visited...
            print(path)
            if path is not None:
                    # Mark it as visited
                    if len(path) == longest_path:
                        if path[-1] < earliest_ancestor:
                            earliest_ancestor = path[-1]
                    if len(path) > longest_path:
                        earliest_ancestor = path[-1]
                        longest_path = len(path)
                    visited.add(path[-1])
                    # Then add all of its neighbors to the back of the queue
                    for neighbor in self.vertices[path[-1]]:
                        z = path[:]
                        z.append(neighbor)
                        q.enqueue(z)
                        print(q.queue)
        print(earliest_ancestor)
        return earliest_ancestor

    def adventure_solution(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create an empty stack and push the starting vertex ID
        s = Stack()
        return_points = Stack()
        s.push(starting_vertex)
        directions = []
        # Create a Set to store visited vertices
        visited = set()
        # While the stack is not empty...
        while s.size() > 0:
            # Pop the first vertex
            v = s.pop()
            # If that vertex has not been visited...
            if v not in visited:
                # Mark it as visited...
                directions.append(v)
                visited.add(v)
                
                # Then add all of its neighbors to the top of the stack
            for neighbor in self.vertices[v]:
                if neighbor not in visited:
                    s.push(neighbor)
            count = 0
            for neighbor in self.vertices[v]:
                if neighbor not in visited:
                    count += 1
            if count > 1:
                return_points.push(v)
                print(return_points.stack)
            if count == 0:
                if len(return_points.stack):
                    backtrack = return_points.pop()
                    print('backtracking to: ', backtrack, 'from ', v)
                    print(f'adding {directions} and {self.bfs(v,backtrack)}')
                    directions = directions + self.bfs(v,backtrack)
                    s.push(backtrack)
                    
        print('final: ', directions)
        return directions


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()
        s.push([starting_vertex])
        # Create an empty Set to store visited vertices
        visited = set()
        # While the queue is not empty...
        while s.size() > 0:
            # Dequeue the first vertex
            v = s.pop()
            # If that vertex has not been visited...
            print(v)
            if v is not None:
                if v[-1] not in visited:
                    # Mark it as visited
                    if v[-1] == destination_vertex:
                        return v
                    visited.add(v[-1])
                    # Then add all of its neighbors to the back of the queue
                    for neighbor in self.vertices[v[-1]]:
                        z = v[:]
                        z.append(neighbor)
                        s.push(z)
                        print(s.stack)
