from services.retriever import get_retriever
from services.llm import get_llm
from services.prompt import get_prompt


def query_rag(question: str):
    retriever = get_retriever()
    llm = get_llm()
    prompt = get_prompt()

    # Step 1: retrieve relevant docs
    docs = retriever.invoke(question)

    # Step 2: combine context
    context = "\n\n".join([doc.page_content for doc in docs])

    # Step 3: create final prompt
    final_prompt = prompt.invoke({"context": context, "question": question})

    # Step 4: generate answer
    response = llm.invoke(final_prompt)

    return response.content
