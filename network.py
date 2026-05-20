"""
Module for API network interactions.
Manages asynchronous communication with the local LLM server.
"""
import json
import gi
gi.require_version("Soup", "3.0")
from gi.repository import Soup, GLib
from typing import List

async def get_ai_response(app, bubble: Gtk.Label, thinking_label: Gtk.Label, messages: List[dict]):
    """Prepares and executes the chat completion request."""
    payload = {
        "model": app.current_model,
        "messages": messages,
        "stream": True
    }
    
    msg = Soup.Message.new("POST", f"{app.BASE_URL}/chat/completions")
    msg.set_request_body_from_bytes("application/json", GLib.Bytes.new(json.dumps(payload).encode()))
    
    return await app.session.send_async(msg, GLib.PRIORITY_DEFAULT, None)
