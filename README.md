# FastFlowLM-gtk

A native GTK4 chat client for [FastFlowLM](https://github.com/FastFlowLM/FastFlowLM).

It belongs on desktop Linux. It uses GTK4, `GtkSourceView 5`, and avoids bloated Electron/web frameworks so it doesn't chew through your RAM just to talk to local LLMs. It fits cleanly into GNOME or tiling window managers.

No telemetry, no tracking, no web. Just a simple offline tool.

---

## Features

*   **Model switching** – Download and switch local models directly within the UI.
*   **Syntax highlighting** – Uses real `GtkSourceView 5` components (Python, C++, JS, Bash, etc.).
*   **VLM / Image input** – Drag and drop image files directly into the input to prompt vision models.
*   **Keyboard navigation** – Hotkeys for sidebar, new chat, copy last output, and search.
*   **RAM limits check** – Warns before loading a model that will likely freeze your system.

---

## Keyboard Shortcuts

| Shortcut | Action |
| :--- | :--- |
| **Ctrl + N** | Start a new chat session |
| **Ctrl + F** | Search through chat history |
| **F9** | Toggle the sidebar display |
| **Ctrl + Shift + C** | Copy the last assistant response to your clipboard |
| **Ctrl + ?** or **Ctrl + /** | Show the shortcut helper dialog |
| **Enter** | Send your message |
| **Shift + Enter** | Insert a new line in the text box |

---

## Setup Requirements: memory locking (memlock)

Local model loading via `fastflowlm` requires memory locking limits to be set to infinity. If you skip this, it crashes.

Here is how to set it to unlimited:

1. Open `/etc/security/limits.conf` as root:
   ```bash
   sudo nano /etc/security/limits.conf
   ```
2. Add these to the bottom (replace `your-username` with your actual Linux user):
   ```text
   your-username    soft    memlock    unlimited
   your-username    hard    memlock    unlimited
   ```
3. Log out or restart for the limits to take effect.

---

## Getting Started (Arch Linux)

Dependencies: `gtk4`, `libadwaita`, `gtksourceview5`, `libsoup3`, `python-gobject`, `python-psutil`, `fastflowlm`, `xrt-plugin-amdxdna`.

### 1. Install dependencies:
```bash
sudo pacman -S gtk4 libadwaita gtksourceview5 libsoup3 python-gobject python-psutil fastflowlm xrt-plugin-amdxdna
```

### 2. Install from the AUR:
```bash
yay -S fastflowlm-gtk
```

### 3. Manual installation:
```bash
git clone https://github.com/marleylinux/FastFlowLM-gtk
cd FastFlowLM-gtk
sudo ./install.sh
```

### Run without installing:
```bash
python app.py
```
