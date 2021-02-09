import streamlit as st
import pandas as pd
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('I update automatically!')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

def run():
    st.title("Demo App")


if __name__ == "__main__":
    run()
