from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Developer Sahil", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r=requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style{f.read()}</style>", unsafe_allow_html= True)
        local_css("style/style.css ")

lottie_coding = load_lottieurl("https://assets6.lottiefiles.com/private_files/lf30_kw5jwkm0.json")
#img_contact_form = Image.open("Images/cyber.png")
#img_lottie_animation = Image.open("Images/lock.png")
st.subheader("Hii,Myself Sahil")
st.title("A Cybersecurity Analyst From India")
st.write("I'm Eager to learn new things and capture it fastly")
st.write("[learn more>](https://www.youtube.com/shorts/-vVTCQyjbZ8)")

 
st.write("----")
left_column, right_column = st.columns(2)
with left_column:
    st.header("what I Do")
    st.write("##")
    st.write("""• Maintained inventory of computer parts to keep accurate log and records.
• Utilised components and equipment to configure networks and integrate systems.
Surveilled systems to determine needs for upgrades and enhancements.
• Conducted data backups to enable tracking history and preserve memory and information.
•Troubleshot problems arising between data and voice communication systems.
• Used technical knowledge of telecommunications engineering to identify and solve operational problems.
Recommended best technology and hardware to use in network implementation.
Detected and resolved issues with current network systems to avoid bugs
and errors""")
with right_column:
    st_lottie(lottie_coding, height=300,key="cybersecurity")

with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        #st.image(img_lottie_animation)
  #  with text_column:
        st.subheader("Integration")
        st.write("""• Conducted data backups to enable tracking history and preserve memory and information.
•Troubleshot problems arising between data and voice communication systems.
""")
with st.container():
    image_column,text_column = st.columns((1,2))
    with image_column:
      #  st.image(img_contact_form )
  #  with text_column:
        st.subheader("Integration")
        st.write("""• Conducted data backups to enable tracking history and preserve memory and information.
    •Troubleshot problems arising between data and voice communication systems.
    """)

with st.container():
    st.write("---")
    st.header("Get In Touch with me!")
    st.write("##")

    contact_form = """<form action="https://formsubmit.co/sahiltongale1310@gmail.com" method="POST">
     <input type ="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder = "Your Name" required>
     <input type="email" name="email" placeholder = "Your email" required>
     <textarea name="message" placeholder = "Your message here" required></textarea>
     <button type="submit">Send</button>
</form>
"""
left_column,right_column = st.columns(2)
with left_column:
    st.markdown(contact_form, unsafe_allow_html= True)
with right_column:
    st.empty()