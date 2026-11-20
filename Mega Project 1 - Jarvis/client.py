
# import os
# import time
# from google import genai

# api_key = os.getenv("GEMINI_API_KEY")

# if not api_key:
#     raise ValueError("Gemini API key not found!")

# client = genai.Client(api_key=api_key)

# for attempt in range(3):
#     try:
#         response = client.models.generate_content(
#             model="gemini-3.8-flash",
#             contents="Hello Gemini! Introduce yourself."
#         )

#         print("Gemini:", response.text)
#         break

#     except Exception as e:
#         if "503" in str(e) and attempt < 2:
#             print("Gemini is busy. Retrying in 10 seconds...")
#             time.sleep(10)
#         else:
#             print("Error:", e)
#             break
