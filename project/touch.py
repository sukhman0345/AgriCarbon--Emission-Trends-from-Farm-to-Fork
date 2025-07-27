import streamlit as st

def get_in_touch():
  
   st.markdown("""
        <div style='text-align: center'>
            <h1>Get In Touch!</h1>       
        </div>
      """, unsafe_allow_html=True)

   contact_form= """
    <form action="https://formsubmit.co/sukhmansinghcodes@gmail.com" method="POST">
      <input type="hidden" name="_captcha" value="false">
      <input type="text" name="name" placeholder="your name" required>
      <input type="email" name="email" placeholder="your email" required>
      <textarea name="message" placeholder="Write your query here"></textarea>
      <button type="submit">Send</button>
    </form>

  """ 
   st.markdown(contact_form, unsafe_allow_html=True) 

   #inject the css using local css
   def local_css(file_name):
      with open(file_name) as f:
         st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

   local_css("style/style.css")   