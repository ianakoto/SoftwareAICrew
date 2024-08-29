import sys
import streamlit as st
from streamer import StreamToExpander
from main import run
from utils import get_lantrace_url


def icon(emoji: str):
    st.set_page_config(page_title="Software Engineering Idea Processor", page_icon=emoji)


def display_langtrace_button():
    langtrace_url = get_lantrace_url()
    st.markdown(f"[Click here to view metrics on Langtrace]({langtrace_url})", unsafe_allow_html=True)


def sidebar_form():
    with st.sidebar:
        st.header("👇 Enter your project idea")
        with st.form("project_form"):
            project_idea = st.text_area("Describe your software project idea:",
                                        placeholder="A web app for managing personal finances")
            submitted = st.form_submit_button("Submit")
        st.divider()
        display_langtrace_button()
        st.sidebar.markdown(
            """
            Created by [Ian Akoto](https://www.linkedin.com/in/iancecilakoto/)
            """,
            unsafe_allow_html=True
        )
    return submitted, project_idea


def main():
    icon("💡")
    st.subheader("Software Engineering Idea Processor", divider="rainbow", anchor=False)

    submitted, project_idea = sidebar_form()

    if submitted:
        with st.status("🤖 **Agents at work...**", state="running", expanded=True) as status:
            with st.container(height=500, border=True):
                sys.stdout = StreamToExpander(st)
                results = run(inputs={"idea": project_idea})
            status.update(label="✅ Project Plan Ready!", state="complete", expanded=False)
        st.subheader("Here is your Project Codes", anchor=False, divider="rainbow")
        st.markdown(results)



if __name__ == "__main__":
    main()
