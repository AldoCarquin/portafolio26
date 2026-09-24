# aldoaldoaldo.com — Portafolio Personal

> **Un portafolio que no se limita a mostrar trabajo: es, en sí mismo, la demostración de lo que hago.**

🌐 **Sitio web en vivo:** [www.aldoaldoaldo.com](https://www.aldoaldoaldo.com)  
👤 **Rol:** Diseño + Desarrollo  
🛠️ **Stack principal:** Python, Django, HTML, CSS, JavaScript, SVG  
🚀 **Estado:** En producción  

---

## 💡 La Premisa

Un portafolio de alguien que cruza diseño y desarrollo tiene un desafío particular: **contarlo no alcanza**. Si el sitio se ve bien pero corre sobre una plantilla comprada, o si está bien programado pero luce genérico, el argumento pierde fuerza.

Por eso este sitio es **la evidencia, no solo el catálogo**:
- **Sistema visual 100% original:** Formas orgánicas, tipografía en tensión y uso de color saturado con criterio.
- **Arquitectura real por detrás:** Sin plantillas ni constructores visuales. Todo lo que se ve está sostenido por modelos, vistas y plantillas escritas y administradas desde cero.

---

## 🛠️ Cómo está construido

- **Todo es un modelo:** Proyectos, experiencia laboral, educación, conocimientos, certificados y versiones del CV viven estructurados en la base de datos PostgreSQL/SQLite. Nada está fijado a mano en el HTML.
- **Sistema de Portales:** Cada caso de estudio se inyecta con su propio bloque de estilos aislado. El sitio funciona como un marco contenedor navegable, mientras que el universo visual del proyecto toma el control al abrirse.
- **Marco orgánico en SVG:** El borde deformado que envuelve cada proyecto no utiliza `border-radius` tradicional; se trata de un filtro SVG dinámico con turbulencia y desplazamiento que se adapta a cualquier altura de página.
- **Autoadministrable:** Cargar un proyecto nuevo, actualizar experiencia o modificar el CV se gestiona directamente desde el panel de administración de Django, sin necesidad de redeplegar código.

---

## 💻 Tech Stack & Herramientas

| Categoría | Tecnologías / Herramientas |
| :--- | :--- |
| **Backend** | Python, Django, Django Admin |
| **Frontend** | HTML5, CSS3, JavaScript (ES6+), SVG Filters |
| **Diseño y UI/UX** | Adobe Illustrator, Figma |

---

## 🧩 Modelo de Datos Destacado

Ejemplo del concepto de **Portales**, donde cada proyecto almacena su propio contenido y estilo dentro del modelo de datos:

```python
# El corazón del sistema de portales:
# cada proyecto trae su propio HTML y sus propios estilos.

class Proyecto(models.Model):
    titulo            = models.CharField(max_length=150)
    slug              = models.SlugField(unique=True)
    icono             = models.CharField(max_length=40)
    descripcion_corta = models.CharField(max_length=250)
    contenido_html    = models.TextField()  # ← El portal
