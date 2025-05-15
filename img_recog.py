import requests
from PIL import Image
from io import BytesIO
import google.generativeai as genai

# Set up your API key for Gemini
genai.configure(api_key="YOUR_API_KEY")  

# Fetch image from the internet
img_link = "https://images5.alphacoders.com/133/1337263.png"
img_data = requests.get(img_link)
img_obj = Image.open(BytesIO(img_data.content))

# Reduce the image size to save token usage
img_resized = img_obj.resize((400, 400))

# Initialize the Gemini Pro model
gemini_model = genai.GenerativeModel("gemini-1.5-pro")

# Attempt to describe the image
try:
    result = gemini_model.generate_content([img_resized, "What do you see in this image?"])
    print("\nGemini AI Description:\n", result.text)

except Exception as err:
    print("\n⚠️ Unable to generate image description.")
    print("Error details:", err)
    print("Hint: Try reducing the image size further or wait before retrying.")
