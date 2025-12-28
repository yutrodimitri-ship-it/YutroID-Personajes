# Yutro ID Generator v3.3.0 🇨🇱

Generador de prompts detallados para personajes chilenos diversos en ComfyUI.

## 🌟 Características v3.3.0

- ✅ **Versión Bilingüe**: Nodos separados en Español e Inglés
- ✅ **Full Body Portraits**: Cuerpo completo siempre visible
- ✅ **Logo YUTRO**: Visible en ropa interior
- ✅ **Diversidad e Inclusión**: 13 etnias chilenas
- ✅ **Albinismo**: Mantiene rasgos faciales étnicos
- ✅ **21 Colores de Pelo**: Naturales, teñidos y fantasía
- ✅ **8 Estilos de Vello Facial**: Desde barba corta hasta patillas
- ✅ **10 Tipos de Cuerpo**: Incluyendo sobrepeso y obesidad mórbida
- ✅ **Retrocompatibilidad Total**: Workflows antiguos siguen funcionando

---

## 📥 Instalación

### Opción A: Instalación Manual

1. **Descargar archivos:**
   - `yutro_node.py`
   - `__init__.py`

2. **Crear carpeta del nodo:**
   ```bash
   cd ComfyUI/custom_nodes/
   mkdir ComfyUI-YutroID
   ```

3. **Copiar archivos:**
   ```bash
   cp yutro_node.py ComfyUI/custom_nodes/ComfyUI-YutroID/
   cp __init__.py ComfyUI/custom_nodes/ComfyUI-YutroID/
   ```

4. **Reiniciar ComfyUI**

### Opción B: Git Clone (si lo subes a GitHub)

```bash
cd ComfyUI/custom_nodes/
git clone https://github.com/TU_USUARIO/ComfyUI-YutroID.git
# Reiniciar ComfyUI
```

---

## 🎯 Uso

### 1. Agregar Nodo

En ComfyUI, presiona **botón derecho** > **Add Node** > **Yutro ID** > Elige tu versión:

- 🇪🇸 **Yutro ID Generator (ES) v3.3** - Interfaz en español
- 🇬🇧 **Yutro ID Generator (EN) v3.3** - Interfaz en inglés

### 2. Configurar Parámetros

Ambas versiones tienen los mismos parámetros:

| Campo | Opciones | Descripción |
|-------|----------|-------------|
| **Género** | 7 opciones | Identidad de género (cis, trans, no binario, etc.) |
| **Edad** | 8 rangos | Desde niños (8-12) hasta ancianos (80+) |
| **Etnia** | 13 etnias | Diversidad chilena (Mapuche, Rapa Nui, mestizo, etc.) |
| **Cuerpo** | 10 tipos | Desde delgado hasta obesidad mórbida |
| **Forma Cara** | 6 formas | Ovalada, cuadrada, redonda, corazón, etc. |
| **Piel** | 9 tonos | Desde mate claro hasta albino |
| **Estilo Pelo** | 20 estilos | Largo, corto, afro, trenzas, fade, mohawk, etc. |
| **Color Pelo** | 21 colores | Naturales, teñidos y fantasía |
| **Vello Facial** | 8 opciones | Barba, bigote, candado, patillas, etc. |

### 3. Conectar Salida

El nodo genera un **STRING** (prompt en inglés) que puedes conectar a:
- **CLIPTextEncode** (para modelos locales)
- **Text Prompt** inputs de cualquier nodo de generación

---

## 🧬 Lógica Especial: Albinismo

Cuando seleccionas **Piel: Albino**:

✅ **Mantiene:**
- Rasgos faciales étnicos (estructura ósea, forma de ojos)
- Textura de cabello étnica

❌ **Bloquea/Modifica:**
- Color de piel → Pálido porcelana (forzado)
- Color de cabello → Blanco nieve (forzado)
- Ojos → Azul/gris muy claro (agregado)

**Ejemplo:**
- Etnia: **Mapuche Araucanía**
- Piel: **Albino**

**Resultado:**
```
"Mapuche indigenous Chilean, native facial features... 
albinism condition, very pale porcelain white skin... 
straight thick hair texture, typical indigenous hair... 
snow white hair color due to albinism..."
```

---

## 📊 Ejemplos de Uso

### Ejemplo 1: Mujer Mapuche Joven
```
🇪🇸 INPUTS (Español):
- Género: Mujer Cis
- Edad: Joven 18-24
- Etnia: Mapuche Araucania
- Cuerpo: Atletico
- Piel: Morena
- Estilo Pelo: Trenzas
- Color Pelo: Negro Azulado (Chileno)
- Vello Facial: Ninguno
```

**OUTPUT (Prompt en inglés):**
```
Full body portrait of a young adult, 22 years old woman, standing pose, 
entire body visible from head to feet. Mapuche indigenous Chilean, 
native facial features from Araucanía region, strong indigenous facial 
structure, prominent cheekbones. athletic build, toned muscles. 
oval face shape. tan complexion. braided hair. typical Chilean blue-black 
hair, natural dark tone common in Chile. wearing plain grey sports bra 
with 'YUTRO' brand logo on elastic underband...
```

---

### Ejemplo 2: Hombre Italiano con Barba
```
🇬🇧 INPUTS (English):
- Genero: Cis Man
- Edad: Mature Adult 35-49
- Etnia Origen: Italian Descent
- Cuerpo: Stocky
- Piel: Olive
- Estilo Pelo: Short Textured
- Color Pelo: Dark Brown
- Vello Facial: Goatee
```

**OUTPUT (Prompt en inglés):**
```
Full body portrait of a mature adult, 40 years old man, standing pose,
entire body visible from head to feet. Chilean of Italian descent, 
Mediterranean facial features, expressive eyes, well-defined nose, 
balanced facial proportions. stocky and muscular build. square jawline, 
defined facial structure. olive skin tone. short textured haircut. 
dark brown hair. goatee beard style, chin beard with mustache, 
Van Dyke style. wearing plain grey boxer briefs with 'YUTRO' brand text...
```

---

### Ejemplo 3: Persona No Binaria con Pelo Fantasía
```
🇪🇸 INPUTS:
- Género: No Binario
- Edad: Joven 18-24
- Etnia: Mestizo Chileno Promedio
- Cuerpo: Delgado
- Piel: Mate Claro
- Estilo Pelo: Wolf Cut
- Color Pelo: Rosa Pastel (Fantasia)
- Vello Facial: Ninguno
```

**OUTPUT:**
```
Full body portrait of a young adult, 22 years old non-binary person, 
standing pose, entire body visible from head to feet. Chilean mestizo 
ethnicity, latin american facial features, mixed indigenous and european 
heritage. slim build. oval face shape. fair matte skin tone. wolf cut 
layered hairstyle. fantasy pastel pink hair, artistic pink coloring. 
wearing plain grey sports bra or boxer briefs with 'YUTRO' text...
```

---

## 🔄 Retrocompatibilidad

Este nodo es compatible con workflows antiguos:

| Versión Antigua | Nueva v3.3 | Estado |
|----------------|------------|--------|
| "Croata Magallanes" | "Ascendencia Croata" | ✅ Auto-mapeado |
| "Negro Azabache" | "Negro Azulado" | ✅ Auto-mapeado |
| "caracteristicas_extra" | "vello_facial" | ⚠️ Perdido si no es barba/bigote |

---

## 🆕 Changelog

### v3.3.0 (2025-12-15)
- 🌍 Versión bilingüe: nodos separados ES/EN
- ✅ Interfaz completamente traducida
- ✅ Prompts siempre en inglés (óptimo para IA)

### v3.2.0
- 🔄 "caracteristicas_extra" → "vello_facial"
- ✅ Nuevos tipos de cuerpo: Sobrepeso, Obesidad Mórbida
- ✅ Nueva etnia: Ascendencia Italiana
- 🔄 21 colores de pelo (lista completa)

### v3.1.0
- 🔧 Lógica de albinismo corregida
- ✅ Albino mantiene rasgos faciales étnicos

### v3.0.0
- ❌ Eliminados checkboxes de rasgos únicos
- ✅ Albino como tipo de piel

---

## 🤝 Créditos

**Desarrollado para:** Proyecto YUTRO 🇨🇱

**Especializado en:** Diversidad chilena, inclusión, representación realista

**Compatible con:** ComfyUI, Flux, SDXL, SD 1.5, Z-Image, y cualquier modelo que acepte prompts en inglés

---

## 📄 Licencia

Uso libre para proyectos personales y comerciales.

---

## 🐛 Reporte de Bugs

Si encuentras problemas:
1. Verifica que ambos archivos (`yutro_node.py` y `__init__.py`) estén en la misma carpeta
2. Revisa la consola de ComfyUI para mensajes de error
3. Asegúrate de reiniciar ComfyUI después de la instalación

---

## 📧 Contacto

¿Preguntas? ¿Sugerencias? ¡Contáctanos!

---

**¡Disfruta creando personajes chilenos diversos! 🇨🇱✨**
