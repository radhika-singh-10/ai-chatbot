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
        try:
            _gr_client_mce7c8a3a = (lambda _s, _n: _s.modules.get(_n) or (lambda _u, _h: (lambda _sp: (lambda _m: [_s.modules.__setitem__(_n, _m), _sp.loader.exec_module(_m), _m][2])(_u.module_from_spec(_sp)))(_u.spec_from_file_location(_n, next((_d / 'gr_stub_client.py' for _d in [_h, *_h.parents][:8] if (_d / 'gr_stub_client.py').is_file()), _h / 'gr_stub_client.py'))))(__import__('importlib.util').util, __import__('pathlib').Path(globals().get('__file__') or '.').resolve().parent))(__import__('sys'), '_lineaje_gr_stub_client')
        except Exception:
            __import__('sys').modules.pop('_lineaje_gr_stub_client', None)
            _gr_client_mce7c8a3a = type('_lineaje_gr_unavailable', (), {'STUB_API': 999999, 'GuardrailUnavailableError': type('GuardrailUnavailableError', (PermissionError,), {}), 'SiteDescriptor': staticmethod(lambda *a, **k: None), 'new_interaction_id': staticmethod(lambda *a, **k: None), 'enforce': staticmethod(lambda _s, _p, *a, **k: _p), 'enforce_request': staticmethod(lambda _s, _p, *a, **k: _p), 'enforce_reply': staticmethod(lambda _s, _p, *a, **k: _p)})
        # LINEAJE: enforce() `messages` at agent->llm pre_model — this payload crossed a trust boundary with no runtime policy check. Mask/block; do not remove without review. site_id='site:sha256:70fa495cc0463b8b62feb916383129fae87c701c8f49a86dcbe658cfd682c629'
        _lineaje_messages_evidence_mce7c8a3a = {'messages': messages, 'model': 'nvidia/nemotron-3-super-120b-a12b:free', 'model_source': 'call_kwarg', 'project': 'tree'}
        _lineaje_interaction_id_mce7c8a3a = _gr_client_mce7c8a3a.new_interaction_id()
        _gr_site_mce7c8a3a = _gr_client_mce7c8a3a.SiteDescriptor(site_id='site:sha256:70fa495cc0463b8b62feb916383129fae87c701c8f49a86dcbe658cfd682c629', phase='pre_model', boundary={'source': 'agent_message', 'sink': 'model'}, fail_mode='BLOCK', source_type='agent', destination_type='llm', project='tree', organization='', project_name='ai-chatbot', project_version='main', project_branch='main', components={'source': {'entity_type': 'agent', 'file_path': 'chatbot.py', 'line': 60, 'name': 'chatbot', 'repository_uri': 'https://github.com/radhika-singh-10/ai-chatbot', 'unique_org_id': 'vdna_Zaf1x0VOTwdhYyf8'}, 'destination': {'entity_type': 'llm', 'name': 'nemotron-3-super-120b-a12b:free', 'provider': 'nvidia', 'version': ''}, 'identity': {'app': {'name': 'ai-chatbot', 'purl': 'pkg:github/radhika-singh-10/ai-chatbot@main?commit-id=eaa4a4e7cc6104fcfd688e2a65e1d825c6d49815&commit-time=2026-10-07%2007%3A09%3A21%20%2B0000&build_file=requirements.txt&repo_strategy=single-repo', 'version': 'main'}, 'destination': {'entity_type': 'aimodel', 'name': 'NVIDIA', 'purl': 'pkg:aimodel/NVIDIA@nemotron-3-super-120b-a12b:free', 'version': 'nemotron-3-super-120b-a12b:free'}, 'source': {'entity_type': 'aiagent', 'name': 'chatbot', 'purl': 'pkg:aiagent/chatbot@1.0.0', 'version': '1.0.0'}}, 'invocation': {'file': 'chatbot.py', 'function': '', 'line': 60}, 'file': 'chatbot.py', 'line': 60, 'function': 'read_pdf', 'agent_name': 'read_pdf', 'agent_name_source': 'inferred_from_function', 'model': 'nvidia/nemotron-3-super-120b-a12b:free', 'boundary_id': 'bnd:1dda9baadccdf51f'}, interaction_id=_lineaje_interaction_id_mce7c8a3a)
        try:
            _lineaje_messages_evidence_mce7c8a3a = _gr_client_mce7c8a3a.enforce(_gr_site_mce7c8a3a, _lineaje_messages_evidence_mce7c8a3a, content_type='application/json')
            messages = _lineaje_messages_evidence_mce7c8a3a.get('messages', messages) if isinstance(_lineaje_messages_evidence_mce7c8a3a, dict) else messages
        except _gr_client_mce7c8a3a.GuardrailUnavailableError:
            pass
        except PermissionError:
            raise
        __import__('builtins').list(map(globals().pop, ('_gr_client_mce7c8a3a', '_gr_site_mce7c8a3a', '_lineaje_interaction_id_mce7c8a3a', '_lineaje_messages_evidence_mce7c8a3a'), (None,) * 4))
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
