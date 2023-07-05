# Import necessary libraries
import openai
import streamlit as st

# Main function to run the chat app
def main():
    st.title("AI Assistant Chat App")

    # Get user input for API key
    api_key = st.text_input("Enter your OpenAI API key:")

    # Set up OpenAI API credentials
    openai.api_key = api_key

    # Get user input
    user_input = st.text_input("You:")

    # Check if user wants to exit
    if user_input.lower() == "exit":
        st.write("Goodbye!")
        return

    # Get response from the chatbot using OpenAI GPT-3.5-turbo model
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_input}
        ]
    )

    # Extract the generated response from the OpenAI API response
    response_text = response.choices[0].message.content.strip()

    # Display the response
    st.text_area("AI Assistant:", value=response_text, height=200)

# Run the main function
if __name__ == "__main__":
    main()
