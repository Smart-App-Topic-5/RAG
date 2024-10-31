import networkx as nx

class GraphManager:
    def __init__(self):
        # Crea un grafo diretto
        self.graph = nx.DiGraph()
        self.initialize_graph()

    def initialize_graph(self):
        # Definisci le entità
        self.graph.add_node("Gioele", tipo="Persona", età=25)
        self.graph.add_node("Chiara", tipo="Persona", età=25)
        self.graph.add_node("Giorgio", tipo="Persona", età=25)
        self.graph.add_node("Palma di Mallorca", tipo="Luogo")
        self.graph.add_node("Erasmus", tipo="Evento")

        # Aggiungi relazioni
        self.graph.add_edge("Gioele", "Erasmus", relazione="partecipante")
        self.graph.add_edge("Chiara", "Erasmus", relazione="partecipante")
        self.graph.add_edge("Giorgio", "Erasmus", relazione="partecipante")
        self.graph.add_edge("Erasmus", "Palma di Mallorca", relazione="si svolge a")

    def query_graph(self, node):
        """Funzione per interrogare il grafo e ottenere i partecipanti a un evento."""
        return list(self.graph.predecessors(node))
