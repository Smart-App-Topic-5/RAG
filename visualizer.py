import matplotlib.pyplot as plt
import networkx as nx  

class GraphVisualizer:
    @staticmethod
    def visualize(graph):
        plt.figure(figsize=(8, 6))
        pos = nx.spring_layout(graph)  # Posizionamento dei nodi
        nx.draw(graph, pos, with_labels=True, node_color='lightblue', node_size=2000,
                font_size=10, font_weight='bold', edge_color='gray', arrows=True)
        labels = nx.get_edge_attributes(graph, 'relazione')
        nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
        plt.title("Knowledge Graph di Esempio (Grafo Diretto)")
        plt.show()
