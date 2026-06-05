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


    return results['documents'][0], results['metadatas'][0]