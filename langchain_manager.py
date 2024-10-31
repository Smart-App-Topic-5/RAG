from transformers import GPT2LMHeadModel, GPT2Tokenizer, pipeline
from langchain.chains import RetrievalQA
from langchain_core.runnables import RunnableLambda

class LangChainManager:
    def __init__(self, graph_manager):
        # Carica il tokenizer e il modello
        model_name = 'gpt2'
        tokenizer = GPT2Tokenizer.from_pretrained(model_name)
        model = GPT2LMHeadModel.from_pretrained(model_name)
        
        # Crea una pipeline per il modello
        self.llm_pipeline = pipeline("text-generation", model=model, tokenizer=tokenizer)

        # Wrapping della pipeline in un RunnableLambda
        self.llm = RunnableLambda(lambda prompt: self.llm_pipeline(prompt, max_length=100)[0]['generated_text'])

        # Inizializza RetrievalQA con un retriever
        self.qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            retriever=self.create_retriever(graph_manager)
        )

    def create_retriever(self, graph_manager):
        """Crea un retriever che interroga il grafo."""
        return RunnableLambda(lambda event: graph_manager.query_graph(event))

    def langchain_query(self, event):
        """Interroga il grafo per ottenere informazioni sui partecipanti all'evento."""
        partecipanti = self.qa_chain({"query": event})  # Esegui la query attraverso qa_chain
        return partecipanti
