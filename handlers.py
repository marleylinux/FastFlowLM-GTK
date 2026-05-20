"""
Module for UI event handlers.
Contains logic for user interactions like key presses and sending messages.
"""
import gi
gi.require_version("Gtk", "4.0")
gi.require_version("Gdk", "4.0")
from gi.repository import Gtk, Gdk, GLib
import asyncio

def on_key_pressed(app, ctrl: Gtk.EventControllerKey, keyval: int, keycode: int, state: Gdk.ModifierType) -> bool:
    """Handles Enter key press to send messages (unless SHIFT is held)."""
    if keyval == Gdk.KEY_Return:
        if not (state & Gdk.ModifierType.SHIFT_MASK):
            on_send(app, None)
            return True
    return False

def on_send(app, widget: Optional[Gtk.Widget]) -> None:
    """Handles the send action triggered by the button or Enter key."""
    if app.is_sending:
        return
        
    buffer = app.entry.get_buffer()
    start, end = buffer.get_bounds()
    text = buffer.get_text(start, end, True).strip()
    
    if not text and not app.selected_image_path:
        return
        
    app.is_sending = True
    
    # Immediate UI lock
    app.input_box.set_sensitive(False)
    app.entry.set_editable(False)
        
    buffer.set_text("")
    app.add_message(text, is_user=True, image_path=app.selected_image_path)
    app.history.append({"role": "user", "content": text, "image": app.selected_image_path})
    
    app.selected_image_path = None
    app.update_thumbnail()
    
    app.save_session()
    app.update_model_ui()
    app.ai_task = asyncio.create_task(app.get_ai_response())
    app.tasks.add(app.ai_task)
    
    GLib.idle_add(app.scroll_to_bottom)
