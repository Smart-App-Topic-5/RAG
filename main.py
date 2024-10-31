from graph_manager import GraphManager
from langchain_manager import LangChainManager
from visualizer import GraphVisualizer

def main():
    # Gestione del grafo
    graph_manager = GraphManager()
    
    # Visualizzazione del grafo
    GraphVisualizer.visualize(graph_manager.graph)

    # Gestione di LangChain
    langchain_manager = LangChainManager(graph_manager=graph_manager)

    # Esegui una query
    query_event = "Erasmus"
    partecipanti = langchain_manager.langchain_query(query_event, graph_manager)

    # Stampa il risultato
    print("Partecipanti all'evento", query_event, ":", partecipanti)

if __name__ == "__main__":
    main()
