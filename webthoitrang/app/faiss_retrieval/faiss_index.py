import faiss

def load_index(index_path):
    """Loads a FAISS index from a .bin file."""
    return faiss.read_index(index_path)


def query_index(index, query_features, k=5):
    """Queries the FAISS index for k nearest neighbors."""
    distances, indices = index.search(query_features, k)
    return distances, indices

