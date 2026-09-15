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

import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

# Create client
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

# Store conversation
messages = [
    {"role": "system", "content": "You are a helpful assistant."}
]

_lineaje_payload = "AI Chatbot started! Type 'quit' to stop."
# LINEAJE: enforce() `_lineaje_payload` at agent->log log_emit — scan flagged AI_APP_SEC_006 (Use only LLMs from the organization's approved list.); AI_APP_SEC_023 (Client must validate and sanitize any output from a MCP server); AI_APP_SEC_028 (Do not use LLMs from the organization's disallowed list). Mask/block; do not remove without review. site_id='site:sha256:ed624d7387b012c7fb9cd362810981cf06f0368728f7f1f39af7a066293107f4'
_gr_client = _lineaje_load_gr_client()
_gr_site = _gr_client.SiteDescriptor(site_id='site:sha256:ed624d7387b012c7fb9cd362810981cf06f0368728f7f1f39af7a066293107f4', phase='log_emit', boundary={'source': 'log', 'sink': 'log'}, candidate_policies=[{'policy_id': 'AI_DAT_SEC_010', 'guardrail_id': 'Mask PII in Logs', 'policy_version': '2026.08.1'}], fail_mode='BLOCK', source_type='agent', destination_type='log')
_lineaje_payload = _gr_client.enforce(_gr_site, _lineaje_payload, content_type='application/json')
print(_lineaje_payload)

while True:
    user_input = input("You: ")

    if user_input.lower() in ["quit", "exit"]:
        _lineaje_payload = "Chat ended."
        # LINEAJE: enforce() `_lineaje_payload` at agent->log log_emit — scan flagged AI_APP_SEC_006 (Use only LLMs from the organization's approved list.); AI_APP_SEC_023 (Client must validate and sanitize any output from a MCP server); AI_APP_SEC_028 (Do not use LLMs from the organization's disallowed list). Mask/block; do not remove without review. site_id='site:sha256:a72da41e95204bc39209257371f9946776a0d2d29d96eceeee50efe86e3909c4'
        _gr_client = _lineaje_load_gr_client()
        _gr_site = _gr_client.SiteDescriptor(site_id='site:sha256:a72da41e95204bc39209257371f9946776a0d2d29d96eceeee50efe86e3909c4', phase='log_emit', boundary={'source': 'log', 'sink': 'log'}, candidate_policies=[{'policy_id': 'AI_DAT_SEC_010', 'guardrail_id': 'Mask PII in Logs', 'policy_version': '2026.08.1'}], fail_mode='BLOCK', source_type='agent', destination_type='log')
        _lineaje_payload = _gr_client.enforce(_gr_site, _lineaje_payload, content_type='application/json')
        print(_lineaje_payload)
        break

    messages.append({"role": "user", "content": user_input})

    try:
        # LINEAJE: enforce() `messages` at agent->llm pre_model — scan flagged AI_DAT_SEC_011 (Do not send PII and/or secrets to AI Models). Mask/block; do not remove without review. site_id='site:sha256:70fa495cc0463b8b62feb916383129fae87c701c8f49a86dcbe658cfd682c629'
        _gr_client = _lineaje_load_gr_client()
        _gr_site = _gr_client.SiteDescriptor(site_id='site:sha256:70fa495cc0463b8b62feb916383129fae87c701c8f49a86dcbe658cfd682c629', phase='pre_model', boundary={'source': 'agent_message', 'sink': 'model'}, candidate_policies=[], fail_mode='ALLOW_WITH_AUDIT', source_type='agent', destination_type='llm')
        messages = _gr_client.enforce(_gr_site, messages, content_type='application/json', variable_name='messages', source_file=__file__, before_line=31)
        response = client.chat.completions.create(
            model="nvidia/nemotron-3-super-120b-a12b:free",
            messages=messages
        )

        reply = response.choices[0].message.content
        # LINEAJE: enforce() `reply` at llm->agent post_model — scan flagged AI_APP_SEC_006 (Use only LLMs from the organization's approved list.); AI_APP_SEC_023 (Client must validate and sanitize any output from a MCP server); AI_APP_SEC_028 (Do not use LLMs from the organization's disallowed list). Mask/block; do not remove without review. site_id='site:sha256:55171778fd7c3720ec8dd579051eab96945d861c81a1eef12fc5071179f7dd80'
        _gr_client = _lineaje_load_gr_client()
        _gr_site = _gr_client.SiteDescriptor(site_id='site:sha256:55171778fd7c3720ec8dd579051eab96945d861c81a1eef12fc5071179f7dd80', phase='post_model', boundary={'source': 'model', 'sink': 'agent_message'}, candidate_policies=[], fail_mode='ALLOW_WITH_AUDIT', source_type='llm', destination_type='agent')
        reply = _gr_client.enforce(_gr_site, reply, content_type='application/json', variable_name='reply', source_file=__file__, before_line=36)
        # LINEAJE: enforce() `reply` at agent->log log_emit — scan flagged AI_APP_SEC_023 (Client must validate and sanitize any output from a MCP server). Mask/block; do not remove without review. site_id='site:sha256:c8efd315656a0577efbfe1b45dc1925e8cf5ceca6b851a1393803b5823a0e2cf'
        _gr_client = _lineaje_load_gr_client()
        _gr_site = _gr_client.SiteDescriptor(site_id='site:sha256:c8efd315656a0577efbfe1b45dc1925e8cf5ceca6b851a1393803b5823a0e2cf', phase='log_emit', boundary={'source': 'log', 'sink': 'log'}, candidate_policies=[{'policy_id': 'AI_DAT_SEC_010', 'guardrail_id': 'Mask PII in Logs', 'policy_version': '2026.08.1'}], fail_mode='BLOCK', source_type='agent', destination_type='log')
        reply = _gr_client.enforce(_gr_site, reply, content_type='application/json')
        print("AI:", reply)

        messages.append({"role": "assistant", "content": reply})

    except Exception as e:
        # LINEAJE: enforce() `e` at agent->log log_emit — scan flagged AI_APP_SEC_006 (Use only LLMs from the organization's approved list.); AI_APP_SEC_023 (Client must validate and sanitize any output from a MCP server); AI_APP_SEC_028 (Do not use LLMs from the organization's disallowed list). Mask/block; do not remove without review. site_id='site:sha256:6eb6961c74d7529817bbf771bbc7baa50e4a4bdc10f3095a6ad3a6d0ca1f8da3'
        _gr_client = _lineaje_load_gr_client()
        _gr_site = _gr_client.SiteDescriptor(site_id='site:sha256:6eb6961c74d7529817bbf771bbc7baa50e4a4bdc10f3095a6ad3a6d0ca1f8da3', phase='log_emit', boundary={'source': 'log', 'sink': 'log'}, candidate_policies=[{'policy_id': 'AI_DAT_SEC_010', 'guardrail_id': 'Mask PII in Logs', 'policy_version': '2026.08.1'}], fail_mode='BLOCK', source_type='agent', destination_type='log')
        e = _gr_client.enforce(_gr_site, e, content_type='application/json')
        print("Error:", e)