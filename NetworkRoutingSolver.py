#!/usr/bin/python3
import math

from CS312Graph import *
import time


class NetworkRoutingSolver:
    def __init__(self):
        # Added these 3 lines
        self.network = None
        self.dest = None
        self.source = None
        self.prev = None
        self.dist = None

    def initializeNetwork(self, network):
        assert (type(network) == CS312Graph)
        self.network = network

    def getShortestPath(self, destIndex):
        for node in self.network.getNodes():
            if node.node_id == destIndex:
                self.dest = node
                break
        # TODO: RETURN THE SHORTEST PATH FOR destIndex
        #       INSTEAD OF THE DUMMY SET OF EDGES BELOW
        #       IT'S JUST AN EXAMPLE OF THE FORMAT YOU'LL 
        #       NEED TO USE
        '''
                path_edges = []
                total_length = 0
                node = self.network.nodes[self.source]
                edges_left = 3
                while edges_left > 0:
                    edge = node.neighbors[2]
                    path_edges.append((edge.src.loc, edge.dest.loc, '{:.0f}'.format(edge.length)))
                    total_length += edge.length
                    node = edge.dest
                    edges_left -= 1
                return {'cost': total_length, 'path': path_edges}
        '''
        pathEdges = []
        totalLength = 0
        currentNode = self.dest
        while self.prev[currentNode] is not None:
            backPath = self.prev[currentNode]
            totalLength += backPath.length
            pathEdges.append(backPath)
            currentNode = backPath.src  # maybe source?
        if currentNode != self.source:
            return {'cost': math.inf, 'path': pathEdges}
        else:
            return {'cost': totalLength, 'path': pathEdges}

    def computeShortestPaths(self, srcIndex, use_heap=False):
        self.source = srcIndex
        t1 = time.time()
        self.dist = {}
        self.prev = {}
        # TODO: RUN DIJKSTRA'S TO DETERMINE SHORTEST PATHS.
        #       ALSO, STORE THE RESULTS FOR THE SUBSEQUENT
        #       CALL TO getShortestPath(dest_index)
        if use_heap:
            pass  # TODO use heap
        else:
            for u in self.network.getNodes():
                self.dist[u] = math.inf
                self.prev[u] = None
                if u.node_id == srcIndex:
                    self.dist[u] = 0

            H = self.dist.copy()
            while len(H) > 0:
                u = self.deleteMin(H)
                for v in u.neighbors:  # v is each edge coming from u
                    if self.dist[v.dest] > self.dist[u] + v.length:
                        self.dist[v.dest] = self.dist[u] + v.length
                        self.prev[v.dest] = v
                        # H[v] = self.dist[u] + v.length

        t2 = time.time()
        return t2 - t1

    def deleteMin(self, d):
        smallest = None
        smallestNode = None
        for node in d:
            if smallest is None:
                smallest = d[node]
                smallestNode = node

            elif self.dist[node] < smallest:
                smallest = self.dist[node]
                smallestNode = node

        d.pop(smallestNode)
        return smallestNode
