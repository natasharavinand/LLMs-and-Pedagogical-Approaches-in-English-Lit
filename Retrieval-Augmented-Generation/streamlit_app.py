import streamlit as st
from retrieval_augmented_generation import get_llm_response_with_prompt, get_user_recommendation

st.title("LLMs and Pedagogical Approaches in English Literature")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

sidebar = st.sidebar

sidebar.title("Select which course you would like to focus on:")

course = sidebar.radio(
    "Course",
    ["Introduction to the Theory of Literature", "Milton", "Modern Poetry", "The American Novel Since 1945"]
)

recommendation_title = sidebar.title("Recommendation")
default_recommendation = sidebar.markdown(
        "Chat with me more to have a detailed recommendation of text."
)

if st.session_state.messages:
    default_recommendation.empty()
    recommendation = sidebar.markdown(
        get_user_recommendation(course, st.session_state.messages)
    )

if prompt := st.chat_input("Enter a question you have from your English literature coursework."):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    previous_responses = [msg["content"] for msg in st.session_state.messages if msg["role"] == "ai"]

    response = get_llm_response_with_prompt(course, prompt, previous_responses)

    with st.chat_message("ai"):
        st.markdown(response)

    st.session_state.messages.append({"role": "ai", "content": response})
