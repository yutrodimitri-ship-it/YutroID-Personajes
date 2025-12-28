# Changelog

Todas las versiones y cambios importantes del proyecto.

---

## [v3.3.1] - 2025-12-15

### 🔧 Corregido
- **Nombres de campos traducidos en versión EN**
  - `genero` → `gender`
  - `edad` → `age`
  - `etnia_origen` → `ethnicity`
  - `cuerpo` → `body_type`
  - `forma_cara` → `face_shape`
  - `piel` → `skin_tone`
  - `estilo_pelo` → `hair_style`
  - `color_pelo` → `hair_color`
  - `vello_facial` → `facial_hair`

### ✨ Mejorado
- Sistema de mapeo automático entre parámetros EN/ES
- Método `generate_prompt()` ahora acepta `**kwargs` flexible

---

## [v3.3.0] - 2025-12-15

### 🌍 Nuevo
- **Versión bilingüe**: Dos nodos separados
  - `Yutro ID Generator 🇨🇱 (ES) v3.3` - Interfaz en español
  - `Yutro ID Generator 🇨🇱 (EN) v3.3` - Interfaz en inglés
- Ambos nodos comparten la misma lógica interna
- Prompts siempre generados en inglés (óptimo para IA)

### 🏗️ Arquitectura
- Clase base `YutroIDGeneratorBase` con lógica compartida
- Clases wrapper `YutroIDGenerator_ES` y `YutroIDGenerator_EN`
- Sistema de retrocompatibilidad mejorado

---

## [v3.2.0] - 2025-12-15

### 🔄 Cambios
- **Campo renombrado**: `caracteristicas_extra` → `vello_facial`
- **Opciones eliminadas**: Pecas, lunares, piercings, cicatrices, tatuajes

### ✨ Nuevo
- **Cuerpo**: Agregados "Sobrepeso" y "Obesidad Morbida"
- **Etnia**: Nueva opción "Ascendencia Italiana"
- **Etnias renombradas**:
  - Croata Magallanes → Ascendencia Croata
  - Palestino Patronato → Ascendencia Palestina
  - Aleman Llanquihue → Ascendencia Alemana
- **Color de pelo**: 21 opciones (vs 10 anteriores)
  - Naturales: Negro Azulado, Castaño, Rubio, etc.
  - Teñidos: con indicador "(Tinte)"
  - Fantasía: Azul Eléctrico, Rosa Pastel, Verde Neón

### 🎨 Vello Facial
- Barba corta
- Barba larga
- Bigote
- Candado (goatee)
- Barba de 3 días (stubble)
- Patillas largas (sideburns)
- Mosca (soul patch)

---

## [v3.1.0] - 2025-12-15

### 🔧 Corregido
- **Lógica de albinismo**: Ahora mantiene rasgos faciales étnicos
- Albinismo solo afecta: color de piel, pelo y ojos
- Albinismo NO afecta: estructura facial, origen étnico

### 🧬 Mejorado
- Separación de diccionarios:
  - `ethnicity_facial_features` (siempre se aplica)
  - `ethnicity_skin_tone` (bloqueado con albinismo)
  - `ethnicity_hair_texture` (se aplica con albinismo)

---

## [v3.0.0] - 2025-12-15

### ❌ Eliminado
- **Todos los checkboxes de rasgos únicos** (20 opciones)
  - implante_coclear, audifonos, sindrome_down, etc.
- Simplificación de la interfaz

### ✨ Nuevo
- **"Albino" como tipo de piel** en dropdown
- Lógica automática de bloqueo de colores

---

## [v2.5.0] - 2025-12-14

### ✨ Nuevo
- Campo "Características Extra" agregado
- 10 opciones: pecas, lunares, tatuajes, piercings, etc.

### ✅ Mejorado
- Sistema de retrocompatibilidad con mapeos completos
- Validación de valores legacy

---

## [v2.0.0] - 2025-12-13

### 🎉 Lanzamiento inicial
- Full body portraits
- Logo YUTRO en ropa
- 12 etnias chilenas
- 20 estilos de pelo
- Ropa según edad (niños vs adultos)
- Rasgos únicos (checkboxes de inclusión)

---

## Leyenda de Símbolos

- ✨ Nuevo feature
- 🔧 Corrección de bug
- 🔄 Cambio/Refactor
- ❌ Eliminado
- 🎨 Mejora visual
- 🧬 Mejora lógica
- 🌍 Internacionalización
- 🏗️ Arquitectura
- 📝 Documentación
