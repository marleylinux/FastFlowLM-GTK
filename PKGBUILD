# Maintainer: Marley <warburtonmarley@proton.me>
pkgname=fastflowlm-gtk
pkgver=1.8.5
pkgrel=2
pkgdesc="A minimalist, modern desktop interface for FastFlowLM, built with GTK 4 and Libadwaita."
arch=('any')
url="https://github.com/marleylinux/FastFlowLM-GTK"
license=('MIT')
depends=('python' 'python-gobject' 'gtk4' 'libadwaita' 'libsoup3' 'gtksourceview5' 'python-psutil' 'fastflowlm' 'xrt-plugin-amdxdna')
makedepends=('imagemagick')
source=("com.marley.FastFlowLM-gtk.desktop"
        "flm-gtk.webp"
        "app.py"
        "main.py"
        "flm.py"
        "utils.py"
        "ui.py"
        "sessions.py"
        "network.py"
        "theme.py"
        "handlers.py"
        "models.py"
        "display.py"
        "init_gi.py"
        "assets/llama.png"
        "assets/qwen.png"
        "assets/gemini.png"
        "assets/mistral.png"
        "assets/phi.png")
        sha256sums=('SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP' 'SKIP')

package() {
  # Install Python files
  install -d "$pkgdir/usr/share/fastflowlm-gtk"
  install -m644 "$srcdir/"*.py "$pkgdir/usr/share/fastflowlm-gtk/"
  chmod 755 "$pkgdir/usr/share/fastflowlm-gtk/app.py"

  # Install custom model avatars
  install -d "$pkgdir/usr/share/fastflowlm-gtk/assets"
  for avatar in llama qwen gemini mistral phi; do
    if [ -f "$srcdir/assets/$avatar.png" ]; then
      install -m644 "$srcdir/assets/$avatar.png" "$pkgdir/usr/share/fastflowlm-gtk/assets/"
    elif [ -f "$srcdir/$avatar.png" ]; then
      install -m644 "$srcdir/$avatar.png" "$pkgdir/usr/share/fastflowlm-gtk/assets/$avatar.png"
    fi
  done

  # Install Icon (Convert to PNG with transparency preservation)
  install -d "$pkgdir/usr/share/icons/hicolor/256x256/apps"
  magick "$srcdir/flm-gtk.webp" "$pkgdir/usr/share/icons/hicolor/256x256/apps/com.marley.FastFlowLM-gtk.png"

  # Install Desktop file
  install -Dm644 "$srcdir/com.marley.FastFlowLM-gtk.desktop" "$pkgdir/usr/share/applications/com.marley.FastFlowLM-gtk.desktop"

  # Create executable wrapper
  install -d "$pkgdir/usr/bin"
  cat <<EOF > "$pkgdir/usr/bin/fastflowlm-gtk"
#!/bin/sh
export PYTHONPATH="/usr/share/fastflowlm-gtk:\$PYTHONPATH"
exec python /usr/share/fastflowlm-gtk/app.py "\$@"
EOF
  chmod +x "$pkgdir/usr/bin/fastflowlm-gtk"
}
