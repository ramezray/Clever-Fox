import streamlit as st

from server import generate_question, answer_question


def main():
    """Main function for the Streamlit app"""
    st.title("Clever Fox 🦊")
    if st.button("Generate Question"):
        st.session_state.answer = None  # Clear previous answer
        generate_question()

    st.markdown("---")
    st.subheader("Solve with Clever Fox")

    # Show the generated question if available
    question = st.session_state.get("generated_question", None)
    if question:
        st.info(f"Question: {question}")

    answer = st.session_state.get("answer", None)

    # Track if user requested to see the answer
    if "show_answer" not in st.session_state:
        st.session_state.show_answer = False

    solve_btn = st.button("How Clever Fox will Solve it!")
    if solve_btn and question:
        st.session_state.show_answer = True

    if st.session_state.show_answer and answer:
        st.success("Answer:")
        st.write(answer)


if __name__ == "__main__":
    main()
