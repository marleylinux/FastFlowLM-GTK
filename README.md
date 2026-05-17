# FastFlowLM-gtk

A minimalist desktop interface for [FastFlowLM](https://github.com/FastFlowLM/FastFlowLM).

FastFlowLM-gtk is a lightweight, distraction-free application built with GTK 4 and Libadwaita. It serves as a dedicated interface for interacting with local LLMs, focusing on a clean, simple layout.

## Installation

### AUR (Recommended)
You can install this package using your favorite AUR helper:
```bash
yay -S fastflowlm-gtk
# OR
paru -S fastflowlm-gtk
```

### Manual Installation
If you prefer to build from source:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/marleylinux/FastFlowLM-GTK
   cd FastFlowLM-GTK
   ```

2. **Run the installer:**
   ```bash
   chmod +x install.sh
   sudo ./install.sh
   ```

The script installs `fastflowlm` and all required GTK/GNOME dependencies, then sets up the application.

## Features
- **Distraction-free interface:** Uses standard GNOME dark mode with black AI chat bubbles for clear reading.
- **Backend management:** Detects flm serve status and handles lifecycle management.
- **Session-based model loading:** Automates model loading and unloading per session to optimize resource usage.
- **History persistence:** Automatically saves chat sessions to the configuration directory, using the first prompt as the chat title.
- **Syntax highlighting:** Provides high-quality syntax highlighting for code blocks using GtkSourceView 5.
- **Minimal controls:** Includes basic session and model management without extra overhead.

## System Dependencies
The installation process ensures the following are present on your system:
- `fastflowlm`: The backend engine.
- `python`, `python-gobject`: Required for application logic and GTK bindings.
- `gtk4`, `libadwaita`: Modern UI toolkit components.
- `libsoup3`: Handles asynchronous HTTP communication.
- `gtksourceview5`: Provides professional-grade syntax highlighting.
