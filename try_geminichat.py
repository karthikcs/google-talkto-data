from langchain_google_vertexai import ChatVertexAI

llm = ChatVertexAI(
    model="gemini-1.5-flash-001",
    temperature=0.7,
    # max_tokens=None,
    # max_retries=6,
    # stop=None,
    # other params...
)

messages = [
    (
        "system",
        "You are a helpful assistant that translates English to Spanish. Translate the user sentence.",
    ),
    ("human", "I love programming."),
]
ai_msg = llm.invoke(messages)
print(ai_msg.content)