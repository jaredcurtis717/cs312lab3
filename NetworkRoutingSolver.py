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
        # TODO: RETURN THE SHORTEST PATH FOR destIndex
        #       INSTEAD OF THE DUMMY SET OF EDGES BELOW
        #       IT'S JUST AN EXAMPLE OF THE FORMAT YOU'LL 
        #       NEED TO USE
        pathEdges = []
        totalLength = 0
        currentNode = destIndex
        while currentNode != self.source and self.prev[currentNode] is not None:
            edge = self.findEdge(currentNode, self.prev[currentNode])
            assert(edge is not None)
            totalLength += edge.length
            pathEdges.append(edge)
            currentNode = self.prev[currentNode]

        return {'cost': totalLength, 'path': pathEdges}

        """
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
        """

    def computeShortestPaths(self, srcIndex, use_heap=False):
        self.source = srcIndex
        t1 = time.time()
        self.dist = []
        self.prev = []
        # TODO: RUN DIJKSTRA'S TO DETERMINE SHORTEST PATHS.
        #       ALSO, STORE THE RESULTS FOR THE SUBSEQUENT
        #       CALL TO getShortestPath(dest_index)
        if use_heap:
            pass  # TODO use heap
        else:
            for i in self.network.getNodes():
                self.dist.append(math.inf)
                self.prev.append(None)

            self.dist[srcIndex] = 0

            H = {}
            for i in range(len(self.dist)):
                H[i] = self.dist[i]

            while len(H) > 0:
                u = self.deleteMin(H)
                for e in self.network.getNodes()[u].neighbors:
                    if self.dist[e.dest.node_id] > self.dist[e.src.node_id] + e.length:
                        self.dist[e.dest.node_id] = self.dist[e.src.node_id] + e.length
                        self.prev[e.dest.node_id] = e.src.node_id
                        H[e.dest.node_id] = self.dist[e.dest.node_id]

        t2 = time.time()
        return t2 - t1

    def deleteMin(self, d):
        smallestIn = None
        for i in d:
            if smallestIn is None:
                smallestIn = i
            if d[i] < d[smallestIn]:
                smallestIn = i
        del d[smallestIn]
        return smallestIn

    def findEdge(self, dest, src):
        for e in self.network.getNodes()[src].neighbors:
            if e.dest.node_id == dest:
                return e
        return None
