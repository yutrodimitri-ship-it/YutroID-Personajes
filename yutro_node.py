"""
YutroIDGenerator - ComfyUI Custom Node v3.3.1
Generador de prompts detallados para personajes chilenos diversos

CAMBIOS v3.3.1:
- 🔧 CORREGIDO: Nombres de campos traducidos en versión EN
- 🇪🇸 Versión ES: genero, edad, etnia_origen, cuerpo, etc.
- 🇬🇧 Versión EN: gender, age, ethnicity, body_type, etc.
- ✅ Ambos generan prompts en INGLÉS (óptimo para modelos de IA)
"""

# ===== CLASE BASE CON TODA LA LÓGICA =====
class YutroIDGeneratorBase:
    """
    Clase base con toda la lógica de generación de prompts
    Las clases ES y EN heredan de esta y solo cambian INPUT_TYPES
    """
    
    RETURN_TYPES = ("STRING",)
    FUNCTION = "generate_prompt"
    CATEGORY = "Yutro ID"
    OUTPUT_NODE = False

    def generate_prompt(self, **kwargs):
        """
        Método flexible que acepta parámetros en español o inglés
        """
        
        # Mapeo de nombres de parámetros EN->ES
        param_mapping = {
            "gender": "genero",
            "age": "edad",
            "ethnicity": "etnia_origen",
            "body_type": "cuerpo",
            "face_shape": "forma_cara",
            "skin_tone": "piel",
            "hair_style": "estilo_pelo",
            "hair_color": "color_pelo",
            "facial_hair": "vello_facial"
        }
        
        # Normalizar nombres de parámetros a español (interno)
        normalized_kwargs = {}
        for key, value in kwargs.items():
            # Si el key está en inglés, traducirlo a español
            if key in param_mapping:
                normalized_kwargs[param_mapping[key]] = value
            else:
                normalized_kwargs[key] = value
        
        # Extraer parámetros normalizados
        genero = normalized_kwargs.get("genero", "Mujer Cis")
        edad = normalized_kwargs.get("edad", "Joven 18-24")
        etnia_origen = normalized_kwargs.get("etnia_origen", "Mestizo Chileno Promedio")
        cuerpo = normalized_kwargs.get("cuerpo", "Promedio")
        forma_cara = normalized_kwargs.get("forma_cara", "Ovalada")
        piel = normalized_kwargs.get("piel", "Morena")
        estilo_pelo = normalized_kwargs.get("estilo_pelo", "Lacio Largo")
        color_pelo = normalized_kwargs.get("color_pelo", "Castano Oscuro")
        vello_facial = normalized_kwargs.get("vello_facial", "Ninguno")
        
        # ===== NORMALIZAR VALORES (traducciones y legacy) =====
        def normalize_value(value):
            """Normaliza valores antiguos y traduce EN->ES si es necesario"""
            
            # Mapeo de INGLÉS a ESPAÑOL (para versión EN del nodo)
            en_to_es = {
                # GÉNERO
                "Cis Woman": "Mujer Cis",
                "Cis Man": "Hombre Cis",
                "Non-Binary": "No Binario",
                "Trans Woman": "Mujer Trans",
                "Trans Man": "Hombre Trans",
                "Agender": "Agenero",
                "Genderfluid": "Fluido",
                
                # EDAD
                "Child 8-12": "Nino 8-12",
                "Teen 13-17": "Adolescente 13-17",
                "Young Adult 18-24": "Joven 18-24",
                "Young Adult 25-34": "Adulto Joven 25-34",
                "Mature Adult 35-49": "Adulto Maduro 35-49",
                "Middle-Aged 50-64": "Adulto Mayor 50-64",
                "Senior 65-79": "Tercera Edad 65-79",
                "Elderly 80+": "Anciano 80plus",
                
                # ETNIA
                "Chilean Mestizo": "Mestizo Chileno Promedio",
                "Mapuche Indigenous": "Mapuche Araucania",
                "Aymara Andean": "Aymara Andino",
                "Selknam Patagonian": "Selknam Austral",
                "Rapa Nui Polynesian": "Rapa Nui Polinesio",
                "Chilean Caucasian": "Chileno Caucasico",
                "Afro-Chilean": "Afro-Chileno",
                "Asian-Chilean": "Asiatico-Chileno",
                "Croatian Descent": "Ascendencia Croata",
                "Palestinian Descent": "Ascendencia Palestina",
                "German Descent": "Ascendencia Alemana",
                "Italian Descent": "Ascendencia Italiana",
                "Haitian-Chilean": "Haitiano-Chileno",
                
                # CUERPO
                "Average": "Promedio",
                "Slim": "Delgado",
                "Athletic": "Atletico",
                "Curvy": "Curvy",
                "Voluptuous": "Voluminoso",
                "Stocky": "Robusto",
                "Short & Compact": "Bajo y Compacto",
                "Tall & Slender": "Alto y Delgado",
                "Overweight": "Sobrepeso",
                "Morbidly Obese": "Obesidad Morbida",
                
                # FORMA CARA
                "Oval": "Ovalada",
                "Square Jaw": "Mandibula Cuadrada",
                "Round": "Redonda",
                "Heart": "Corazon",
                "Long": "Alargada",
                "Triangular": "Triangular",
                
                # PIEL
                "Fair Matte": "Mate Claro",
                "Tan": "Morena",
                "Bronze": "Bronceada",
                "Olive": "Oliva",
                "Cinnamon": "Canela",
                "Chocolate": "Chocolate",
                "Dark Brown": "Marron Oscuro",
                "Deep Black": "Negra Profunda",
                "Albino": "Albino",
                
                # ESTILO PELO
                "Long Straight": "Lacio Largo",
                "Loose Wavy": "Ondulado Suelto",
                "Voluminous Curly": "Rizado Voluminoso",
                "Braids": "Trenzas",
                "Natural Afro": "Afro Natural",
                "Buzz Cut": "Rapado",
                "Short Textured": "Corto Texturizado",
                "Short Bob": "Bob Corto",
                "Pixie Cut": "Pixie",
                "Ponytail": "Cola de Caballo",
                "Shoulder with Bangs": "Medio con Flequillo",
                "Dreadlocks": "Dreadlocks",
                "Low Fade": "Fade Bajo",
                "Taper Fade": "Taper Fade",
                "Undercut": "Undercut",
                "Slick Back": "Slick Back",
                "Quiff": "Quiff",
                "Mohawk": "Mohawk",
                "Wolf Cut": "Wolf Cut",
                "Shaggy Cut": "Shag Desestructurado",
                
                # COLOR PELO
                "Blue-Black": "Negro Azulado",
                "Dark Brown": "Castano Oscuro",
                "Light Brown": "Castano Claro",
                "Platinum Blonde": "Rubio Platinado",
                "Copper Red": "Rojizo Cobre",
                "Silver Grey": "Gris Plateado",
                "Natural White": "Blanco Natural",
                "Electric Blue": "Azul Electrico",
                "Pastel Pink": "Rosa Pastel",
                "Neon Green": "Verde Neon",
                "Purple Violet": "Purpura Violeta",
                "Fire Orange": "Naranja Fuego",
                "Blue-Black (Chilean)": "Negro Azulado (Chileno)",
                "Dark Brown (Common)": "Castano Oscuro (Comun)",
                "Light Brown (Dyed)": "Castano Claro (Tinte)",
                "Blonde (Dyed)": "Rubio (Tenido)",
                "Reddish (Dyed)": "Rojizo (Tinte)",
                "Grey (Natural)": "Gris (Natural)",
                "White (Elderly)": "Blanco (Adulto Mayor)",
                "Electric Blue (Fantasy)": "Azul Electrico (Fantasia)",
                "Pastel Pink (Fantasy)": "Rosa Pastel (Fantasia)",
                "Neon Green (Fantasy)": "Verde Neon (Fantasia)",
                
                # VELLO FACIAL
                "None": "Ninguno",
                "Short Beard": "Barba corta",
                "Long Beard": "Barba larga",
                "Mustache": "Bigote",
                "Goatee": "Candado",
                "Stubble": "Barba de 3 dias",
                "Long Sideburns": "Patillas largas",
                "Soul Patch": "Mosca",
            }
            
            # Mapeos legacy (versiones antiguas)
            legacy_mappings = {
                # GÉNERO
                "Mujer (Cis)": "Mujer Cis",
                "Hombre (Cis)": "Hombre Cis",
                "No Binario / Otros": "No Binario",
                
                # EDAD
                "Niño/a (8-12)": "Nino 8-12",
                "Adolescente (13-17)": "Adolescente 13-17",
                "Joven (18-24)": "Joven 18-24",
                "Adulto Joven (25-34)": "Adulto Joven 25-34",
                "Adulto Maduro (35-49)": "Adulto Maduro 35-49",
                "Adulto Mayor (50-64)": "Adulto Mayor 50-64",
                "Tercera Edad (65-79)": "Tercera Edad 65-79",
                "Anciano (80+)": "Anciano 80plus",
                
                # ETNIA
                "Croata Magallanes": "Ascendencia Croata",
                "Palestino Patronato": "Ascendencia Palestina",
                "Aleman Llanquihue": "Ascendencia Alemana",
                
                # COLOR PELO (legacy)
                "Negro Azabache": "Negro Azulado",
                "Rubio Platino": "Rubio Platinado",
                "Gris Plata": "Gris Plateado",
                "Blanco Nieve": "Blanco Natural",
                
                # VELLO FACIAL
                "Ninguna": "Ninguno",
            }
            
            # Primero intenta traducir de inglés a español
            if value in en_to_es:
                return en_to_es[value]
            
            # Luego intenta mapeos legacy
            if value in legacy_mappings:
                return legacy_mappings[value]
            
            return value
        
        # ===== DICCIONARIOS DE TRADUCCIÓN A INGLÉS (PROMPT) =====
        
        gender_map = {
            "Mujer Cis": "woman",
            "Hombre Cis": "man",
            "No Binario": "non-binary person",
            "Mujer Trans": "transgender woman",
            "Hombre Trans": "transgender man",
            "Agenero": "agender person",
            "Fluido": "genderfluid person"
        }
        
        age_map = {
            "Nino 8-12": "child, 10 years old",
            "Adolescente 13-17": "teenager, 15 years old",
            "Joven 18-24": "young adult, 22 years old",
            "Adulto Joven 25-34": "young adult, 30 years old",
            "Adulto Maduro 35-49": "mature adult, 40 years old",
            "Adulto Mayor 50-64": "middle-aged adult, 55 years old",
            "Tercera Edad 65-79": "senior, 70 years old",
            "Anciano 80plus": "elderly, 85 years old"
        }
        
        ethnicity_facial_features = {
            "Mestizo Chileno Promedio": "Chilean mestizo ethnicity, latin american facial features, mixed indigenous and european heritage",
            "Mapuche Araucania": "Mapuche indigenous Chilean, native facial features from Araucanía region, strong indigenous facial structure, prominent cheekbones",
            "Aymara Andino": "Aymara indigenous Chilean, Andean facial features from northern Chile, high-altitude adapted physique, distinctive indigenous nose shape",
            "Selknam Austral": "Selk'nam indigenous heritage, Patagonian facial features, strong jaw, robust build",
            "Rapa Nui Polinesio": "Rapa Nui Polynesian Chilean, Easter Island heritage, Polynesian facial features, broad nose, full lips",
            "Chileno Caucasico": "Chilean of full European descent, European facial features",
            "Afro-Chileno": "Afro-Chilean heritage, African diaspora facial features, broad nose, full lips",
            "Asiatico-Chileno": "Chilean of East Asian descent, Asian facial features, almond-shaped eyes",
            "Ascendencia Croata": "Chilean of Croatian descent from Magallanes region, Slavic facial features, defined cheekbones",
            "Ascendencia Palestina": "Chilean of Palestinian descent, Middle Eastern facial features, aquiline nose",
            "Ascendencia Alemana": "Chilean of German descent from Llanquihue region, Germanic facial features, strong jawline",
            "Ascendencia Italiana": "Chilean of Italian descent, Mediterranean facial features, expressive eyes, well-defined nose, balanced facial proportions",
            "Haitiano-Chileno": "Chilean of Haitian heritage, Afro-Caribbean facial features"
        }
        
        ethnicity_hair_texture = {
            "Mestizo Chileno Promedio": "straight to slightly wavy hair texture, typical latin american hair",
            "Mapuche Araucania": "straight thick hair texture, typical indigenous hair",
            "Aymara Andino": "straight coarse hair texture, typical Andean hair",
            "Selknam Austral": "straight hair texture",
            "Rapa Nui Polinesio": "thick wavy hair texture, Polynesian hair type",
            "Chileno Caucasico": "variable hair texture, European hair type",
            "Afro-Chileno": "coily hair texture, afro-textured hair type",
            "Asiatico-Chileno": "straight fine hair texture, East Asian hair type",
            "Ascendencia Croata": "straight to wavy hair texture, Slavic hair type",
            "Ascendencia Palestina": "straight to wavy hair texture, Middle Eastern hair type",
            "Ascendencia Alemana": "straight to wavy hair texture, Germanic hair type",
            "Ascendencia Italiana": "wavy to slightly curly hair texture, Mediterranean hair type",
            "Haitiano-Chileno": "coily hair texture, Afro-Caribbean hair type"
        }
        
        body_map = {
            "Promedio": "average body type",
            "Delgado": "slim build",
            "Atletico": "athletic build, toned muscles",
            "Curvy": "curvy build",
            "Voluminoso": "plus-size, full-figured",
            "Robusto": "stocky and muscular build",
            "Bajo y Compacto": "short and compact build",
            "Alto y Delgado": "tall and slender",
            "Sobrepeso": "overweight build, heavier body type",
            "Obesidad Morbida": "morbidly obese, very large body size, severe obesity"
        }
        
        face_map = {
            "Ovalada": "oval face shape",
            "Mandibula Cuadrada": "square jawline, defined facial structure",
            "Redonda": "round face shape",
            "Corazon": "heart-shaped face",
            "Alargada": "long face shape",
            "Triangular": "triangular face shape"
        }
        
        skin_map = {
            "Mate Claro": "fair matte skin tone",
            "Morena": "tan complexion",
            "Bronceada": "sun-kissed bronze skin",
            "Oliva": "olive skin tone",
            "Canela": "cinnamon brown skin",
            "Chocolate": "rich chocolate brown skin",
            "Marron Oscuro": "dark brown skin tone",
            "Negra Profunda": "deep ebony black skin",
            "Albino": "albinism condition, very pale porcelain white skin, complete lack of melanin pigmentation"
        }
        
        hair_style_map = {
            "Lacio Largo": "long straight hair",
            "Ondulado Suelto": "loose wavy hair",
            "Rizado Voluminoso": "voluminous curly hair",
            "Trenzas": "braided hair",
            "Afro Natural": "natural afro hair",
            "Rapado": "buzz cut",
            "Corto Texturizado": "short textured haircut",
            "Bob Corto": "short bob haircut",
            "Pixie": "pixie cut",
            "Cola de Caballo": "ponytail hairstyle",
            "Medio con Flequillo": "shoulder-length hair with bangs",
            "Dreadlocks": "dreadlocks hairstyle",
            "Fade Bajo": "low fade haircut",
            "Taper Fade": "taper fade haircut",
            "Undercut": "undercut hairstyle",
            "Slick Back": "slicked-back hair",
            "Quiff": "quiff hairstyle",
            "Mohawk": "mohawk haircut",
            "Wolf Cut": "wolf cut layered hairstyle",
            "Shag Desestructurado": "shaggy textured haircut"
        }
        
        hair_color_map = {
            "Negro Azulado": "blue-black hair, very dark hair with blue undertones",
            "Castano Oscuro": "dark brown hair",
            "Castano Claro": "light brown hair, chestnut colored",
            "Rubio Platinado": "platinum blonde hair, very light blonde",
            "Rojizo Cobre": "copper red hair, reddish-brown tone",
            "Gris Plateado": "silver grey hair, metallic grey tone",
            "Blanco Natural": "natural white hair, snow white",
            "Azul Electrico": "electric blue hair, vibrant blue colored",
            "Rosa Pastel": "pastel pink hair, soft pink tone",
            "Verde Neon": "neon green hair, bright fluorescent green",
            "Purpura Violeta": "purple violet hair, deep purple tone",
            "Naranja Fuego": "fire orange hair, bright orange tone",
            "Negro Azulado (Chileno)": "typical Chilean blue-black hair, natural dark tone common in Chile",
            "Castano Oscuro (Comun)": "common dark brown hair, most typical hair color",
            "Castano Claro (Tinte)": "light brown dyed hair, tinted chestnut color",
            "Rubio (Tenido)": "dyed blonde hair, bleached or colored blonde",
            "Rojizo (Tinte)": "dyed reddish hair, tinted red tone",
            "Gris (Natural)": "natural grey hair, aging grey color",
            "Blanco (Adulto Mayor)": "elderly white hair, senior grey-white hair",
            "Azul Electrico (Fantasia)": "fantasy electric blue hair, creative blue coloring",
            "Rosa Pastel (Fantasia)": "fantasy pastel pink hair, artistic pink coloring",
            "Verde Neon (Fantasia)": "fantasy neon green hair, creative bright green coloring"
        }
        
        vello_facial_map = {
            "Ninguno": None,
            "Barba corta": "short well-groomed beard, trimmed facial hair",
            "Barba larga": "long full beard, natural facial hair growth",
            "Bigote": "mustache, groomed upper lip facial hair",
            "Candado": "goatee beard style, chin beard with mustache, Van Dyke style",
            "Barba de 3 dias": "three-day stubble, short beard growth, unshaven look",
            "Patillas largas": "long sideburns, extended facial hair along jawline, mutton chops style",
            "Mosca": "soul patch, small tuft of hair below lower lip"
        }
        
        # NORMALIZAR VALORES (convierte EN->ES si es necesario)
        genero = normalize_value(genero)
        edad = normalize_value(edad)
        etnia_origen = normalize_value(etnia_origen)
        cuerpo = normalize_value(cuerpo)
        forma_cara = normalize_value(forma_cara)
        piel = normalize_value(piel)
        estilo_pelo = normalize_value(estilo_pelo)
        color_pelo = normalize_value(color_pelo)
        vello_facial = normalize_value(vello_facial)
        
        # DETECTAR SI ES ALBINO
        es_albino = (piel == "Albino")
        
        # ===== CONSTRUCCIÓN DEL PROMPT (SIEMPRE EN INGLÉS) =====
        parts = []
        
        # 1. BASE
        gender_desc = gender_map.get(genero, "person")
        age_desc = age_map.get(edad, "adult")
        parts.append(f"Full body portrait of a {age_desc} {gender_desc}, standing pose, entire body visible from head to feet")
        
        # 2. RASGOS FACIALES ÉTNICOS
        parts.append(ethnicity_facial_features.get(etnia_origen, "Chilean ethnicity"))
        
        # 3. CUERPO Y FORMA CARA
        parts.append(body_map.get(cuerpo, "average body type"))
        parts.append(face_map.get(forma_cara, "oval face shape"))
        
        # 4. PIEL
        parts.append(skin_map.get(piel, "medium skin tone"))
        
        # 5. PELO
        if es_albino:
            parts.append(hair_style_map.get(estilo_pelo, "shoulder-length hair"))
            parts.append(ethnicity_hair_texture.get(etnia_origen, "typical hair texture"))
            parts.append("snow white hair color due to albinism, very light colored hair lacking pigmentation")
        else:
            parts.append(hair_style_map.get(estilo_pelo, "shoulder-length hair"))
            parts.append(hair_color_map.get(color_pelo, "dark brown hair"))
        
        # 5.5. VELLO FACIAL
        vello_desc = vello_facial_map.get(vello_facial)
        if vello_desc:
            parts.append(vello_desc)
        
        # 6. OJOS
        if es_albino:
            parts.append("very light blue or pale grey eyes, photosensitive eyes typical of albinism")
        
        # 7. ROPA Y LOGO YUTRO
        is_child = edad == "Nino 8-12"
        
        if is_child:
            parts.append("wearing plain grey t-shirt and grey shorts, minimal clothing, non-sexual context, full body anatomical reference")
        else:
            if genero in ["Hombre Cis", "Hombre Trans"]:
                parts.append("wearing plain grey boxer briefs with 'YUTRO' brand text on elastic waistband, small logo visible on waistband, men's underwear, minimal clothing, non-sexual context, anatomical study")
            elif genero in ["Mujer Cis", "Mujer Trans"]:
                parts.append("wearing plain grey sports bra with 'YUTRO' brand logo on elastic underband, small logo visible on bra band, and plain grey briefs without logos, women's athletic underwear, minimal clothing, non-sexual context, anatomical study")
            else:
                parts.append("wearing plain grey sports bra or boxer briefs with 'YUTRO' text on elastic band, neutral undergarments, minimal clothing, non-sexual context, anatomical study")
        
        # 8. FONDO Y CALIDAD
        parts.append("Plain grey studio background with soft even lighting")
        parts.append("High quality portrait photography, professional lighting, sharp focus, realistic skin texture, anatomical accuracy")
        
        # PROMPT FINAL
        final_prompt = ". ".join(parts) + "."
        
        return (final_prompt,)


# ===== VERSIÓN EN ESPAÑOL =====
class YutroIDGenerator_ES(YutroIDGeneratorBase):
    """
    Versión en ESPAÑOL del generador Yutro ID
    Todas las opciones de interfaz en español
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "genero": ([
                    "Mujer Cis",
                    "Hombre Cis",
                    "No Binario",
                    "Mujer Trans",
                    "Hombre Trans",
                    "Agenero",
                    "Fluido"
                ],),
                "edad": ([
                    "Nino 8-12",
                    "Adolescente 13-17",
                    "Joven 18-24",
                    "Adulto Joven 25-34",
                    "Adulto Maduro 35-49",
                    "Adulto Mayor 50-64",
                    "Tercera Edad 65-79",
                    "Anciano 80plus"
                ],),
                "etnia_origen": ([
                    "Mestizo Chileno Promedio",
                    "Mapuche Araucania",
                    "Aymara Andino",
                    "Selknam Austral",
                    "Rapa Nui Polinesio",
                    "Chileno Caucasico",
                    "Afro-Chileno",
                    "Asiatico-Chileno",
                    "Ascendencia Croata",
                    "Ascendencia Palestina",
                    "Ascendencia Alemana",
                    "Ascendencia Italiana",
                    "Haitiano-Chileno"
                ],),
                "cuerpo": ([
                    "Promedio",
                    "Delgado",
                    "Atletico",
                    "Curvy",
                    "Voluminoso",
                    "Robusto",
                    "Bajo y Compacto",
                    "Alto y Delgado",
                    "Sobrepeso",
                    "Obesidad Morbida"
                ],),
                "forma_cara": ([
                    "Ovalada",
                    "Mandibula Cuadrada",
                    "Redonda",
                    "Corazon",
                    "Alargada",
                    "Triangular"
                ],),
                "piel": ([
                    "Mate Claro",
                    "Morena",
                    "Bronceada",
                    "Oliva",
                    "Canela",
                    "Chocolate",
                    "Marron Oscuro",
                    "Negra Profunda",
                    "Albino"
                ],),
                "estilo_pelo": ([
                    "Lacio Largo",
                    "Ondulado Suelto",
                    "Rizado Voluminoso",
                    "Trenzas",
                    "Afro Natural",
                    "Rapado",
                    "Corto Texturizado",
                    "Bob Corto",
                    "Pixie",
                    "Cola de Caballo",
                    "Medio con Flequillo",
                    "Dreadlocks",
                    "Fade Bajo",
                    "Taper Fade",
                    "Undercut",
                    "Slick Back",
                    "Quiff",
                    "Mohawk",
                    "Wolf Cut",
                    "Shag Desestructurado"
                ],),
                "color_pelo": ([
                    "Negro Azulado",
                    "Castano Oscuro",
                    "Castano Claro",
                    "Rubio Platinado",
                    "Rojizo Cobre",
                    "Gris Plateado",
                    "Blanco Natural",
                    "Azul Electrico",
                    "Rosa Pastel",
                    "Verde Neon",
                    "Purpura Violeta",
                    "Naranja Fuego",
                    "Negro Azulado (Chileno)",
                    "Castano Oscuro (Comun)",
                    "Castano Claro (Tinte)",
                    "Rubio (Tenido)",
                    "Rojizo (Tinte)",
                    "Gris (Natural)",
                    "Blanco (Adulto Mayor)",
                    "Azul Electrico (Fantasia)",
                    "Rosa Pastel (Fantasia)",
                    "Verde Neon (Fantasia)"
                ],),
                "vello_facial": ([
                    "Ninguno",
                    "Barba corta",
                    "Barba larga",
                    "Bigote",
                    "Candado",
                    "Barba de 3 dias",
                    "Patillas largas",
                    "Mosca"
                ],),
            }
        }


# ===== VERSIÓN EN INGLÉS =====
class YutroIDGenerator_EN(YutroIDGeneratorBase):
    """
    Versión en INGLÉS del generador Yutro ID
    Todas las opciones de interfaz en inglés
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "gender": ([  # 🔧 CORREGIDO: "genero" -> "gender"
                    "Cis Woman",
                    "Cis Man",
                    "Non-Binary",
                    "Trans Woman",
                    "Trans Man",
                    "Agender",
                    "Genderfluid"
                ],),
                "age": ([  # 🔧 CORREGIDO: "edad" -> "age"
                    "Child 8-12",
                    "Teen 13-17",
                    "Young Adult 18-24",
                    "Young Adult 25-34",
                    "Mature Adult 35-49",
                    "Middle-Aged 50-64",
                    "Senior 65-79",
                    "Elderly 80+"
                ],),
                "ethnicity": ([  # 🔧 CORREGIDO: "etnia_origen" -> "ethnicity"
                    "Chilean Mestizo",
                    "Mapuche Indigenous",
                    "Aymara Andean",
                    "Selknam Patagonian",
                    "Rapa Nui Polynesian",
                    "Chilean Caucasian",
                    "Afro-Chilean",
                    "Asian-Chilean",
                    "Croatian Descent",
                    "Palestinian Descent",
                    "German Descent",
                    "Italian Descent",
                    "Haitian-Chilean"
                ],),
                "body_type": ([  # 🔧 CORREGIDO: "cuerpo" -> "body_type"
                    "Average",
                    "Slim",
                    "Athletic",
                    "Curvy",
                    "Voluptuous",
                    "Stocky",
                    "Short & Compact",
                    "Tall & Slender",
                    "Overweight",
                    "Morbidly Obese"
                ],),
                "face_shape": ([  # 🔧 CORREGIDO: "forma_cara" -> "face_shape"
                    "Oval",
                    "Square Jaw",
                    "Round",
                    "Heart",
                    "Long",
                    "Triangular"
                ],),
                "skin_tone": ([  # 🔧 CORREGIDO: "piel" -> "skin_tone"
                    "Fair Matte",
                    "Tan",
                    "Bronze",
                    "Olive",
                    "Cinnamon",
                    "Chocolate",
                    "Dark Brown",
                    "Deep Black",
                    "Albino"
                ],),
                "hair_style": ([  # 🔧 CORREGIDO: "estilo_pelo" -> "hair_style"
                    "Long Straight",
                    "Loose Wavy",
                    "Voluminous Curly",
                    "Braids",
                    "Natural Afro",
                    "Buzz Cut",
                    "Short Textured",
                    "Short Bob",
                    "Pixie Cut",
                    "Ponytail",
                    "Shoulder with Bangs",
                    "Dreadlocks",
                    "Low Fade",
                    "Taper Fade",
                    "Undercut",
                    "Slick Back",
                    "Quiff",
                    "Mohawk",
                    "Wolf Cut",
                    "Shaggy Cut"
                ],),
                "hair_color": ([  # 🔧 CORREGIDO: "color_pelo" -> "hair_color"
                    "Blue-Black",
                    "Dark Brown",
                    "Light Brown",
                    "Platinum Blonde",
                    "Copper Red",
                    "Silver Grey",
                    "Natural White",
                    "Electric Blue",
                    "Pastel Pink",
                    "Neon Green",
                    "Purple Violet",
                    "Fire Orange",
                    "Blue-Black (Chilean)",
                    "Dark Brown (Common)",
                    "Light Brown (Dyed)",
                    "Blonde (Dyed)",
                    "Reddish (Dyed)",
                    "Grey (Natural)",
                    "White (Elderly)",
                    "Electric Blue (Fantasy)",
                    "Pastel Pink (Fantasy)",
                    "Neon Green (Fantasy)"
                ],),
                "facial_hair": ([  # 🔧 CORREGIDO: "vello_facial" -> "facial_hair"
                    "None",
                    "Short Beard",
                    "Long Beard",
                    "Mustache",
                    "Goatee",
                    "Stubble",
                    "Long Sideburns",
                    "Soul Patch"
                ],),
            }
        }


# ===== REGISTRO DE AMBOS NODOS =====
NODE_CLASS_MAPPINGS = {
    "YutroIDGenerator_ES": YutroIDGenerator_ES,
    "YutroIDGenerator_EN": YutroIDGenerator_EN
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "YutroIDGenerator_ES": "Yutro ID Generator 🇨🇱 (ES) v3.3.1",
    "YutroIDGenerator_EN": "Yutro ID Generator 🇨🇱 (EN) v3.3.1"
}
