# FastFlowLM-gtk

**FastFlowLM-gtk** is a minimalist, native interface for the [FastFlowLM](https://github.com/FastFlowLM/FastFlowLM) LLM engine. Built with GTK 4 and Libadwaita, it provides a distraction-free environment for chatting with local LLMs on Arch Linux.

---

## 🚀 Key Features

*   **Native Performance:** Built for speed using GTK 4/Libadwaita. No browser or Electron bloat.
*   **Intelligent Session Management:** Automatic history saving, searchable chat sidebar, and robust session loading.
*   **Vision-Ready:** Support for attaching images to supported VLM models.
*   **System Awareness:** Real-time RAM monitoring and smart server lifecycle management.
*   **Theming:** Dynamic accent color support that matches your desktop theme.
*   **Robust Streaming:** Real-time token streaming with resilient connection handling.

---

## 🏗 Architectural Overview

The application follows a clean, modular structure to ensure maintainability and separation of concerns:

| Module | Responsibility |
| :--- | :--- |
| `main.py` | **Controller:** Orchestrates application lifecycle and state. |
| `ui.py` | **Layouts:** Static widget and sidebar construction. |
| `display.py` | **Rendering:** Handles UI updates, chat bubbles, and state changes. |
| `handlers.py` | **Events:** Interaction logic (keyboard shortcuts, clicks, sending). |
| `models.py` | **System:** Server lifecycle and model management (downloads/repairs). |
| `network.py` | **Transport:** Asynchronous communication with the LLM backend. |
| `sessions.py` | **Persistence:** Chat history saving and metadata indexing. |
| `theme.py` | **Style:** Dynamic CSS injection. |
| `flm.py` | **Glue:** Wrapper functions for the `flm` command-line tools. |
| `utils.py` | **Helpers:** Markdown processing and CSS definitions. |

---

## 🛠 Setup & Installation

### Arch Linux (AUR)
If you're on Arch, use your preferred AUR helper:
```bash
yay -S fastflowlm-gtk
```

### Manual Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/marleylinux/FastFlowLM-gtk
   cd FastFlowLM-gtk
   ```
2. **Install dependencies:**
   Ensure you have the required dependencies: `fastflowlm`, `python`, `python-gobject`, `gtk4`, `libadwaita`, `libsoup3`, `gtksourceview5`, and `python-psutil`.
3. **Run the installation script:**
   ```bash
   sudo ./install.sh
   ```

---

## 💡 Usage Notes

*   **Model Management:** Use the "Repair" button (refresh icon) in the top header bar to force-reinstall corrupted models without manual file manipulation.
*   **Mid-Chat Switching:** You can enable model switching mid-conversation via the options menu, though this may trigger a model server reload.
*   **System Locks:** The app manages model resource usage via `~/.config/flm/model_ram.lock` to prevent system instability.

---

## 🤝 Contribution
Contributions are welcome! Please open an issue or pull request for any bugs or enhancements.

*Powered by [FastFlowLM](https://github.com/FastFlowLM/FastFlowLM).*
*Contact: warburtonmarley@proton.me*
