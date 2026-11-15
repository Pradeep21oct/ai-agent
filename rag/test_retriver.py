from retriver import load_documents, retrive

documents = load_documents()
for name, content in documents.items():
    print(name)
    print(content)
    print("=" * 40)




file_name, file_content = retrive("weather")
print(file_name)
print(file_content)
print("*" * 40)