from tqdm import tqdm


class DocumentEnricher:

    def __init__(self):
        pass 

    def enrich_document(self, documents, processors, text_col='text'):
        for doc in tqdm(documents, desc="Enriching documents using processors: "+str(processors)): 
            for (processor, field) in processors: 
                doc.update({field: processor(doc[text_col])})
 
    