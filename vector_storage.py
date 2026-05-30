import chromadb
from data_generator import generate_incidents

chroma_client = chromadb.Client()
collection = chroma_client.create_collection(name="incidents")

def store_incidents_in_db():
    incidents = generate_incidents(200)
    for incident in incidents:
        collection.add(
            ids = [incident.id],
            documents = [f"{incident.title} {incident.root_cause or ''} {incident.resolution or ''} {', '.join(incident.tags)} {incident.description or ''}"],
            metadatas= [{"severity": incident.severity, "status": incident.status, "service": incident.service}]
        )
    return

def get_similar_incidents(user_query):
    results = collection.query(
    query_texts=[user_query],
    n_results=5
    )

    filtered_docs = []
    filtered_metadatas = []

    for doc, meta, distance in zip(results['documents'][0], results['metadatas'][0], results['distances'][0]):
        if distance < 0.3:
            filtered_docs.append(doc)
            filtered_metadatas.append(meta)


    return filtered_docs, filtered_metadatas