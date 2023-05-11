import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image
# import altair as alt
# # import os
# alt.renderers.enable('default')
#
# def folder_img_opener(path):
#     """
#
#     :param path:
#     :return: open the the imges in a folder and present them with a header
#     """
#     os.listdir()
# def anchorlink(n, title):
#     """
#     :param n: name of photo
#     :param title: what is the link name
#     :return:
#     """
#
#     if i == n:
#         st.header(f"{title}")

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# # # ---- LOAD ASSETS ----
# lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
# img_contact_form = Image.open("images/yt_contact_form.png")
# img_lottie_animation = Image.open("images/yt_lottie_animation.png")

# ---- HEADER SECTION ----
with st.container():
    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.subheader("bring back a litlebit of nature")
            st.title("organic designer")
            st.write(
                "I love to build furniture ,ecosystems and all that is between them."
            )
        with right_column:
            img = Image.open("tree1.png")
            st.image(img)

    # st.write("[Learn More >](https://pythonandvba.com)")

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        # st.header("What I do")
        st.write("##")
        st.write(
            """



              """
        )

    with right_column:
        img = Image.open("tree5.png")
        st.image(img)

    #     st_lottie(lottie_coding, height=300, key="coding")

# ---- PROJECTS ----
# st.sidebar.success("Select a demo above.")

with st.container():
    st.write("---")
    st.header("Get In Touch With Me")
    st.write("##")
    st.write(" my email: farfuraaa@gmail.com")
    # with right_column:
    #     img = Image.open("tree.png")
    #     st.image(img)
    st.write("---")
    st.header("My Projects")
    st.write("##")
    st.write("[tools](https://photos.app.goo.gl/ihT5Sty7Yx3NUsVL8)")
    img = Image.open("n (30).JPG")
    # st.image(img, width=200)
    # mage = Image.open("n (30).JPG")

    st.write("[furniture](https://photos.app.goo.gl/fuAaCVfaQq6TthMf9)")
    st.write("[scolpturs @ landscape](https://photos.app.goo.gl/zG2we5Hc3HNSrojv6)")

    # st.markdown("[plastic](#plastic)")
    # image_column, text_column = st.columns((1, 2))
    # with image_column:
    #     st.image(img_lottie_animation)
    img = Image.open("img3.JPG")
    st.image(img)
    img = Image.open("img4.JPG")
    st.image(img)
    st.video("https://youtu.be/Rc8Ot_JZP0U")
    st.video("https://youtu.be/nG71y2pjGNg")
    img = Image.open("img1.jpg")
    st.image(img)
    img = Image.open("img2.jpg")
    st.image(img)
    st.video("https://youtu.be/yd47jjJwuYY")


    # for loop that open all the jpg files that are name with (n)
    for i in range(200):
        # anchorlink(33,"plastic")
        try:
            img = Image.open(f"n ({i}).JPG")
            st.image(img)
        except:
            try:
                img = Image.open(f"n ({i}).jpg")
                st.image(img)
            except:
                pass




#     with text_column:
#         st.subheader("Integrate Lottie Animations Inside Your Streamlit App")
#         st.write(
#             """
#             Learn how to use Lottie Files in Streamlit!
#             Animations make our web app more engaging and fun, and Lottie Files are the easiest way to do it!
#             In this tutorial, I'll show you exactly how to do it
#             """
#         )
#         st.markdown("[Watch Video...](https://youtu.be/TXSOitGoINE)")
# # with st.container():
# #     image_column, text_column = st.columns((1, 2))
# #     with image_column:
# #         st.image(img_contact_form)
# #     with text_column:
# #         st.subheader("How To Add A Contact Form To Your Streamlit App")
# #         st.write(
# #             """
# #             Want to add a contact form to your Streamlit website?
# #             In this video, I'm going to show you how to implement a contact form in your Streamlit app using the free service ‘Form Submit’.
# #             """
# #         )
# #         st.markdown("[Watch Video...](https://youtu.be/FOULV9Xij_8)")

# ---- CONTACT ----

    # st.sidebar.markdown('<a href="mailto:farfuraaa@gmail.com">Contact us !</a>', unsafe_allow_html=True)
    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    # contact_form = """
    # <form action="https://formsubmit.co/farfuraaa@gmail.com" method="POST">
    #     <input type="hidden" name="_captcha" value="false">
    #     <input type="text" name="name" placeholder="Your name" required>
    #     <input type="email" name="email" placeholder="Your email" required>
    #     <textarea name="message" placeholder="Your message here" required></textarea>
    #     <button type="submit">Send</button>
    # </form>
    # """
    # left_column, right_column = st.columns(2)
    # with left_column:
    #     st.markdown(contact_form, unsafe_allow_html=True)
    # with right_column:
    #     st.empty()
#
# git add .    “git commit -m 'type any message here”    git push
