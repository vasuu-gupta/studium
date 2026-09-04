import time
from google import genai

print("Starting...")

start = time.time()

client = genai.Client()

print("Sending request...")

response = client.interactions.create(
    model="gemini-3.6-flash",
    input="Say hello in one sentence."
)

print(f"Response received in {time.time() - start:.2f}s")
print(response.output_text)