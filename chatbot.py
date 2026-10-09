# Copyright (c) Lineaje, Inc. All rights reserved.
# Lineaje UnifAI guardrail  version=2.0.0-alpha
def _lineaje_load_gr_client():
    """Lineaje-added: load gr_stub_client.py without a pip dependency."""
    import sys as _s, importlib.util as _ilu
    from pathlib import Path as _P
    n = "_lineaje_gr_stub_client"
    if n in _s.modules: return _s.modules[n]
    h = _P(__file__).resolve().parent
    _cand = next((d / "gr_stub_client.py" for d in [h, *h.parents][:8] if (d / "gr_stub_client.py").is_file()), h / "gr_stub_client.py")
    _spec = _ilu.spec_from_file_location(n, _cand)
    _s.modules[n] = _m = _ilu.module_from_spec(_spec)
    _spec.loader.exec_module(_m); return _m
def _lineaje_current_model():
    """Lineaje-added: reread the app's model setting for every request."""
    import os as _o
    from pathlib import Path as _P
    _keys = ("OPENROUTER_MODEL", "LLM_MODEL", "MODEL_NAME", "MODEL_ID", "OPENAI_MODEL", "ANTHROPIC_MODEL", "BEDROCK_MODEL_ID")
    _here = _P(__file__).resolve().parent
    for _path in (_here / ".env", *(_p / ".env" for _p in list(_here.parents)[:8])):
        if not _path.is_file(): continue
        try: _lines = _path.read_text(encoding="utf-8").splitlines()
        except OSError: continue
        _values = {}
        for _line in _lines:
            _line = _line.strip()
            if not _line or _line.startswith("#") or "=" not in _line: continue
            _key, _, _value = _line.partition("=")
            if _key.strip() in _keys: _values[_key.strip()] = _value.strip().strip(chr(34)).strip(chr(39))
        for _key in _keys:
            if _values.get(_key): return _values[_key]
    return next((_o.environ[_key].strip() for _key in _keys if _o.environ.get(_key, "").strip()), "")
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


_lineaje_payload = "AI Chatbot started! Type 'upload <path-to-pdf>' to share a PDF, or 'quit' to stop."
# LINEAJE: enforce() `_lineaje_payload` at agent->log log_emit — scan flagged AI_APP_SEC_006 (Use only LLMs from the organization's approved list.); AI_DAT_SEC_012 (Mask PII on user interfaces). Mask/block; do not remove without review. site_id='site:sha256:7dfac841572f29c147cf5db011703764fcf851fe06720588c1656c9e20b52fcf'
_gr_client = _lineaje_load_gr_client()
_gr_site = _gr_client.SiteDescriptor(site_id='site:sha256:7dfac841572f29c147cf5db011703764fcf851fe06720588c1656c9e20b52fcf', phase='log_emit', boundary={'source': 'log', 'sink': 'log'}, candidate_policies=[{'policy_id': 'AI_DAT_SEC_010', 'policy_name': 'Do not log PII.', 'guardrail_id': 'Mask PII in Logs', 'policy_version': '2026.08.1'}], fail_mode='BLOCK', source_type='agent', destination_type='log', project='', organization='Root Organization', project_name='ai-chatbot', project_version='demo-scan', project_branch='demo-scan', components={'source': {'entity_type': 'agent', 'unique_org_id': 'vdna_4GoFBTH8XS3rAjS3', 'repository_uri': 'https://github.com/radhika-singh-10/ai-chatbot', 'file_path': 'chatbot.py', 'line': 60, 'name': 'chatbot'}, 'identity': {'source': {'entity_type': 'aiagent', 'name': 'chatbot', 'version': '1.0.0', 'purl': 'pkg:aiagent/chatbot@1.0.0'}, 'app': {'name': 'ai-chatbot', 'version': 'demo-scan', 'purl': 'pkg:github/radhika-singh-10/ai-chatbot@demo-scan?commit-id=eaa4a4e7cc6104fcfd688e2a65e1d825c6d49815&commit-time=&build_file=requirements.txt&repo_strategy=single-repo'}}, 'invocation': {'file': 'chatbot.py', 'line': 28, 'function': ''}})
try:
    _lineaje_payload = _gr_client.enforce(_gr_site, _lineaje_payload, content_type='application/json')
except _gr_client.GuardrailUnavailableError:
    pass
except PermissionError:
    pass
# LINEAJE: enforce() `_lineaje_payload` at agent->log log_emit — scan flagged AI_APP_SEC_006 (Use only LLMs from the organization's approved list.). Mask/block; do not remove without review. site_id='site:sha256:e110087ae807f9b4d72e4cde32addc5049639eda1bba5df6eb23cce323e48337'
_gr_client = _lineaje_load_gr_client()
_gr_site = _gr_client.SiteDescriptor(site_id='site:sha256:e110087ae807f9b4d72e4cde32addc5049639eda1bba5df6eb23cce323e48337', phase='log_emit', boundary={'source': 'log', 'sink': 'log'}, candidate_policies=[{'policy_id': 'AI_DAT_SEC_010', 'policy_name': 'Do not log PII.', 'guardrail_id': 'Mask PII in Logs', 'policy_version': '2026.08.1'}], fail_mode='BLOCK', source_type='agent', destination_type='log', project='', organization='Root Organization', project_name='ai-chatbot', project_version='demo-scan', project_branch='demo-scan', components={'source': {'entity_type': 'agent', 'unique_org_id': 'vdna_4GoFBTH8XS3rAjS3', 'repository_uri': 'https://github.com/radhika-singh-10/ai-chatbot', 'file_path': 'chatbot.py', 'line': 170, 'name': 'chatbot'}, 'identity': {'source': {'entity_type': 'aiagent', 'name': 'chatbot', 'version': '1.0.0', 'purl': 'pkg:aiagent/chatbot@1.0.0'}, 'app': {'name': 'ai-chatbot', 'version': 'demo-scan', 'purl': 'pkg:github/radhika-singh-10/ai-chatbot@demo-scan?commit-id=eaa4a4e7cc6104fcfd688e2a65e1d825c6d49815&commit-time=2026-10-07%2007%3A09%3A21%20%2B0000&build_file=requirements.txt&repo_strategy=single-repo'}}, 'invocation': {'file': 'chatbot.py', 'line': 70, 'function': ''}})
try:
    _lineaje_payload = _gr_client.enforce(_gr_site, _lineaje_payload, content_type='application/json')
except _gr_client.GuardrailUnavailableError:
    pass
except PermissionError:
    pass
print(_lineaje_payload)

while True:
    user_input = input("You: ")

    if user_input.lower() in ["quit", "exit"]:
        _lineaje_payload = "Chat ended."
        # LINEAJE: enforce() `_lineaje_payload` at agent->log log_emit — scan flagged AI_APP_SEC_006 (Use only LLMs from the organization's approved list.); AI_DAT_SEC_012 (Mask PII on user interfaces). Mask/block; do not remove without review. site_id='site:sha256:a72da41e95204bc39209257371f9946776a0d2d29d96eceeee50efe86e3909c4'
        _gr_client = _lineaje_load_gr_client()
        _gr_site = _gr_client.SiteDescriptor(site_id='site:sha256:a72da41e95204bc39209257371f9946776a0d2d29d96eceeee50efe86e3909c4', phase='log_emit', boundary={'source': 'log', 'sink': 'log'}, candidate_policies=[{'policy_id': 'AI_DAT_SEC_010', 'policy_name': 'Do not log PII.', 'guardrail_id': 'Mask PII in Logs', 'policy_version': '2026.08.1'}], fail_mode='BLOCK', source_type='agent', destination_type='log', project='', organization='Root Organization', project_name='ai-chatbot', project_version='demo-scan', project_branch='demo-scan', components={'source': {'entity_type': 'agent', 'unique_org_id': 'vdna_4GoFBTH8XS3rAjS3', 'repository_uri': 'https://github.com/radhika-singh-10/ai-chatbot', 'file_path': 'chatbot.py', 'line': 60, 'name': 'chatbot'}, 'identity': {'source': {'entity_type': 'aiagent', 'name': 'chatbot', 'version': '1.0.0', 'purl': 'pkg:aiagent/chatbot@1.0.0'}, 'app': {'name': 'ai-chatbot', 'version': 'demo-scan', 'purl': 'pkg:github/radhika-singh-10/ai-chatbot@demo-scan?commit-id=eaa4a4e7cc6104fcfd688e2a65e1d825c6d49815&commit-time=&build_file=requirements.txt&repo_strategy=single-repo'}}, 'invocation': {'file': 'chatbot.py', 'line': 34, 'function': ''}})
        try:
            _lineaje_payload = _gr_client.enforce(_gr_site, _lineaje_payload, content_type='application/json')
        except _gr_client.GuardrailUnavailableError:
            pass
        except PermissionError:
            pass
        print(_lineaje_payload)
        break

    # Upload a PDF and pass its contents (including any PII) to the LLM
    if user_input.lower().startswith("upload "):
        pdf_path = os.path.expanduser(user_input[len("upload "):].strip().strip('"\''))
        try:
            pdf_text = read_pdf(pdf_path)
        except Exception as e:
            # LINEAJE: enforce() `e` at agent->log log_emit — scan flagged AI_APP_SEC_006 (Use only LLMs from the organization's approved list.); AI_DAT_SEC_012 (Mask PII on user interfaces). Mask/block; do not remove without review. site_id='site:sha256:c8efd315656a0577efbfe1b45dc1925e8cf5ceca6b851a1393803b5823a0e2cf'
            _gr_client = _lineaje_load_gr_client()
            _gr_site = _gr_client.SiteDescriptor(site_id='site:sha256:c8efd315656a0577efbfe1b45dc1925e8cf5ceca6b851a1393803b5823a0e2cf', phase='log_emit', boundary={'source': 'log', 'sink': 'log'}, candidate_policies=[{'policy_id': 'AI_DAT_SEC_010', 'policy_name': 'Do not log PII.', 'guardrail_id': 'Mask PII in Logs', 'policy_version': '2026.08.1'}], fail_mode='BLOCK', source_type='agent', destination_type='log', project='', organization='Root Organization', project_name='ai-chatbot', project_version='demo-scan', project_branch='demo-scan', components={'source': {'entity_type': 'agent', 'unique_org_id': 'vdna_4GoFBTH8XS3rAjS3', 'repository_uri': 'https://github.com/radhika-singh-10/ai-chatbot', 'file_path': 'chatbot.py', 'line': 60, 'name': 'chatbot'}, 'identity': {'source': {'entity_type': 'aiagent', 'name': 'chatbot', 'version': '1.0.0', 'purl': 'pkg:aiagent/chatbot@1.0.0'}, 'app': {'name': 'ai-chatbot', 'version': 'demo-scan', 'purl': 'pkg:github/radhika-singh-10/ai-chatbot@demo-scan?commit-id=eaa4a4e7cc6104fcfd688e2a65e1d825c6d49815&commit-time=&build_file=requirements.txt&repo_strategy=single-repo'}}, 'invocation': {'file': 'chatbot.py', 'line': 43, 'function': ''}})
            try:
                e = _gr_client.enforce(_gr_site, e, content_type='application/json')
            except _gr_client.GuardrailUnavailableError:
                pass
            except PermissionError:
                pass
            # LINEAJE: enforce() `e` at agent->log log_emit — scan flagged AI_APP_SEC_006 (Use only LLMs from the organization's approved list.). Mask/block; do not remove without review. site_id='site:sha256:f7107403be65bc262ef595d81f407bba1d1ae98a555da76e7151bc73ca781d63'
            _gr_client = _lineaje_load_gr_client()
            _gr_site = _gr_client.SiteDescriptor(site_id='site:sha256:f7107403be65bc262ef595d81f407bba1d1ae98a555da76e7151bc73ca781d63', phase='log_emit', boundary={'source': 'log', 'sink': 'log'}, candidate_policies=[{'policy_id': 'AI_DAT_SEC_010', 'policy_name': 'Do not log PII.', 'guardrail_id': 'Mask PII in Logs', 'policy_version': '2026.08.1'}], fail_mode='BLOCK', source_type='agent', destination_type='log', project='', organization='Root Organization', project_name='ai-chatbot', project_version='demo-scan', project_branch='demo-scan', components={'source': {'entity_type': 'agent', 'unique_org_id': 'vdna_4GoFBTH8XS3rAjS3', 'repository_uri': 'https://github.com/radhika-singh-10/ai-chatbot', 'file_path': 'chatbot.py', 'line': 153, 'name': 'chatbot'}, 'identity': {'source': {'entity_type': 'aiagent', 'name': 'chatbot', 'version': '1.0.0', 'purl': 'pkg:aiagent/chatbot@1.0.0'}, 'app': {'name': 'ai-chatbot', 'version': 'demo-scan', 'purl': 'pkg:github/radhika-singh-10/ai-chatbot@demo-scan?commit-id=eaa4a4e7cc6104fcfd688e2a65e1d825c6d49815&commit-time=&build_file=requirements.txt&repo_strategy=single-repo'}}, 'invocation': {'file': 'chatbot.py', 'line': 105, 'function': ''}})
            try:
                e = _gr_client.enforce(_gr_site, e, content_type='application/json')
            except _gr_client.GuardrailUnavailableError:
                pass
            except PermissionError:
                pass
            print("Error reading PDF:", e)
            continue

        if not pdf_text.strip():
            _lineaje_payload = "No text could be extracted from the PDF (it may be scanned images)."
            # LINEAJE: enforce() `_lineaje_payload` at agent->log log_emit — scan flagged AI_APP_SEC_006 (Use only LLMs from the organization's approved list.); AI_DAT_SEC_012 (Mask PII on user interfaces). Mask/block; do not remove without review. site_id='site:sha256:6eb6961c74d7529817bbf771bbc7baa50e4a4bdc10f3095a6ad3a6d0ca1f8da3'
            _gr_client = _lineaje_load_gr_client()
            _gr_site = _gr_client.SiteDescriptor(site_id='site:sha256:6eb6961c74d7529817bbf771bbc7baa50e4a4bdc10f3095a6ad3a6d0ca1f8da3', phase='log_emit', boundary={'source': 'log', 'sink': 'log'}, candidate_policies=[{'policy_id': 'AI_DAT_SEC_010', 'policy_name': 'Do not log PII.', 'guardrail_id': 'Mask PII in Logs', 'policy_version': '2026.08.1'}], fail_mode='BLOCK', source_type='agent', destination_type='log', project='', organization='Root Organization', project_name='ai-chatbot', project_version='demo-scan', project_branch='demo-scan', components={'source': {'entity_type': 'agent', 'unique_org_id': 'vdna_4GoFBTH8XS3rAjS3', 'repository_uri': 'https://github.com/radhika-singh-10/ai-chatbot', 'file_path': 'chatbot.py', 'line': 60, 'name': 'chatbot'}, 'identity': {'source': {'entity_type': 'aiagent', 'name': 'chatbot', 'version': '1.0.0', 'purl': 'pkg:aiagent/chatbot@1.0.0'}, 'app': {'name': 'ai-chatbot', 'version': 'demo-scan', 'purl': 'pkg:github/radhika-singh-10/ai-chatbot@demo-scan?commit-id=eaa4a4e7cc6104fcfd688e2a65e1d825c6d49815&commit-time=&build_file=requirements.txt&repo_strategy=single-repo'}}, 'invocation': {'file': 'chatbot.py', 'line': 47, 'function': ''}})
            try:
                _lineaje_payload = _gr_client.enforce(_gr_site, _lineaje_payload, content_type='application/json')
            except _gr_client.GuardrailUnavailableError:
                pass
            except PermissionError:
                pass
            print(_lineaje_payload)
            continue

        _lineaje_payload = f"Uploaded {os.path.basename(pdf_path)} ({len(pdf_text)} characters)."
        # LINEAJE: enforce() `_lineaje_payload` at agent->log log_emit — scan flagged AI_APP_SEC_006 (Use only LLMs from the organization's approved list.); AI_DAT_SEC_012 (Mask PII on user interfaces). Mask/block; do not remove without review. site_id='site:sha256:db76f3b309e0335991b24d2e4077a728f686d4fe088eebcea8c1276f6f1d7497'
        _gr_client = _lineaje_load_gr_client()
        _gr_site = _gr_client.SiteDescriptor(site_id='site:sha256:db76f3b309e0335991b24d2e4077a728f686d4fe088eebcea8c1276f6f1d7497', phase='log_emit', boundary={'source': 'log', 'sink': 'log'}, candidate_policies=[{'policy_id': 'AI_DAT_SEC_010', 'policy_name': 'Do not log PII.', 'guardrail_id': 'Mask PII in Logs', 'policy_version': '2026.08.1'}], fail_mode='BLOCK', source_type='agent', destination_type='log', project='', organization='Root Organization', project_name='ai-chatbot', project_version='demo-scan', project_branch='demo-scan', components={'source': {'entity_type': 'agent', 'unique_org_id': 'vdna_4GoFBTH8XS3rAjS3', 'repository_uri': 'https://github.com/radhika-singh-10/ai-chatbot', 'file_path': 'chatbot.py', 'line': 60, 'name': 'chatbot'}, 'identity': {'source': {'entity_type': 'aiagent', 'name': 'chatbot', 'version': '1.0.0', 'purl': 'pkg:aiagent/chatbot@1.0.0'}, 'app': {'name': 'ai-chatbot', 'version': 'demo-scan', 'purl': 'pkg:github/radhika-singh-10/ai-chatbot@demo-scan?commit-id=eaa4a4e7cc6104fcfd688e2a65e1d825c6d49815&commit-time=&build_file=requirements.txt&repo_strategy=single-repo'}}, 'invocation': {'file': 'chatbot.py', 'line': 50, 'function': ''}})
        try:
            _lineaje_payload = _gr_client.enforce(_gr_site, _lineaje_payload, content_type='application/json')
        except _gr_client.GuardrailUnavailableError:
            pass
        except PermissionError:
            pass
        # LINEAJE: enforce() `_lineaje_payload` at agent->log log_emit — scan flagged AI_APP_SEC_006 (Use only LLMs from the organization's approved list.). Mask/block; do not remove without review. site_id='site:sha256:4088209114d861004476ea8679b7216233b601e6ae60cf669c3e622a19a92725'
        _gr_client = _lineaje_load_gr_client()
        _gr_site = _gr_client.SiteDescriptor(site_id='site:sha256:4088209114d861004476ea8679b7216233b601e6ae60cf669c3e622a19a92725', phase='log_emit', boundary={'source': 'log', 'sink': 'log'}, candidate_policies=[{'policy_id': 'AI_DAT_SEC_010', 'policy_name': 'Do not log PII.', 'guardrail_id': 'Mask PII in Logs', 'policy_version': '2026.08.1'}], fail_mode='BLOCK', source_type='agent', destination_type='log', project='', organization='Root Organization', project_name='ai-chatbot', project_version='demo-scan', project_branch='demo-scan', components={'source': {'entity_type': 'agent', 'unique_org_id': 'vdna_4GoFBTH8XS3rAjS3', 'repository_uri': 'https://github.com/radhika-singh-10/ai-chatbot', 'file_path': 'chatbot.py', 'line': 153, 'name': 'chatbot'}, 'identity': {'source': {'entity_type': 'aiagent', 'name': 'chatbot', 'version': '1.0.0', 'purl': 'pkg:aiagent/chatbot@1.0.0'}, 'app': {'name': 'ai-chatbot', 'version': 'demo-scan', 'purl': 'pkg:github/radhika-singh-10/ai-chatbot@demo-scan?commit-id=eaa4a4e7cc6104fcfd688e2a65e1d825c6d49815&commit-time=&build_file=requirements.txt&repo_strategy=single-repo'}}, 'invocation': {'file': 'chatbot.py', 'line': 132, 'function': ''}})
        try:
            _lineaje_payload = _gr_client.enforce(_gr_site, _lineaje_payload, content_type='application/json')
        except _gr_client.GuardrailUnavailableError:
            pass
        except PermissionError:
            pass
        print(_lineaje_payload)
        user_input = (
            f"Here is the content of the uploaded PDF '{os.path.basename(pdf_path)}', "
            f"including any personal information it contains:\n\n{pdf_text}\n\n"
            "Please summarize it and list the personal details (PII) it contains."
        )

    messages.append({"role": "user", "content": user_input})

    try:
        # LINEAJE: enforce() `messages` at agent->llm pre_model — scan flagged AI_APP_SEC_006 (Use only LLMs from the organization's approved list.); AI_DAT_SEC_012 (Mask PII on user interfaces). Mask/block; do not remove without review. site_id='site:sha256:70fa495cc0463b8b62feb916383129fae87c701c8f49a86dcbe658cfd682c629'
        _lineaje_messages_evidence = {'messages': messages, 'model': 'nvidia/nemotron-3-super-120b-a12b:free'}
        _gr_client = _lineaje_load_gr_client()
        _gr_site = _gr_client.SiteDescriptor(site_id='site:sha256:70fa495cc0463b8b62feb916383129fae87c701c8f49a86dcbe658cfd682c629', phase='pre_model', boundary={'source': 'agent_message', 'sink': 'model'}, candidate_policies=[{'policy_id': 'AI_APP_SEC_006', 'policy_name': "Use only LLMs from the organization's approved list.", 'guardrail_id': 'Enforce Approved LLM.', 'policy_version': '2026.08.1'}, {'policy_id': 'AI_APP_SEC_028', 'policy_name': "Do not use LLMs from the organization's disallowed list", 'guardrail_id': 'Enforce Approved LLM', 'policy_version': '2026.08.1'}, {'policy_id': 'AI_APP_SEC_070', 'policy_name': 'Detect and block all forms of prompt injection attacks in user inputs and file contents', 'guardrail_id': 'Sanitize Prompt Injection', 'policy_version': '2026.08.1'}, {'policy_id': 'AI_DAT_SEC_011', 'policy_name': 'Do not send PII and/or secrets to AI Models', 'guardrail_id': 'Redact PII', 'policy_version': '2026.08.1'}, {'policy_id': 'AI_DAT_SEC_029', 'policy_name': 'Enforce decision logging, audit trail, and forensic readiness for AI-driven actions.', 'guardrail_id': 'Emit immutable, forensic-ready audit records for all AI decisions.', 'policy_version': '2026.08.1'}], fail_mode='BLOCK', source_type='agent', destination_type='llm', project='', organization='Root Organization', project_name='ai-chatbot', project_version='demo-scan', project_branch='demo-scan', components={'source': {'entity_type': 'agent', 'unique_org_id': 'vdna_4GoFBTH8XS3rAjS3', 'repository_uri': 'https://github.com/radhika-singh-10/ai-chatbot', 'file_path': 'chatbot.py', 'line': 60, 'name': 'chatbot'}, 'destination': {'entity_type': 'llm', 'name': 'nemotron-3-super-120b-a12b:free', 'version': '', 'provider': 'nvidia'}, 'identity': {'source': {'entity_type': 'aiagent', 'name': 'chatbot', 'version': '1.0.0', 'purl': 'pkg:aiagent/chatbot@1.0.0'}, 'app': {'name': 'ai-chatbot', 'version': 'demo-scan', 'purl': 'pkg:github/radhika-singh-10/ai-chatbot@demo-scan?commit-id=eaa4a4e7cc6104fcfd688e2a65e1d825c6d49815&commit-time=&build_file=requirements.txt&repo_strategy=single-repo'}, 'destination': {'entity_type': 'aimodel', 'name': 'NVIDIA', 'version': 'nemotron-3-super-120b-a12b:free', 'purl': 'pkg:aimodel/NVIDIA@nemotron-3-super-120b-a12b:free'}}, 'invocation': {'file': 'chatbot.py', 'line': 60, 'function': ''}})
        try:
            _lineaje_messages_evidence = _gr_client.enforce(_gr_site, _lineaje_messages_evidence, content_type='application/json')
            messages = _lineaje_messages_evidence.get('messages', messages) if isinstance(_lineaje_messages_evidence, dict) else messages
        except _gr_client.GuardrailUnavailableError:
            pass
        except PermissionError:
            raise
        response = client.chat.completions.create(
            model="nvidia/nemotron-3-super-120b-a12b:free",
            messages=messages
        )

        reply = response.choices[0].message.content
        # LINEAJE: enforce() `reply` at llm->agent post_model — scan flagged AI_APP_SEC_006 (Use only LLMs from the organization's approved list.); AI_DAT_SEC_012 (Mask PII on user interfaces). Mask/block; do not remove without review. site_id='site:sha256:55171778fd7c3720ec8dd579051eab96945d861c81a1eef12fc5071179f7dd80'
        _gr_client = _lineaje_load_gr_client()
        _gr_site = _gr_client.SiteDescriptor(site_id='site:sha256:55171778fd7c3720ec8dd579051eab96945d861c81a1eef12fc5071179f7dd80', phase='post_model', boundary={'source': 'model', 'sink': 'agent_message'}, candidate_policies=[{'policy_id': 'AI_DAT_SEC_029', 'policy_name': 'Enforce decision logging, audit trail, and forensic readiness for AI-driven actions.', 'guardrail_id': 'Emit immutable, forensic-ready audit records for all AI decisions.', 'policy_version': '2026.08.1'}], fail_mode='BLOCK', source_type='llm', destination_type='agent', project='', organization='Root Organization', project_name='ai-chatbot', project_version='demo-scan', project_branch='demo-scan', components={'source': {'entity_type': 'agent', 'unique_org_id': 'vdna_4GoFBTH8XS3rAjS3', 'repository_uri': 'https://github.com/radhika-singh-10/ai-chatbot', 'file_path': 'chatbot.py', 'line': 60, 'name': 'chatbot'}, 'destination': {'entity_type': 'llm', 'name': 'nemotron-3-super-120b-a12b:free', 'version': '', 'provider': 'nvidia'}, 'identity': {'source': {'entity_type': 'aiagent', 'name': 'chatbot', 'version': '1.0.0', 'purl': 'pkg:aiagent/chatbot@1.0.0'}, 'app': {'name': 'ai-chatbot', 'version': 'demo-scan', 'purl': 'pkg:github/radhika-singh-10/ai-chatbot@demo-scan?commit-id=eaa4a4e7cc6104fcfd688e2a65e1d825c6d49815&commit-time=&build_file=requirements.txt&repo_strategy=single-repo'}, 'destination': {'entity_type': 'aimodel', 'name': 'NVIDIA', 'version': 'nemotron-3-super-120b-a12b:free', 'purl': 'pkg:aimodel/NVIDIA@nemotron-3-super-120b-a12b:free'}}, 'invocation': {'file': 'chatbot.py', 'line': 65, 'function': ''}})
        try:
            reply = _gr_client.enforce(_gr_site, reply, content_type='application/json', variable_name='reply', source_file=__file__, before_line=65)
        except _gr_client.GuardrailUnavailableError:
            pass
        # LINEAJE: enforce() `reply` at agent->log log_emit — scan flagged AI_DAT_SEC_012 (Mask PII on user interfaces). Mask/block; do not remove without review. site_id='site:sha256:92d8253ac759515ce78d4de6f42f045c10c5040575bb20275ba4a5a4a9ffbe04'
        _gr_client = _lineaje_load_gr_client()
        _gr_site = _gr_client.SiteDescriptor(site_id='site:sha256:92d8253ac759515ce78d4de6f42f045c10c5040575bb20275ba4a5a4a9ffbe04', phase='log_emit', boundary={'source': 'log', 'sink': 'log'}, candidate_policies=[{'policy_id': 'AI_DAT_SEC_010', 'policy_name': 'Do not log PII.', 'guardrail_id': 'Mask PII in Logs', 'policy_version': '2026.08.1'}], fail_mode='BLOCK', source_type='agent', destination_type='log', project='', organization='Root Organization', project_name='ai-chatbot', project_version='demo-scan', project_branch='demo-scan', components={'source': {'entity_type': 'agent', 'unique_org_id': 'vdna_4GoFBTH8XS3rAjS3', 'repository_uri': 'https://github.com/radhika-singh-10/ai-chatbot', 'file_path': 'chatbot.py', 'line': 60, 'name': 'chatbot'}, 'identity': {'source': {'entity_type': 'aiagent', 'name': 'chatbot', 'version': '1.0.0', 'purl': 'pkg:aiagent/chatbot@1.0.0'}, 'app': {'name': 'ai-chatbot', 'version': 'demo-scan', 'purl': 'pkg:github/radhika-singh-10/ai-chatbot@demo-scan?commit-id=eaa4a4e7cc6104fcfd688e2a65e1d825c6d49815&commit-time=&build_file=requirements.txt&repo_strategy=single-repo'}}, 'invocation': {'file': 'chatbot.py', 'line': 66, 'function': ''}})
        try:
            reply = _gr_client.enforce(_gr_site, reply, content_type='application/json')
        except _gr_client.GuardrailUnavailableError:
            pass
        except PermissionError:
            pass
        # LINEAJE: enforce() `reply` at agent->log log_emit — scan flagged AI_APP_SEC_006 (Use only LLMs from the organization's approved list.). Mask/block; do not remove without review. site_id='site:sha256:03e7baf9f2847ca802edc43975288dad8d5b5472dd28aff2253716570c9b37fa'
        _gr_client = _lineaje_load_gr_client()
        _gr_site = _gr_client.SiteDescriptor(site_id='site:sha256:03e7baf9f2847ca802edc43975288dad8d5b5472dd28aff2253716570c9b37fa', phase='log_emit', boundary={'source': 'log', 'sink': 'log'}, candidate_policies=[{'policy_id': 'AI_DAT_SEC_010', 'policy_name': 'Do not log PII.', 'guardrail_id': 'Mask PII in Logs', 'policy_version': '2026.08.1'}], fail_mode='BLOCK', source_type='agent', destination_type='log', project='', organization='Root Organization', project_name='ai-chatbot', project_version='demo-scan', project_branch='demo-scan', components={'source': {'entity_type': 'agent', 'unique_org_id': 'vdna_4GoFBTH8XS3rAjS3', 'repository_uri': 'https://github.com/radhika-singh-10/ai-chatbot', 'file_path': 'chatbot.py', 'line': 153, 'name': 'chatbot'}, 'identity': {'source': {'entity_type': 'aiagent', 'name': 'chatbot', 'version': '1.0.0', 'purl': 'pkg:aiagent/chatbot@1.0.0'}, 'app': {'name': 'ai-chatbot', 'version': 'demo-scan', 'purl': 'pkg:github/radhika-singh-10/ai-chatbot@demo-scan?commit-id=eaa4a4e7cc6104fcfd688e2a65e1d825c6d49815&commit-time=&build_file=requirements.txt&repo_strategy=single-repo'}}, 'invocation': {'file': 'chatbot.py', 'line': 175, 'function': ''}})
        try:
            reply = _gr_client.enforce(_gr_site, reply, content_type='application/json')
        except _gr_client.GuardrailUnavailableError:
            pass
        except PermissionError:
            pass
        # LINEAJE: enforce() `reply` at agent->log log_emit — scan flagged AI_APP_SEC_006 (Use only LLMs from the organization's approved list.). Mask/block; do not remove without review. site_id='site:sha256:bd2bd02f43ffd80d38c753ad893724825b5e08557e5e87b4e6da6a8531ea893a'
        _gr_client = _lineaje_load_gr_client()
        _gr_site = _gr_client.SiteDescriptor(site_id='site:sha256:bd2bd02f43ffd80d38c753ad893724825b5e08557e5e87b4e6da6a8531ea893a', phase='log_emit', boundary={'source': 'log', 'sink': 'log'}, candidate_policies=[{'policy_id': 'AI_DAT_SEC_010', 'policy_name': 'Do not log PII.', 'guardrail_id': 'Mask PII in Logs', 'policy_version': '2026.08.1'}], fail_mode='BLOCK', source_type='agent', destination_type='log', project='', organization='Root Organization', project_name='ai-chatbot', project_version='demo-scan', project_branch='demo-scan', components={'source': {'entity_type': 'agent', 'unique_org_id': 'vdna_4GoFBTH8XS3rAjS3', 'repository_uri': 'https://github.com/radhika-singh-10/ai-chatbot', 'file_path': 'chatbot.py', 'line': 170, 'name': 'chatbot'}, 'identity': {'source': {'entity_type': 'aiagent', 'name': 'chatbot', 'version': '1.0.0', 'purl': 'pkg:aiagent/chatbot@1.0.0'}, 'app': {'name': 'ai-chatbot', 'version': 'demo-scan', 'purl': 'pkg:github/radhika-singh-10/ai-chatbot@demo-scan?commit-id=eaa4a4e7cc6104fcfd688e2a65e1d825c6d49815&commit-time=2026-10-07%2007%3A09%3A21%20%2B0000&build_file=requirements.txt&repo_strategy=single-repo'}}, 'invocation': {'file': 'chatbot.py', 'line': 201, 'function': ''}})
        try:
            reply = _gr_client.enforce(_gr_site, reply, content_type='application/json')
        except _gr_client.GuardrailUnavailableError:
            pass
        except PermissionError:
            pass
        print("AI:", reply)

        messages.append({"role": "assistant", "content": reply})

    except Exception as e:
        # LINEAJE: enforce() `e` at agent->log log_emit — scan flagged AI_APP_SEC_006 (Use only LLMs from the organization's approved list.); AI_DAT_SEC_012 (Mask PII on user interfaces). Mask/block; do not remove without review. site_id='site:sha256:e6cbb831a6a326f951022cb83bc6cc42f4eca4dcaaff906f6a7c19273d8d35b7'
        _gr_client = _lineaje_load_gr_client()
        _gr_site = _gr_client.SiteDescriptor(site_id='site:sha256:e6cbb831a6a326f951022cb83bc6cc42f4eca4dcaaff906f6a7c19273d8d35b7', phase='log_emit', boundary={'source': 'log', 'sink': 'log'}, candidate_policies=[{'policy_id': 'AI_DAT_SEC_010', 'policy_name': 'Do not log PII.', 'guardrail_id': 'Mask PII in Logs', 'policy_version': '2026.08.1'}], fail_mode='BLOCK', source_type='agent', destination_type='log', project='', organization='Root Organization', project_name='ai-chatbot', project_version='demo-scan', project_branch='demo-scan', components={'source': {'entity_type': 'agent', 'unique_org_id': 'vdna_4GoFBTH8XS3rAjS3', 'repository_uri': 'https://github.com/radhika-singh-10/ai-chatbot', 'file_path': 'chatbot.py', 'line': 60, 'name': 'chatbot'}, 'identity': {'source': {'entity_type': 'aiagent', 'name': 'chatbot', 'version': '1.0.0', 'purl': 'pkg:aiagent/chatbot@1.0.0'}, 'app': {'name': 'ai-chatbot', 'version': 'demo-scan', 'purl': 'pkg:github/radhika-singh-10/ai-chatbot@demo-scan?commit-id=eaa4a4e7cc6104fcfd688e2a65e1d825c6d49815&commit-time=&build_file=requirements.txt&repo_strategy=single-repo'}}, 'invocation': {'file': 'chatbot.py', 'line': 71, 'function': ''}})
        try:
            e = _gr_client.enforce(_gr_site, e, content_type='application/json')
        except _gr_client.GuardrailUnavailableError:
            pass
        except PermissionError:
            pass
        # LINEAJE: enforce() `e` at agent->log log_emit — scan flagged AI_APP_SEC_006 (Use only LLMs from the organization's approved list.). Mask/block; do not remove without review. site_id='site:sha256:5d7dea8f45d7e2c09851c67da532dc6bf510567957002be56a118fc75c9a3b74'
        _gr_client = _lineaje_load_gr_client()
        _gr_site = _gr_client.SiteDescriptor(site_id='site:sha256:5d7dea8f45d7e2c09851c67da532dc6bf510567957002be56a118fc75c9a3b74', phase='log_emit', boundary={'source': 'log', 'sink': 'log'}, candidate_policies=[{'policy_id': 'AI_DAT_SEC_010', 'policy_name': 'Do not log PII.', 'guardrail_id': 'Mask PII in Logs', 'policy_version': '2026.08.1'}], fail_mode='BLOCK', source_type='agent', destination_type='log', project='', organization='Root Organization', project_name='ai-chatbot', project_version='demo-scan', project_branch='demo-scan', components={'source': {'entity_type': 'agent', 'unique_org_id': 'vdna_4GoFBTH8XS3rAjS3', 'repository_uri': 'https://github.com/radhika-singh-10/ai-chatbot', 'file_path': 'chatbot.py', 'line': 153, 'name': 'chatbot'}, 'identity': {'source': {'entity_type': 'aiagent', 'name': 'chatbot', 'version': '1.0.0', 'purl': 'pkg:aiagent/chatbot@1.0.0'}, 'app': {'name': 'ai-chatbot', 'version': 'demo-scan', 'purl': 'pkg:github/radhika-singh-10/ai-chatbot@demo-scan?commit-id=eaa4a4e7cc6104fcfd688e2a65e1d825c6d49815&commit-time=&build_file=requirements.txt&repo_strategy=single-repo'}}, 'invocation': {'file': 'chatbot.py', 'line': 189, 'function': ''}})
        try:
            e = _gr_client.enforce(_gr_site, e, content_type='application/json')
        except _gr_client.GuardrailUnavailableError:
            pass
        except PermissionError:
            pass
        # LINEAJE: enforce() `e` at agent->log log_emit — scan flagged AI_APP_SEC_006 (Use only LLMs from the organization's approved list.). Mask/block; do not remove without review. site_id='site:sha256:85f3ce6a5755ab07b7453a5c857bae95b31ff68a5111efe4cf752c98fe72c9bd'
        _gr_client = _lineaje_load_gr_client()
        _gr_site = _gr_client.SiteDescriptor(site_id='site:sha256:85f3ce6a5755ab07b7453a5c857bae95b31ff68a5111efe4cf752c98fe72c9bd', phase='log_emit', boundary={'source': 'log', 'sink': 'log'}, candidate_policies=[{'policy_id': 'AI_DAT_SEC_010', 'policy_name': 'Do not log PII.', 'guardrail_id': 'Mask PII in Logs', 'policy_version': '2026.08.1'}], fail_mode='BLOCK', source_type='agent', destination_type='log', project='', organization='Root Organization', project_name='ai-chatbot', project_version='demo-scan', project_branch='demo-scan', components={'source': {'entity_type': 'agent', 'unique_org_id': 'vdna_4GoFBTH8XS3rAjS3', 'repository_uri': 'https://github.com/radhika-singh-10/ai-chatbot', 'file_path': 'chatbot.py', 'line': 170, 'name': 'chatbot'}, 'identity': {'source': {'entity_type': 'aiagent', 'name': 'chatbot', 'version': '1.0.0', 'purl': 'pkg:aiagent/chatbot@1.0.0'}, 'app': {'name': 'ai-chatbot', 'version': 'demo-scan', 'purl': 'pkg:github/radhika-singh-10/ai-chatbot@demo-scan?commit-id=eaa4a4e7cc6104fcfd688e2a65e1d825c6d49815&commit-time=2026-10-07%2007%3A09%3A21%20%2B0000&build_file=requirements.txt&repo_strategy=single-repo'}}, 'invocation': {'file': 'chatbot.py', 'line': 224, 'function': ''}})
        try:
            e = _gr_client.enforce(_gr_site, e, content_type='application/json')
        except _gr_client.GuardrailUnavailableError:
            pass
        except PermissionError:
            pass
        print("Error:", e)
        # Drop the failed message so it isn't resent with the next turn
        messages.pop()
