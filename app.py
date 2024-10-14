import streamlit as st
from logistic_data import logistics_data

st.title("Logistics Data Bot")

st.sidebar.title("Data Sources")

## Streamlit upload an XL file 
file = st.sidebar.file_uploader("Upload a file", type=["xlsx"])
if file:
    data = logistics_data(file.name)
    st.sidebar.markdown("### Sheets in the file")
    for sheet in data.sheets:
        st.sidebar.markdown(f"* {sheet}" )


# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("Do you have any query about Logistics Data?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    response, detailed_response = data.chat(prompt)
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
        st.markdown("### Detailed Response")
        st.markdown(detailed_response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})