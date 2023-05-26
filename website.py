from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="My Website",page_icon=":slightly_smiling_face:",layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None 
    return r.json()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")              

lottie_coding = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_TecLfM.json")
img_contact_force = Image.open("image/WhatsApp Image 2023-05-22 at 20.51.02.png")
img_lottie_animation = Image.open("image/WhatsApp Image 2023-05-22 at 20.49.51.png")

with st.container():
    st.subheader("Hi i am praneeth")
    st.title("I love my Father")
    st.write("Gratitude for his love: Start by expressing your gratitude for the love and affection your father has shown you throughout your life. Let him know how much his presence has meant to you.")
    st.write("Support and guidance: Highlight the ways in which your father has supported and guided you. Whether it's through his advice, encouragement, or simply being there for you during challenging times, acknowledge the role he has played in shaping your life.")
    st.write("Role model: Share specific examples of how your father has been a role model to you. Talk about the qualities you admire in him, such as his integrity, work ethic, kindness, or perseverance, and explain how these traits have inspired you.")
    st.write("Sacrifices and dedication: Recognize the sacrifices your father has made for your well-being and happiness. Whether it's working long hours, providing for the family, or putting your needs before his own, acknowledging his dedication will make him feel appreciated.")
    st.write("Shared experiences: Recall cherished memories and moments you've shared together. Talk about the times you've laughed, learned, and grown together, emphasizing how those experiences have enriched your life and strengthened your bond.")
    st.write("Unconditional love: Assure your father that your love for him is unconditional. Let him know that you value him for who he is and that your love extends beyond any achievements or circumstances.")
    st.write("Future aspirations: Discuss your hopes and dreams, and how your father has influenced them. Share your ambitions and reassure him that his love and support have been instrumental in shaping your goals for the future.")

with st.container():
    st.write("---")
    left_column,right_column = st.columns(2)
    with left_column:
        st.header("My Father is Great")
        st.write("##")
        st.write(
            """The love between a child and their father is a bond that holds immense significance and is often characterized by a deep sense of admiration, respect, and affection. It is a unique and irreplaceable relationship that shapes a person's life in profound ways. The love for a father is a blend of gratitude, guidance, and a sense of security.
       """ )

with right_column:
    st_lottie(lottie_coding,height=300,key="father")

with st.container():
    st.write("----")
    st.header("My Father")
    st.write("##")
    image_column,text_column = st.columns((1,2))
    with image_column:
        st.image(img_lottie_animation)
       
    with text_column:
        st.subheader("My Father name is SATYA VARA PRASAD BHAVANA ")
        st.write("""

                    From the earliest stages of life, 
                    a father is often seen as a protector and provider,
                     ensuring the well-being and safety of their child. 
                     Their love is demonstrated through their constant support, 
                     both emotionally and physically, as they offer guidance and wisdom to navigate life's challenges.
                     A father's presence is a source of comfort, giving their child a sense of security and stability. 
                     
                       """)    
with st.container():
    image_column,text_column = st.columns((1,2))
    with image_column:
        st.image(img_contact_force)
    with text_column:
        st.subheader("I Love My Family")
        st.write("""
                    As time goes by, the love for a father often matures into a profound appreciation for the influence 
                    he has had on shaping one's character and life trajectory. 
                    Memories of shared experiences, laughter, 
                    and even the occasional disagreements become cherished treasures, 
                    reminding us of the special bond we share with our fathers.
                 """)      


with st.container():
   st.write("---")
   st.header("Get in touch With me")
   st.write("##")


   contact_form = """
<form action="https://formsubmit.co/santhibhavana1234@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="flase"
     <input type="name" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placehloder="Your message here" required></textarea>
     <button type="submit">Send</button>
</form>
"""
left_column,right_column = st.columns(2)
with left_column:
    st.markdown(contact_form,unsafe_allow_html=True)
with right_column:
    st.empty()

 

  
         
