# Prompts de los esquemas de la sesión 12

Esquemas generados con la herramienta integrada de imágenes para la clase del 4 de noviembre de 2026. Las copias se exportan como JPEG de 1100 píxeles de ancho y calidad 84, conservando los originales.

## Especificación inicial del flujo de pruebas

```text
Use case: scientific-educational.
Asset type: one compact Spanish teaching sketch for CyberColombia, wide landscape 2:1, intended to be reduced to 1100 px and embedded in repository README and classroom guide.
Primary request: Explain how a change in LibreReserva becomes a tested, identifiable container image. Title exactly "Del cambio a una imagen verificable". Six clear small hand-drawn scenes in two close rows of three, connected in reading order. Row one left to right: laptop with code and label "Cambio"; git branching symbol with label "Commit"; checklist with label "Pruebas en CI". Row two reading left to right: build tools with label "Construcción"; software package with label "Imagen OCI"; small evidence document with label "Commit + ID de imagen". The connection goes from top right down to bottom left, unobstructed. At "Pruebas en CI" one short side branch to a small stop symbol with label exactly "Si fallan, se detiene"; main successful branch to "Construcción" labelled "Si pasan". Final small bottom caption exactly "Aunque las pruebas pasen, debemos saber qué comprobaron."
Technical constraints: tests precede image construction. Image here is built and archived as artifact, no registry publication or deployment shown. The commit appears in evidence and tags as a reference, the image ID identifies the local image artifact. Do not imply passing tests proves all features or that commit alone guarantees a byte-identical rebuild.
Style: friendly lightweight hand-drawn ink sketch, dark blue lines, sparse cyan and purple accents matching CyberColombia palette, pure white background, readable large Spanish letters, no photorealism, no 3D, no logos. Balanced tight crop, very little white padding above/below, no decorative border, no empty bands, no small paragraphs, no watermark.
```

## Consulta parametrizada

```text
Use case: scientific-educational.
Asset type: compact Spanish classroom sketch, landscape 2:1, reduce to 1100px, CyberColombia educational style.
Title exactly "Una entrada debe seguir siendo un dato".
Explain SQL injection and parameterized queries using a reservation search. Two close horizontal rows, each with three hand-drawn scenes connected left-to-right. Top row labels: "Entrada", "Consulta concatenada", "Devuelve otras reservas". Under the entry icon show the exact literal text "' OR '1'='1" clearly. Middle top show two strips of text being mixed into a single query, with warning accent. Right show a database returning two small reservation cards marked "A-101" and "B-202".
Bottom row labels: "Misma entrada", "Consulta parametrizada", "Sin coincidencias". Entry is same input. Middle show a SQL instruction sheet and a distinct value tag, deliberately separated with a clear thin divider, both going toward a database. Right show an empty result tray with a zero. Bottom caption exactly "Aunque la entrada parezca SQL, debe tratarse como un valor." Explain with visuals that this exact input matches no room in the small fictitious dataset, not that parameterization always yields empty results.
Style clean lightweight hand-drawn ink sketch with dark blue, cyan/purple sparse accents, pure white background. Large legible Spanish labels and accents. Very tightly balanced crop with minimal top/bottom whitespace, no paper texture, no logos, no hackers, no photorealism, no extra text or paragraphs. Do not suggest that parameterization handles authorization.
```

## Corrección intermedia de las etiquetas SQL

```text
Use case: precise-object-edit.
Edit target: supplied teaching sketch "Una entrada debe seguir siendo un dato".
Correct ONLY SQL code labels to match the actual LibreReserva classroom example and be syntactically accurate.
1. In the top left SQL sheet replace all text with exactly: "SELECT id, recurso" newline "FROM reservas" newline "WHERE recurso = '"
2. In the red outlined SQL sheet replace all SQL text with exactly: "SELECT id, recurso" newline "FROM reservas" newline "WHERE recurso = ''" newline "OR '1'='1'" . It must have TWO consecutive single quotes after recurso =, representing an empty string, and a final closing quote after the final 1. This red sheet is the FULL concatenated query, no extra separate fragment is required inside it.
3. In the bottom SQL sheet replace text with exactly: "SELECT id, recurso" newline "FROM reservas" newline "WHERE recurso = ?" .
The input tags and laptop screens must display exactly "' OR '1'='1" (one opening quote before OR, quotes around first 1, one opening quote before last 1, no trailing quote after that last 1 in the input value). This input plus the original query's trailing quote forms the red full query above.
Preserve title, all other Spanish labels and caption, two rows, arrows, database icons, A-101/B-202 fictitious records, empty tray, white background, colors, sketch style, compact crop and layout. No new elements, no blank bands, no logos. Ensure code labels use recurso, never habitacion. SQL text must be readable at 1100px overall width.
```

## Edición final con etiquetas conceptuales

```text
Use case: precise-object-edit.
Edit target: the supplied sketch diagram "Una entrada debe seguir siendo un dato".
Simplify ONLY the three SQL instruction sheets into CONCEPT labels, removing code strings and their quote punctuation. This is to keep the diagram conceptual; exact SQL code belongs in accompanying editable teaching text.
Top white instruction sheet: replace all current SQL code with exactly two lines: "Consulta SQL" / "Filtro por recurso".
Top RED outlined sheet: replace all current SQL code with exactly two lines: "La entrada" / "cambia el filtro".
Bottom white instruction sheet: replace all current SQL code with exactly three lines: "Consulta SQL" / "Filtro por recurso" / "Parámetro: ?".
Preserve EVERYTHING else, including all laptop inputs and value tags, Spanish labels, title, caption, arrows, the two rows, warning mark, A-101 and B-202 records, empty result, white background, sketch style and colors, same tight crop. No other changes. Do not put any SQL code in these three sheets. Do not add elements, blank space or borders. Make replacement labels clearly legible at 1100px overall width.
```

Archivos: `pruebas-entrega-trazable.jpg` y `consulta-parametrizada.jpg`. El primer dibujo conserva la secuencia y utiliza ahora el título «Pruebas y construcción de la imagen», según la edición documentada en [las especificaciones actuales](PROMPTS_SESION12_V3.json). La segunda imagen utiliza etiquetas conceptuales; el SQL exacto se conserva como texto editable en la guía y en el ejemplo ejecutable. Los prompts anteriores registran la generación inicial.
