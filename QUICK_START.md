# ⚡ Quick Start - 5 Minutos

## 🚀 Instalación Express

### 1️⃣ Descomprime el ZIP
```
ComfyUI-YutroID-v3.3.1.zip → ComfyUI-YutroID/
```

### 2️⃣ Mueve la carpeta
```bash
# Arrastra la carpeta "ComfyUI-YutroID" a:
ComfyUI/custom_nodes/

# Resultado:
ComfyUI/custom_nodes/ComfyUI-YutroID/
```

### 3️⃣ Reinicia ComfyUI
- Cierra ComfyUI
- Vuelve a abrirlo

### 4️⃣ ¡Listo! ✅
- Clic derecho → Add Node → Yutro ID
- Verás 2 nodos: **(ES)** y **(EN)**

---

## 🎯 Uso en 30 Segundos

1. **Agrega el nodo**: Clic derecho → Add Node → Yutro ID → (ES) o (EN)
2. **Configura**: Elige opciones en los dropdowns
3. **Conecta**: Output STRING → CLIP Text Encode
4. **Genera**: ¡Run!

---

## 📁 ¿Qué incluye?

| Archivo | Descripción |
|---------|-------------|
| `yutro_node.py` | ⚙️ Código principal del nodo |
| `__init__.py` | 🔧 Inicializador de ComfyUI |
| `README.md` | 📖 Documentación completa |
| `EXAMPLES.md` | 🎨 8 ejemplos con prompts |
| `INSTALL_ES.md` | 🇪🇸 Guía de instalación |
| `CHANGELOG.md` | 📝 Historial de versiones |
| `LICENSE` | ⚖️ Licencia MIT |
| `requirements.txt` | 📦 Dependencias (ninguna) |

---

## 🆘 Problemas Comunes

### ❌ "El nodo no aparece"
✅ **Solución:** Verifica que la carpeta esté en `custom_nodes/` y reinicia.

### ❌ "Error al cargar"
✅ **Solución:** Asegúrate de tener ambos archivos: `yutro_node.py` y `__init__.py`

### ❌ "Dropdowns vacíos"
✅ **Solución:** Revisa la consola de ComfyUI por errores y re-descarga el archivo.

---

## 🎓 Aprende Más

- 📖 **README.md** - Documentación completa
- 🎨 **EXAMPLES.md** - 8 ejemplos detallados
- 🇪🇸 **INSTALL_ES.md** - Guía paso a paso

---

## 💡 Tip Pro

**Para mejores resultados:**
- CFG Scale: 7-9
- Steps: 25-40
- Modelos recomendados: Flux, SDXL, Z-Image

---

¡Ya estás listo para crear personajes chilenos diversos! 🇨🇱✨
