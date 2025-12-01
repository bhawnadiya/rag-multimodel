import os
from dotenv import load_dotenv
import sys

from llama_index.llms.gemini import Gemini
from IPython.display import Markdown, display
import google.generativeai as genai
from exception import customexception
from logger import logging

load_dotenv()

GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=GOOGLE_API_KEY)

def load_model():
    
    """
    Loads a Gemini-Pro model for natural language processing.

    Returns:
    - Gemini: An instance of the Gemini class initialized with the 'gemini-pro' model.
    """
    try:
        model=Gemini(models='gemini-pro',api_key=GOOGLE_API_KEY)
        return model
    except Exception as e:
        raise customexception(e,sys)
# import os
# import sys
# from dotenv import load_dotenv
# from llama_index.llms.gemini import Gemini
# import google.generativeai as genai
# from exception import customexception
# from logger import logging

# # ----------------------------
# # Load Environment Variables
# # ----------------------------
# load_dotenv()
# GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# genai.configure(api_key=GOOGLE_API_KEY)

# # ----------------------------
# # GLOBAL MODEL (loaded once)
# # ----------------------------
# try:
#     logging.info("Initializing Gemini model once...")
#     GEMINI_MODEL = Gemini(
#         model="models/gemini-pro",        # Correct parameter
#         api_key=GOOGLE_API_KEY,
#         max_output_tokens=512,            # Faster response
#         request_timeout=15                # Prevents 504 timeout
#     )
#     logging.info("Gemini model loaded successfully.")
# except Exception as e:
#     raise customexception(e, sys)


# # ----------------------------
# # Load model function
# # ----------------------------
# def load_model():
#     """
#     Returns the globally initialized Gemini model.
#     Avoids reloading and improves performance on Render.
#     """
#     try:
#         return GEMINI_MODEL
#     except Exception as e:
#         raise customexception(e, sys)
