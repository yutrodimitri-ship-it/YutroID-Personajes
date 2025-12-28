# 🇪🇸 Guía de Instalación - YutroID Generator

## 📋 Requisitos Previos

- **ComfyUI** instalado y funcionando
- **Python 3.9+**
- **Git** (opcional, para actualizaciones automáticas)

---

## 🚀 Método 1: Instalación Manual (Recomendado)

### Paso 1: Descargar la carpeta

Descarga la carpeta completa `ComfyUI-YutroID` desde el repositorio.

### Paso 2: Copiar a custom_nodes

```bash
# Navega a tu carpeta de ComfyUI
cd /ruta/a/tu/ComfyUI/

# Copia la carpeta a custom_nodes
cp -r /ruta/descarga/ComfyUI-YutroID custom_nodes/
```

O manualmente:
1. Abre la carpeta `ComfyUI/custom_nodes/`
2. Arrastra la carpeta `ComfyUI-YutroID` aquí

### Paso 3: Reiniciar ComfyUI

```bash
# Si ComfyUI está corriendo, detenlo (Ctrl+C)
# Luego reinicia:
python main.py
```

O si usas el ejecutable, simplemente ciérralo y vuelve a abrirlo.

### Paso 4: Verificar instalación

1. En ComfyUI, haz **clic derecho** en el canvas
2. Ve a **Add Node** → **Yutro ID**
3. Deberías ver:
   - ✅ `Yutro ID Generator 🇨🇱 (ES) v3.3.1`
   - ✅ `Yutro ID Generator 🇨🇱 (EN) v3.3.1`

---

## 🔧 Método 2: Instalación con Git

```bash
cd ComfyUI/custom_nodes/
git clone https://github.com/TU_USUARIO/ComfyUI-YutroID.git
```

Luego reinicia ComfyUI.

### Actualizar con Git:
```bash
cd ComfyUI/custom_nodes/ComfyUI-YutroID/
git pull
```

---

## 🎯 Uso Rápido

### 1. Agregar el nodo

- **Clic derecho** → **Add Node** → **Yutro ID**
- Elige tu versión:
  - 🇪🇸 **(ES)** si prefieres español
  - 🇬🇧 **(EN)** si prefieres inglés

### 2. Conectar a tu workflow

```
Yutro ID Generator → [STRING Output]
                      ↓
                   CLIP Text Encode
                      ↓
                   KSampler / Generador
```

### 3. Configurar parámetros

Ajusta los dropdowns según el personaje que quieras generar.

### 4. ¡Generar!

El nodo produce un prompt en inglés optimizado para modelos de IA.

---

## ❓ Solución de Problemas

### El nodo no aparece en el menú

**Solución:**
1. Verifica que la carpeta esté en `ComfyUI/custom_nodes/`
2. Asegúrate de que ambos archivos existan:
   - `yutro_node.py`
   - `__init__.py`
3. Revisa la consola de ComfyUI por errores
4. Reinicia ComfyUI completamente

### Error: "No module named 'yutro_node'"

**Solución:**
- El archivo `__init__.py` está mal o falta
- Verifica que contenga: `from .yutro_node import NODE_CLASS_MAPPINGS`

### Los dropdowns están vacíos

**Solución:**
- Error en `yutro_node.py`
- Revisa la consola de ComfyUI para ver el error específico
- Re-descarga el archivo `yutro_node.py`

### El prompt generado no funciona bien

**Solución:**
- Asegúrate de conectar el output STRING a un nodo CLIP Text Encode
- Verifica que tu modelo de IA entienda prompts en inglés
- Si usas modelos antiguos (SD 1.5), simplifica las descripciones

---

## 🆕 Actualizar de Versiones Anteriores

### Desde v3.x a v3.3.1

```bash
# Haz backup de tu versión actual
cp -r ComfyUI/custom_nodes/ComfyUI-YutroID ComfyUI/custom_nodes/ComfyUI-YutroID_backup

# Reemplaza el archivo principal
cp yutro_node.py ComfyUI/custom_nodes/ComfyUI-YutroID/

# Reinicia ComfyUI
```

**Nota:** Los workflows antiguos seguirán funcionando (retrocompatibilidad total).

---

## 📧 Soporte

¿Problemas? ¿Preguntas?

- 📖 Lee el [README.md](README.md)
- 📝 Revisa el [CHANGELOG.md](CHANGELOG.md)
- 🐛 Reporta bugs abriendo un issue

---

¡Disfruta creando personajes chilenos diversos! 🇨🇱✨
