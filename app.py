import streamlit as st
from dotenv import load_dotenv

load_dotenv()

# ── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Document Intelligence",
    page_icon=None,
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&display=swap');

    /* ── Base ── */
    html, body, [class*="css"] {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        font-size: 15px;
    }

    /* ── App background ── */
    .stApp {
        background-color: #0f1115;
    }

    /* ── Hide Streamlit chrome ── */
    #MainMenu, footer, header,
    section[data-testid="stSidebar"] {
        display: none !important;
    }

    /* ── Main block container ── */
    .block-container {
        max-width: 720px !important;
        padding: 0 1.25rem 5rem !important;
        margin: 0 auto !important;
    }

    /* ── Page header ── */
    .page-header {
        padding: 2.75rem 0 2rem;
        text-align: center;
    }

    .page-header h1 {
        font-size: 1.45rem;
        font-weight: 600;
        color: #f0f0ef;
        letter-spacing: -0.03em;
        margin: 0 0 0.35rem;
        line-height: 1.3;
    }

    .page-header p {
        font-size: 0.84rem;
        color: #5a5f6b;
        font-weight: 400;
        margin: 0;
        letter-spacing: 0.005em;
    }

    /* ── Divider under header ── */
    .header-rule {
        border: none;
        border-top: 1px solid #1e2128;
        margin: 0 0 1.75rem;
    }

    /* ── Chat messages ── */
    .message-row {
        display: flex;
        margin-bottom: 1rem;
        animation: fadeSlide 0.18s ease;
    }

    @keyframes fadeSlide {
        from { opacity: 0; transform: translateY(5px); }
        to   { opacity: 1; transform: translateY(0); }
    }

    .message-row.user  { justify-content: flex-end; }
    .message-row.ai    { justify-content: flex-start; }

    .msg-wrapper {
        display: flex;
        flex-direction: column;
        max-width: 72%;
    }

    .msg-wrapper.user { align-items: flex-end; }
    .msg-wrapper.ai   { align-items: flex-start; }

    .role-label {
        font-size: 0.68rem;
        font-weight: 500;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        color: #3a3f4a;
        margin-bottom: 0.35rem;
    }

    .bubble {
        padding: 0.8rem 1rem;
        border-radius: 12px;
        font-size: 0.875rem;
        line-height: 1.65;
        word-break: break-word;
    }

    .bubble.user {
        background: #2563eb;
        color: #ffffff;
        border-bottom-right-radius: 3px;
        font-weight: 400;
    }

    .bubble.ai {
        background: #1a1d23;
        color: #d4d6db;
        border: 1px solid #262b33;
        border-bottom-left-radius: 3px;
        font-weight: 400;
    }

    /* ── Empty state ── */
    .empty-state {
        text-align: center;
        padding: 4.5rem 1rem;
    }

    .empty-state .glyph {
        font-size: 1.4rem;
        color: #2a2f38;
        margin-bottom: 1rem;
        letter-spacing: 0.2em;
    }

    .empty-state h3 {
        font-size: 0.95rem;
        font-weight: 500;
        color: #3e434e;
        margin: 0 0 0.4rem;
    }

    .empty-state p {
        font-size: 0.8rem;
        color: #2e333c;
        margin: 0;
    }

    /* ── Chat input overrides ── */
    [data-testid="stChatInput"] {
        background-color: #1a1d23 !important;
        border: 1.5px solid #262b33 !important;
        border-radius: 11px !important;
        box-shadow: none !important;
    }

    [data-testid="stChatInput"]:focus-within {
        border-color: #2563eb !important;
        box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.12) !important;
    }

    [data-testid="stChatInput"] textarea {
        background: transparent !important;
        color: #d4d6db !important;
        font-family: 'Inter', sans-serif !important;
        font-size: 0.875rem !important;
        caret-color: #2563eb;
    }

    [data-testid="stChatInput"] textarea::placeholder {
        color: #3a3f4a !important;
    }

    [data-testid="stChatInput"] button {
        color: #2563eb !important;
    }

    [data-testid="stChatInput"] button:hover {
        color: #3b82f6 !important;
    }

    /* ── Alert ── */
    .stAlert {
        background: #1a1d23 !important;
        border: 1px solid #262b33 !important;
        color: #8b8f9a !important;
        border-radius: 8px !important;
        font-size: 0.82rem !important;
    }

    /* ── Spinner ── */
    .stSpinner > div {
        border-top-color: #2563eb !important;
    }

    /* ── Scrollbar ── */
    ::-webkit-scrollbar { width: 4px; }
    ::-webkit-scrollbar-track { background: transparent; }
    ::-webkit-scrollbar-thumb { background: #1e2128; border-radius: 8px; }
    ::-webkit-scrollbar-thumb:hover { background: #262b33; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ── Session state ─────────────────────────────────────────────────────────────
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


# ── Vector store init (lazy, cached per session) ──────────────────────────────
@st.cache_resource(show_spinner=False)
def load_vector_store():
    from langchain_community.vectorstores import Chroma
    from langchain_google_genai import GoogleGenerativeAIEmbeddings

    embedding_model = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")
    return Chroma(persist_directory="chroma_db", embedding_function=embedding_model)


# ── RAG response ──────────────────────────────────────────────────────────────
def get_response(question: str, vector_store) -> str:
    """Run MMR retrieval and pass context + question to Mistral."""
    from langchain_mistralai import ChatMistralAI
    from langchain_core.prompts import ChatPromptTemplate

    retriever = vector_store.as_retriever(
        search_type="mmr",
        search_kwargs={"k": 4, "fetch_k": 10, "lambda_mult": 0.5},
    )

    relevant_docs = retriever.invoke(question)

    if not relevant_docs:
        return "I could not find the answer in the document."

    context = "\n\n".join(doc.page_content for doc in relevant_docs)

    template = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                (
                    "You are a helpful AI assistant.\n\n"
                    "Use ONLY the provided context to answer the question.\n\n"
                    "If the answer is not present in the context, say: "
                    '"I could not find the answer in the document."'
                ),
            ),
            (
                "human",
                "Context:\n{context}\n\nQuestion:\n{question}",
            ),
        ]
    )

    llm = ChatMistralAI(model="mistral-small-2506")
    chain = template | llm
    response = chain.invoke({"context": context, "question": question})
    return response.content


# ── Page header ───────────────────────────────────────────────────────────────
st.markdown(
    '<div class="page-header">'
    "<h1>Document Intelligence</h1>"
    "<p>Ask questions from your indexed knowledge base</p>"
    "</div>"
    '<hr class="header-rule">',
    unsafe_allow_html=True,
)

# ── Chat history display ──────────────────────────────────────────────────────
if not st.session_state.chat_history:
    st.markdown(
        '<div class="empty-state">'
        '<div class="glyph">&#9632; &#9632; &#9632;</div>'
        "<h3>Ready to answer</h3>"
        "<p>Type a question below to query the knowledge base.</p>"
        "</div>",
        unsafe_allow_html=True,
    )
else:
    for message in st.session_state.chat_history:
        role = message["role"]
        content = message["content"]

        if role == "user":
            st.markdown(
                f'<div class="message-row user">'
                f'<div class="msg-wrapper user">'
                f'<div class="role-label">You</div>'
                f'<div class="bubble user">{content}</div>'
                f"</div></div>",
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                f'<div class="message-row ai">'
                f'<div class="msg-wrapper ai">'
                f'<div class="role-label">Assistant</div>'
                f'<div class="bubble ai">{content}</div>'
                f"</div></div>",
                unsafe_allow_html=True,
            )

# ── Chat input ────────────────────────────────────────────────────────────────
user_input = st.chat_input("Ask anything...")

if user_input and user_input.strip():
    try:
        vs = load_vector_store()
    except Exception as e:
        st.error(f"Could not load knowledge base: {e}")
        st.stop()

    st.session_state.chat_history.append(
        {"role": "user", "content": user_input.strip()}
    )

    with st.spinner(""):
        try:
            answer = get_response(user_input.strip(), vs)
        except Exception as e:
            answer = f"An error occurred while generating a response: {e}"

    st.session_state.chat_history.append({"role": "assistant", "content": answer})
    st.rerun()
