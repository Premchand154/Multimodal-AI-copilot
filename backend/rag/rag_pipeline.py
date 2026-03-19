from rag.text_splitter import split_text
from rag.vector_store import vector_store
from llm.llm_inference import generate_response
from memory import memory


def ingest_text(text):
    chunks = split_text(text)
    vector_store.build(chunks)


def ask_ai(question):
    docs = vector_store.search(question)
    context = "\n".join(docs)

    mem_ctx = memory.get_context()
    answer = generate_response(context, question, mem_ctx)

    memory.add(question, answer)
    return answer


if __name__ == "__main__":

    question = "What is computer vision?"

    response = ask_ai(question)

    print(response)