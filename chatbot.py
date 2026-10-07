import os
from dotenv import load_dotenv
from openai import OpenAI
from pypdf import PdfReader

# Load environment variables
load_dotenv()

# Create client
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

# Store conversation
messages = [
    {"role": "system", "content": "You are a helpful assistant. Users may upload PDF documents "
                                  "containing personal information (PII); use that content to answer their questions."}
]


def read_pdf(path):
    """Extract all text from a PDF file."""
    reader = PdfReader(path)
    return "\n".join(page.extract_text() or "" for page in reader.pages)


print("AI Chatbot started! Type 'upload <path-to-pdf>' to share a PDF, or 'quit' to stop.")

while True:
    user_input = input("You: ")

    if user_input.lower() in ["quit", "exit"]:
        print("Chat ended.")
        break

    # Upload a PDF and pass its contents (including any PII) to the LLM
    if user_input.lower().startswith("upload "):
        pdf_path = os.path.expanduser(user_input[len("upload "):].strip().strip('"\''))
        try:
            pdf_text = read_pdf(pdf_path)
        except Exception as e:
            print("Error reading PDF:", e)
            continue

        if not pdf_text.strip():
            print("No text could be extracted from the PDF (it may be scanned images).")
            continue

        print(f"Uploaded {os.path.basename(pdf_path)} ({len(pdf_text)} characters).")
        user_input = (
            f"Here is the content of the uploaded PDF '{os.path.basename(pdf_path)}', "
            f"including any personal information it contains:\n\n{pdf_text}\n\n"
            "Please summarize it and list the personal details (PII) it contains."
        )

    messages.append({"role": "user", "content": user_input})

    try:
        response = client.chat.completions.create(
            model="nvidia/nemotron-3-super-120b-a12b:free",
            messages=messages
        )

        reply = response.choices[0].message.content
        print("AI:", reply)

        messages.append({"role": "assistant", "content": reply})

    except Exception as e:
        print("Error:", e)
        # Drop the failed message so it isn't resent with the next turn
        messages.pop()
