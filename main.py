#Implement adjacent matrix
#Implement adjacency list

#1 Adjacency Matrix
#Logic:
import pprint 
pp = pprint.PrettyPrinter(indent=4)

class Graph():
    _n = 0
    _g = [[0 for x in range(10)] for x in range(10)]

    def __init__(self, v):
        print(self._g)
        self._n = v
        for i in range(0, self._n):
            for j in range(0, self._n):
                self._g[i][j] = 0

    def display(self):
        print("\n\n Adjacency Matrix:", end="")

        for i in range(0, self._n):
            print()
            for j in range(0, self._n):
                print("", self._g[i][j], end="")

    def addEdge(self, vertex1, vertex2):
        self._g[vertex1][vertex2] = 1


class vertex():
    def __init__(self, key):
        self.key = key
        self.neighbours = {}

    def add_neighbours(self, neighbour, weight=0):
        self.neighbours[neighbour] = weight


class graph():
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        self.vertices[vertex.key] = vertex

    def get_vertex(self, key):
        try:
            return self.vertices[key]
        except KeyError:
            return None

    def add_Edge(self, to_key, from_key, weight=0):
        if from_key not in self.vertices:
            self.add_vertex(vertex(from_key))

        elif to_key not in self.vertices:
            self.add_vertex(vertex(to_key))

        self.vertices[from_key].add_neighbours(to_key, weight)

    def display(self):
        print("\nAdjacency List\n", end="")
        for x in self.vertices:
            print()


def bucket(word_list):
		response={}
		for x in word_list:
			for y in range(0,len(x)):
					curr=x[:y]+"_"+x[1+y:]
					#print(curr)
					if curr not in response:
						response[curr]=[]
					response[curr].append(x)
		return response


def build_graph(bucket):
	g={}
	for x in bucket.keys():
		for word1 in bucket[x]:
			for word2 in bucket[x]:
				if(word1!=word2):
					if word1 not in g:
						g[word1]=set()
					g[word1].add(word2)
	return g			


def bfs(g,s,d):
	visited=set()
	pp.pprint(g)
	queue=[]
	length=0
	queue.append((s,length))
	visited.add(s)
	length=0
	while(len(queue)!=0):
		a,l=queue.pop(0)
		print(a)
		print(queue)
		l=l+1
		if(a==d):
			return l

		for i in g[a]:
			if i not in visited:
				queue.append((i,l))
				visited.add(i)
	return 0

		





if __name__ == '__main__':
    # g=Graph(5)
    # g.display()
    # g.addEdge(1,0)
    # g.addEdge(2,4)
    # g.display()

    # g = graph()
    # g.add_vertex(vertex(1))
    # g.add_vertex(vertex(2))
    # g.add_vertex(vertex(3))
    # g.add_vertex(vertex(4))
    # g.add_vertex(vertex(5))
    # g.add_vertex(vertex(6))
    # g.add_vertex(vertex(7))
    # g.add_vertex(vertex(8))
    # g.add_Edge(1, 2)
    # g.add_Edge(4, 3)
    # g.add_Edge(5, 7)
    # g.add_Edge(4, 7)
    # g.add_Edge(8, 1)
    # g.add_Edge(6, 8)
    #g.display()

    word_list=["hot","dot","dog","lot","log","cog","hit"]
    buckets=bucket(word_list)
    #pp.pprint(buckets)
    g=build_graph(buckets)
    #pp.pprint(g)
    print(bfs(g,"hit","cog"))

