import chromadb
from data_generator import generate_incidents

import chromadb
chroma_client = chromadb.Client()
collection = chroma_client.create_collection(name="incidents")

def store_incidents_in_db():
    incidents = generate_incidents(200)
    for incident in incidents:
        collection.add(
            ids = [incident.id],
            documents = [f"{incident.title} {incident.root_cause or ''} {incident.resolution or ''} {incident.tags}"]
        )
    return collection

def get_similar_incidents(user_query):
    context = collection.query(
    query_texts=[user_query],
    n_results=10
    )['documents']

    print(context)
    return context