import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image
import base64
import streamlit as st
# from st_clickable_images import clickable_images
import webbrowser
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.colors import LinearSegmentedColormap
import random
# from streamlit_player import st_player
# from IPython.display import Audio
import time

# n_sounds = 6
# # Define the audio file path
# audio_file = open(f"{random.randint(0,n_sounds)}.mp3", "rb").read()
#
# # Play the audio file using the st_player function
# st_player(audio_file)




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
# st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")


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
            st.subheader("Bring back a litlebit of nature")
            st.title("organic solutions")
            st.write(
                "I love to make music, furniture, ecosystems and everything in between."
            )
            st.write(" my email: arumdioscoridis@gmail.com")
        with right_column:
            img = Image.open("lily.jpg")
            st.image(img)

    # st.write("[Learn More >](https://pythonandvba.com)")

# ---- WHAT I DO ----
# with st.container():
#     st.write("---")
#     left_column, right_column = st.columns(2)
#     with left_column:
#         # st.header("What I do")
#         st.write("##")
#         st.write(
#             """
#
#
#
#               """
#         )

    # with right_column:
    #     img = Image.open("opening1.jpg")
    #     st.image(img)

    #     st_lottie(lottie_coding, height=300, key="coding")

# ---- PROJECTS ----
# st.sidebar.success("Select a demo above.")

# with st.container():
#     st.write("---")
#     # st.header("Get In Touch With Me")
#     # st.write("##")
#     if st.button("stop"):
#         play = 0

    # if st.button("play"):




    #         # # Read the audio file as binary data
    #         # with open(audio_file_path, "rb") as f:
    #         #     audio_data = f.read()
    #         #
    #         # # Encode the audio data in base64 format
    #         # audio_base64 = base64.b64encode(audio_data).decode()
    #         #
    #         # # Define the HTML audio tag with the base64-encoded audio data
    #         # audio_html = f'<audio src="data:audio/mp3;base64,{audio_base64}" autoplay></audio>'
    #         #
    #         # # Display the audio file using Streamlit's `write` method
    #         # st.write(audio_html, unsafe_allow_html=True)

    #         # Define the color gradient from brownish green to straw
    #     play = 1
    #     while play == 1:
    #         colors = [(random.random(), random.random(), random.random()), (random.random(), random.random(), random.random()), (random.random(), random.random(), random.random()),(random.random(), random.random(), random.random())]
    #         cmap_name = 'my_gradient'
    #         cm = LinearSegmentedColormap.from_list(cmap_name, colors)

    #         # Create a 2D array of values from 0 to 1
    #         x = np.linspace(0, 1, 5)
    #         y = np.linspace(0, 0.05, 6)
    #         xx, yy = np.meshgrid(x, y)
    #         z = np.random.rand(*xx.shape)


    #         # Create a function that updates the plot with a new color gradient
    #         def update(frame):
    #             new_colors = [
    #                 (0.2 + 0.3 * np.sin(frame * 1.1), 0.4 + 0.3 * np.sin(frame * 1.3), 0.1 + 0.3 * np.sin(frame * 1.5)),
    #                 (0.3 + 0.2 * np.sin(frame * 0.7), 0.5 + 0.2 * np.sin(frame * 1.2), 0.2 + 0.2 * np.sin(frame * 1.9)),
    #                 (0.5 + 0.2 * np.sin(frame * 0.1), 0.7 + 0.2 * np.sin(frame * 1.1), 0.4 + 0.2 * np.sin(frame * 1.7)),
    #                 (1, 1, 0.4)]
    #             new_cm = LinearSegmentedColormap.from_list(cmap_name, new_colors)
    #             im.set_cmap(new_cm)
    #             im.set_alpha(0.1 + 0.4 * np.sin(frame * 2))


    #         # Create the plot with the initial color gradient and texture
    #         fig, ax = plt.subplots()
    #         im = ax.imshow(z, cmap=cm, aspect='auto', extent=[0, 1, 0, 0.025], origin='lower', interpolation='bicubic')
    #         ax.set_axis_off()

    #         # Animate the plot with the color gradient changing over time
    #         ani = FuncAnimation(fig, update, frames=np.linspace(0, 5, 1), interval=30000)

    #         # Display the animated plot in Streamlit

    #         st.pyplot(fig, bbox_inches='tight', pad_inches=0)

    #         # Define the file path of the MP3 file
    #         audio_file_path = f"{random.randint(1, 5)}.mp3"

    #         # Read the audio file as binary data
    #         with open(audio_file_path, "rb") as f:
    #             audio_data = f.read()

    #         # Encode the audio data in base64 format
    #         audio_base64 = base64.b64encode(audio_data).decode()

    #         # Generate a unique identifier for the HTML audio tag
    #         unique_id = int(time.time())

    #         # Define the updated HTML audio tag with the new unique identifier
    #         audio_html = f'<audio src="data:audio/mp3;base64,{audio_base64}" autoplay id="{unique_id}"></audio>'
    #         # Display the updated HTML audio tag using Streamlit's `write` method
    #         st.write(audio_html, unsafe_allow_html=True)
    #         T = 0.7
    #         time.sleep(T)
    #         # st.pyplot(clear_figure=True)

    if st.button("Generate random organic patterns with code I made"):




        # # Read the audio file as binary data
        # with open(audio_file_path, "rb") as f:
        #     audio_data = f.read()
        #
        # # Encode the audio data in base64 format
        # audio_base64 = base64.b64encode(audio_data).decode()
        #
        # # Define the HTML audio tag with the base64-encoded audio data
        # audio_html = f'<audio src="data:audio/mp3;base64,{audio_base64}" autoplay></audio>'
        #
        # # Display the audio file using Streamlit's `write` method
        # st.write(audio_html, unsafe_allow_html=True)

        # Define the color gradient from brownish green to straw
        colors = [(random.random(), random.random(), random.random()), (random.random(), random.random(), random.random()), (random.random(), random.random(), random.random()),(random.random(), random.random(), random.random())]
        cmap_name = 'my_gradient'
        cm = LinearSegmentedColormap.from_list(cmap_name, colors)

        # Create a 2D array of values from 0 to 1
        x = np.linspace(0, 1, 5)
        y = np.linspace(0, 0.05, 6)
        xx, yy = np.meshgrid(x, y)
        z = np.random.rand(*xx.shape)


        # Create a function that updates the plot with a new color gradient
        def update(frame):
            new_colors = [
                (0.2 + 0.3 * np.sin(frame * 1.1), 0.4 + 0.3 * np.sin(frame * 1.3), 0.1 + 0.3 * np.sin(frame * 1.5)),
                (0.3 + 0.2 * np.sin(frame * 0.7), 0.5 + 0.2 * np.sin(frame * 1.2), 0.2 + 0.2 * np.sin(frame * 1.9)),
                (0.5 + 0.2 * np.sin(frame * 0.1), 0.7 + 0.2 * np.sin(frame * 1.1), 0.4 + 0.2 * np.sin(frame * 1.7)),
                (1, 1, 0.4)]
            new_cm = LinearSegmentedColormap.from_list(cmap_name, new_colors)
            im.set_cmap(new_cm)
            im.set_alpha(0.1 + 0.4 * np.sin(frame * 2))


        # Create the plot with the initial color gradient and texture
        fig, ax = plt.subplots()
        im = ax.imshow(z, cmap=cm, aspect='auto', extent=[0, 1, 0, 0.025], origin='lower', interpolation='bicubic')
        ax.set_axis_off()

        # Animate the plot with the color gradient changing over time
        ani = FuncAnimation(fig, update, frames=np.linspace(0, 5, 1), interval=30000)

        # Display the animated plot in Streamlit

        st.pyplot(fig, bbox_inches='tight', pad_inches=0)

        # Define the file path of the MP3 file
        audio_file_path = f"{random.randint(1, 5)}.mp3"

        # Read the audio file as binary data
        with open(audio_file_path, "rb") as f:
            audio_data = f.read()

        # Encode the audio data in base64 format
        audio_base64 = base64.b64encode(audio_data).decode()

        # Generate a unique identifier for the HTML audio tag
        unique_id = int(time.time())

        # Define the updated HTML audio tag with the new unique identifier
        audio_html = f'<audio src="data:audio/mp3;base64,{audio_base64}" autoplay id="{unique_id}"></audio>'
        # Display the updated HTML audio tag using Streamlit's `write` method
        st.write(audio_html, unsafe_allow_html=True)


    # Hide the Streamlit menu and footer
    hide_menu_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
        """
    st.markdown(hide_menu_style, unsafe_allow_html=True)
    # with right_column:
    #     img = Image.open("tree.png")
    #     st.image(img)
    st.write("---")
    st.header("My Projects")
    st.write("##")
    # st.write("[tools](https://photos.app.goo.gl/ihT5Sty7Yx3NUsVL8)")
    # # img = Image.open("n (30).JPG")
    # # st.image(img, width=200)
    # # mage = Image.open("n (30).JPG")
    #
    # st.write("[furniture](https://photos.app.goo.gl/fuAaCVfaQq6TthMf9)")
    # st.write("[scolpturs @ landscape](https://photos.app.goo.gl/zG2we5Hc3HNSrojv6)")




    # images = []
    # for file in ["tools.png", "fur.png", "landscape.png"]:
    #     with open(file, "rb") as image:
    #         encoded = base64.b64encode(image.read()).decode()
    #         images.append(f"data:image/jpeg;base64,{encoded}")
    #
    # clicked = clickable_images(
    #     images,
    #     titles=[f"Image #{str(i)}" for i in range(len(images))],
    #     div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"},
    #     img_style={"margin": "5px", "height": "200px"},
    # )
    #
    # if clicked == 0:
    #
    #     url = 'https://photos.app.goo.gl/ihT5Sty7Yx3NUsVL8'
    #     webbrowser.open_new_tab(url)
    #
    #
    #
    # if clicked == 1:
    #     url = 'https://photos.app.goo.gl/fuAaCVfaQq6TthMf9'
    #     webbrowser.open_new_tab(url)
    #
    #
    #
    # if clicked == 2:
    #     url = 'https://photos.app.goo.gl/zG2we5Hc3HNSrojv6'
    #     webbrowser.open_new_tab(url)

    # url = "https://photos.app.goo.gl/zG2we5Hc3HNSrojv6"
    # image_path = "landscape.png"
    #
    # link = f'<a href="{url}" target="_blank"><img src="data:image/jpeg;base64,{base64.b64encode(open(image_path, "rb").read()).decode()}" alt="Description of the image"></a>'
    #
    
    # st.markdown(link, unsafe_allow_html=True)
    with st.container():
        with left_column: 
    
            link = f'<a href="{"https://farfura.bandcamp.com/?from=viewsite_dashboard"}" target="_blank"><img src="data:image/jpeg;base64,{base64.b64encode(open("sounds.jpg", "rb").read()).decode()}" alt="Description of the image" width="350"></a>'
            st.markdown(link, unsafe_allow_html=True)
        
            link = f'<a href="{"https://photos.app.goo.gl/ihT5Sty7Yx3NUsVL8"}" target="_blank"><img src="data:image/jpeg;base64,{base64.b64encode(open("tools.jpg", "rb").read()).decode()}" alt="Description of the image" width="350"></a>'
            st.markdown(link, unsafe_allow_html=True)

        with right_column:
            link = f'<a href="{"https://photos.app.goo.gl/fuAaCVfaQq6TthMf9"}" target="_blank"><img src="data:image/jpeg;base64,{base64.b64encode(open("fur.jpg", "rb").read()).decode()}" alt="Description of the image" width="350"></a>'
            st.markdown(link, unsafe_allow_html=True)
        
            link = f'<a href="{"https://photos.app.goo.gl/zG2we5Hc3HNSrojv6"}" target="_blank"><img src="data:image/jpeg;base64,{base64.b64encode(open("landscape.jpg", "rb").read()).decode()}" alt="Description of the image" width="350"></a>'
            st.markdown(link, unsafe_allow_html=True)




    urls = [
        "https://photos.app.goo.gl/ihT5Sty7Yx3NUsVL8",
        "https://photos.app.goo.gl/fuAaCVfaQq6TthMf9",
        "https://photos.app.goo.gl/zG2we5Hc3HNSrojv6"
    ]

    image_paths = [      
        "tools.jpg",
        "fur.jpg",
        "landscape.jpg"
    ]

    col1, col2, col3 = st.columns(3)

    for url, path, col in zip(urls, image_paths, [col1, col2, col3]):
        with col:
            link = f'<a href="{url}" target="_blank"><img src="data:image/jpeg;base64,{base64.b64encode(open(path, "rb").read()).decode()}" alt="Description of the image" width="222"></a>'
            st.markdown(link, unsafe_allow_html=True)




    # Display the image
    # image = Image.open(image_url)
    # st.image(image, caption='Description of the image', use_column_width=True)
    # st.markdown(f"Image #{clicked} clicked" if clicked > -1 else "No image clicked")
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
    n_photos = 50
    if st.button("load more"):
        n = []
        for j in range(n_photos):
            i = random.randint(0, n_photos)

            for m in range(len(n)):
                if n[m] == i:
                    i = random.randint(0, n_photos)

            n.append(i)
        print(n)
        for i in range(n_photos):
            # anchorlink(33,"plastic")
            try:
                img = Image.open(f"n ({n[i]}).JPG")
                st.image(img)
            except:
                try:
                    img = Image.open(f"n ({n[i]}).jpg")
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
st.write("---")
st.write("##")
st.write("[thanks for Sven for the base line website code exmpple](https://www.youtube.com/@CodingIsFun) ")
st.write("and thanks for gtp for code consultation")
