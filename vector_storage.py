import chromadb
from data_generator import generate_incidents

chroma_client = chromadb.Client()
collection = chroma_client.create_collection(name="incidents")

def store_incidents_in_db():
    incidents = generate_incidents(10)
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

def get_last_incident():
    data = collection.get()
    ids = data["ids"]
    max_id= 0
    for id in ids:
        string_num_array = id.split("-")
        str_number = string_num_array[1]
        number = int(str_number)

        if number > max_id:
            max_id = number
    
    new_Id = max_id + 1
    formatted_Id = f"INC-{str(new_Id).zfill(4)}"
    results = formatted_Id

    return results

if __name__ == "__main__":
    store_incidents_in_db()
    get_last_incident()