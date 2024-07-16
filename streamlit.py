import streamlit as st
from prompts import prompt
from backend import bot_response

st.set_page_config(
    page_title="Chat-Bot",
    page_icon="C:\\Users\\VanshLambole\\OneDrive - Rapyder Cloud Solutions Pvt Ltd\\DA Projects\\Bright Champs\\rapyder_logo_1.png")


# Chat-Bot title
st.title(""":rainbow[Student Assistant Chat-Bot]""")


# Initialize chat history in session state if not already present
if "messages" not in st.session_state:
    st.session_state.messages = []


# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        if message["role"] == 'user':
            start_index = message["content"].find("Question:")
            end_index = message["content"].find("Answer:")
            question_text = message["content"][(
                start_index + len("Question:")):end_index].strip()
            st.markdown(question_text)
        elif message['role'] == 'assistant':
            st.markdown(message["content"])


# Accept user input
user_input = st.chat_input(placeholder="Ask your queries...")


if user_input:
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(user_input)

# Add user message to chat history
    query_generation_prompt = prompt.format(user_input=user_input)

    # Get bot response
    bot_res = prompt.format(
        user_input=user_input)

    st.session_state.messages.append({"role": "user", "content": bot_res})

    response = bot_response(st.session_state.messages)
    # print("response :::::: ", response)

# Add bot response to chat history
    st.session_state.messages.append(
        {"role": "assistant", "content": response})

# Display bot response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
