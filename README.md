# DesarrollaGT — sitio web

Sitio público de DesarrollaGT, publicado con GitHub Pages en
<https://sm2002-ai.github.io/desarrollagt/>. Todo es HTML estático: no hay que compilar nada.
Cada cambio que llega a la rama `main` se publica solo en 1–2 minutos.

## Estructura

| Archivo | Para qué sirve |
|---|---|
| `index.html` | Página principal: propuesta, funcionalidades, cómo empezar, comparación, planes y preguntas frecuentes |
| `calculadora-hipotecaria/index.html` | Calculadora gratuita de cuota hipotecaria (banco y Mi Primera Casa) con tablas y guía |
| `mercado-inmobiliario-guatemala/index.html` | Indicadores del mercado (tasa líder, inflación, remesas, PIB, crédito) con fuentes |
| `404.html` | Página de error con enlaces a las secciones principales |
| `assets/sitio.css`, `assets/sitio.js` | Estilos y scripts compartidos por todas las páginas |
| `assets/fuentes/` | Fuentes Playfair Display y DM Sans autoalojadas (licencia SIL OFL, incluida) |
| `assets/og-desarrollagt.jpg` | Imagen que aparece al compartir el enlace en WhatsApp, LinkedIn o X |
| `sitemap.xml` | Lista de páginas para Google y Bing |
| `llms.txt` | Resumen del sitio en texto plano para asistentes de IA |
| `robots.txt` | Reglas para buscadores (solo surte efecto con dominio propio, ver abajo) |
| `8f505853f4db0f550df4f5b6fd1491f1.txt` | Clave de IndexNow (no borrar) |
| `_herramientas/indexnow.py` | Avisa a Bing de los cambios (la carpeta con `_` no se publica) |

## Cómo actualizar las cifras

Las cifras del mercado aparecen en tres lugares y deben cambiarse juntas:

1. `index.html`, sección **Pulso del mercado** (4 tarjetas) y la fecha del pie de página.
2. `mercado-inmobiliario-guatemala/index.html`: tabla de indicadores, gráfica y tabla de remesas,
   análisis, preguntas frecuentes y el bloque `application/ld+json` del encabezado (sus respuestas
   deben decir exactamente lo mismo que las preguntas visibles).
3. `llms.txt` y la fecha `lastmod` de `sitemap.xml`.

Cuándo salen los datos: inflación (INE) alrededor del día 7 de cada mes; remesas (Banguat) en la
primera semana del mes; tasa líder según el calendario de la Junta Monetaria.

Si cambian las condiciones de Mi Primera Casa, actualice las constantes `MPC_TOPE_5` y `MPC_TOPE_55`
al final de `calculadora-hipotecaria/index.html` y las tablas de esa página.

## Lista de tareas para más impresiones y clics

Estas tareas requieren sus cuentas y no se pueden hacer desde el código:

1. **Google Search Console.** Agregue una propiedad de tipo *prefijo de URL* con
   `https://sm2002-ai.github.io/desarrollagt/`, verifíquela con el método de archivo HTML
   (suba ese archivo a la raíz de este repositorio), envíe `sitemap.xml` y pida la indexación de
   las tres páginas con la herramienta de inspección de URL.
2. **Bing Webmaster Tools.** Importe el sitio desde Search Console y envíe `sitemap.xml`.
   Bing alimenta a Copilot y es una de las fuentes de la búsqueda de ChatGPT.
3. **IndexNow.** Después de cada publicación ejecute `python _herramientas/indexnow.py`.
4. **Medición.** Agregue Google Analytics 4 o GoatCounter pegando su fragmento antes de `</head>`
   en cada página. Los botones de WhatsApp ya envían el evento `click_whatsapp` con su origen
   (`hero`, `plan-pro`, `calculadora-resultado`, etc.), así sabrá qué botón genera conversaciones.
   Cada botón también abre WhatsApp con un mensaje distinto, lo que permite identificar el origen
   aunque no haya analítica.
5. **Dominio propio (recomendado).** Un dominio como `desarrollagt.com` concentra la autoridad en
   su marca y permite que `robots.txt` y `llms.txt` queden en la raíz, donde los buscadores los
   leen. Pasos: comprar el dominio, crear un archivo `CNAME` con el dominio, configurar el DNS según
   la guía de GitHub Pages, activar HTTPS y reemplazar las URLs:

   ```bash
   grep -rl "sm2002-ai.github.io/desarrollagt" --include="*.html" --include="*.xml" --include="*.txt" --include="*.py" . \
     | xargs sed -i 's#https://sm2002-ai.github.io/desarrollagt/#https://desarrollagt.com/#g; s#sm2002-ai.github.io/desarrollagt#desarrollagt.com#g'
   sed -i 's#/desarrollagt/#/#g' 404.html
   ```

6. **Presencia fuera del sitio.** Los asistentes de IA citan más a las marcas que aparecen en otros
   sitios: perfil de empresa en LinkedIn, publicaciones en X (Grok busca en X y en la web),
   menciones en medios y asociaciones del sector, y enlaces desde sitios de aliados.
7. **Más páginas con datos propios.** Lo que más impresiones genera son páginas por zona
   (por ejemplo, precio por m² en zona 10 o zona 15) construidas con los datos de la plataforma.

## Notas técnicas

- El contenido está en el HTML (no se genera con JavaScript), así lo pueden leer Google, Bing y los
  rastreadores de IA. JavaScript solo controla el menú móvil, la calculadora y el tooltip de la gráfica.
- Cada página incluye datos estructurados (schema.org) en `application/ld+json`.
- `404.html` usa rutas que empiezan con `/desarrollagt/` porque se muestra en cualquier ruta.
