# FastFlowLM-gtk

A distraction-free, ultra-minimalist desktop interface for [FastFlowLM](https://github.com/FastFlowLM/FastFlowLM).

I built this because I wanted a way to interact with local LLMs that didn't feel like a cluttered web browser or a heavy application. FastFlowLM-gtk is designed to stay out of your way: it's just you, the model, and the chat.

## Features
- **Pure "Just Talk" Experience:** Standard GNOME dark mode with clean, floating AI chat bubbles that blend seamlessly into the background.
- **Auto-Server Management:** No need to tinker with ports—it detects if the server is running, and if not, it handles the lifecycle for you.
- **Smart Model Loading:** Pinned installed models for quick access and a "click-to-download" flow for everything else.
- **Persistent Chat History:** Everything you talk about is saved automatically to your config folder, with the first prompt acting as the chat title.
- **Professional Coding:** Includes high-quality syntax highlighting for code blocks so you can paste and read code directly in the chat.
- **No Clutter:** Simple "Eject" and "New Chat" buttons—nothing more.

## Quick Installation

This application is built for Arch Linux. We've made installation a one-command process that takes care of your system dependencies for you.

1. **Clone the repo:**
   ```bash
   git clone https://github.com/marleylinux/FastFlowLM-GTK
   cd FastFlowLM-GTK
   ```

2. **Run the installer:**
   ```bash
   chmod +x install.sh
   sudo ./install.sh
   ```

That’s it! The script will automatically install `fastflowlm` and all required GTK/GNOME dependencies from the Arch repositories, then set up the application for you. You can find "FastFlowLM-gtk" in your application launcher.
