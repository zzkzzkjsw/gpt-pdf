import pinecone

PINECONE_API_KEY ='bfddb7b9-7f4b-4513-b3ea-dfdf6eb8350b'
PINECONE_ENVIRONEMNENT = 'northamerica-northeast1-gcp'
pinecone.init(api_key=PINECONE_API_KEY, environment=PINECONE_ENVIRONEMNENT)

# pinecone.create_index("quickstart", dimension=8, metric="euclidean", pod_type="p1")

# res = pinecone.list_indexes()

index = pinecone.Index("quickstart")

# Upsert sample data (5 8-dimensional vectors)
index.upsert([
    ("F", [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]),
    ("B", [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2]),
    ("C", [0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3]),
    ("D", [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4]),
    ("E", [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5])
])

res = index.query(
  vector=[0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3],
  top_k=3,
  include_values=True
)
print(res)
# Returns:
# {'matches': [{'id': 'C',
#               'score': 0.0,
#               'values': [0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3]},
#              {'id': 'D',
#               'score': 0.0799999237,
#               'values': [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4]},
#              {'id': 'B',
#               'score': 0.0800000429,
#               'values': [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2]}],
#  'namespace': ''}
