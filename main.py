import streamlit as st
from few_shot import FewShotPosts
from post_generator import generate_post
from textblob import TextBlob
import textstat  
from collab_db import init_collab_db, add_post, get_posts, update_post_status, add_comment

length_options = ["Short", "Medium", "Long"]
language_options = ["English", "Hinglish"]


def main():
    init_collab_db()
    st.title("LinkedIn Post Generator :sparkles:")
    st.subheader("Generate engaging LinkedIn posts with AI")

    col1, col2, col3 = st.columns(3)
    fs = FewShotPosts()
    tags = fs.get_tags()
    with col1:
        selected_tag = st.selectbox("Topic", options=tags)
    with col2:
        selected_length = st.selectbox("Length", options=length_options)
    with col3:
        selected_language = st.selectbox("Language", options=language_options)

    # Use session state to persist post
    if "post" not in st.session_state:
        st.session_state.post = ""

    if st.button("Generate"):
        st.session_state.post = generate_post(selected_length, selected_language, selected_tag)

    if st.session_state.post:
        post = st.session_state.post
        st.markdown("#### Preview")
        st.info(post)

        # Download and Copy
        st.download_button(
            label="Download Post",
            data=post,
            file_name="linkedin_post.txt",
            mime="text/plain"
        )
        st.code(post, language="markdown")

        # Sentiment Analysis
        blob = TextBlob(post)
        polarity = blob.sentiment.polarity
        subjectivity = blob.sentiment.subjectivity
        if polarity > 0:
            sentiment = "Positive :smiley:"
        elif polarity < 0:
            sentiment = "Negative :disappointed:"
        else:
            sentiment = "Neutral :neutral_face:"

        # More Analytics
        word_count = len(post.split())
        char_count = len(post)
        readability = textstat.flesch_reading_ease(post)
        readability_level = textstat.text_standard(post, float_output=False)

        if st.button("Save for Team Review"):
            add_post(post)
            st.success("Post saved for team review!")

        with st.expander("Show Analytics"):
            st.markdown(f"**Sentiment:** {sentiment} (Polarity: {polarity:.2f}, Subjectivity: {subjectivity:.2f})")
            st.progress(min(max(subjectivity, 0), 1), text="Subjectivity")
            st.markdown(f"**Word Count:** {word_count}")
            st.markdown(f"**Character Count:** {char_count}")
            st.markdown(f"**Readability Score:** {readability:.2f} (Flesch Reading Ease)")
            st.markdown(f"**Readability Level:** {readability_level}")

    # Team Collaboration Section (outside the if block)
    st.markdown("---")
    st.header("Review & Approve Posts")
    posts = get_posts()
    for post_id, content, status, comments in posts:
        with st.expander(f"Post #{post_id} [{status}]"):
            st.markdown(content)
            new_comment = st.text_area("Comments", value=comments, key=f"comment_{post_id}")
            if st.button("Save Comment", key=f"save_comment_{post_id}"):
                add_comment(post_id, new_comment)
                st.success("Comment saved!")
            if st.button("Approve", key=f"approve_{post_id}"):
                update_post_status(post_id, "Approved")
                st.success("Post approved!")
            if st.button("Request Edits", key=f"edit_{post_id}"):
                update_post_status(post_id, "Needs Edits")
                st.info("Requested edits for this post.")

if __name__ == "__main__":
    main()