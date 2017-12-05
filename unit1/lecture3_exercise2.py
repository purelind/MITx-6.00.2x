# -*- coding: utf-8 -*-


from lecture3_segments import Node, Graph, Edge


nodes = []
nodes.append(Node("ABC")) # nodes[0]
nodes.append(Node("ACB")) # nodes[1]
nodes.append(Node("BAC")) # nodes[2]
nodes.append(Node("BCA")) # nodes[3]
nodes.append(Node("CAB")) # nodes[4]
nodes.append(Node("CBA")) # nodes[5]

g = Graph()
for n in nodes:
    g.addNode(n)


for i in range(len(nodes)):
    for j in range(i+1, len(nodes)):
        for k in range(3):
            if nodes[i].getName()[k] == nodes[j].getName()[k] and k != 1:
                print(nodes[i], nodes[j])
                g.addEdge(Edge(nodes[i], nodes[j]))
print(g)
