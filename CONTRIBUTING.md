# Guía de Contribución

¡Gracias por tu interés en contribuir al Glosario de Programación! 🎉

## 🤝 Cómo Contribuir

### 1. Fork del Repositorio
1. Haz clic en el botón "Fork" en la parte superior derecha
2. Clona tu fork: `git clone https://github.com/TU-USUARIO/glosario-desarrollo.git`

### 2. Configura tu Entorno
```bash
cd glosario-desarrollo
git remote add upstream https://github.com/spatiummeum/glosario-desarrollo.git
```

### 3. Crea una Nueva Rama
```bash
git checkout -b feature/nombre-del-termino
```

### 4. Formato para Nuevos Términos

Cada término debe seguir este formato exacto:

```markdown
### Nombre del Término (English Name)

**Definición:** Explicación clara y sencilla del concepto en 1-2 oraciones.

**Ejemplo:** Analogía o ejemplo práctico del mundo real que ayude a entender el concepto.

**Ejemplo en Código (Lenguaje):**

```lenguaje
// Código de ejemplo claro y bien comentado
const ejemplo = "que demuestre el concepto";
```

**Relación con [Lenguaje]:** (Si aplica) Cómo se relaciona específicamente con JavaScript, Python, etc.
```

### 5. Lineamientos de Contenido

#### ✅ Qué SÍ incluir:
- Definiciones claras y simples
- Ejemplos prácticos del mundo real
- Código funcional y bien comentado
- Explicaciones orientadas a principiantes
- Referencias a JavaScript, Python cuando sea relevante

#### ❌ Qué NO incluir:
- Definiciones técnicas complejas sin explicación simple
- Código sin comentarios
- Términos ya existentes (revisa primero)
- Contenido copiado de otras fuentes sin adaptación

### 6. Proceso de Review

1. **Auto-revisión**: Verifica que tu contribución sigue el formato
2. **Pull Request**: Abre un PR con descripción clara
3. **Review**: El equipo revisará tu contribución
4. **Merge**: Una vez aprobado, se integrará al proyecto

## 📍 Dónde Agregar Términos

Organiza los términos en la sección apropiada:

- **🏛️ Conceptos Fundamentales**: Algoritmo, Variable, Función, etc.
- **📦 POO**: Clase, Objeto, Herencia, Polimorfismo, etc.
- **🌐 Web y Redes**: HTML, CSS, API, HTTP, etc.
- **🖥️ Hardware**: CPU, RAM, Memoria, etc.
- **🧮 Tipos de Datos**: String, Integer, Boolean, etc.
- **✍️ Sintaxis**: Loops, Condicionales, Funciones, etc.
- **🐛 Errores**: Debugging, Exceptions, Testing, etc.

## 🎯 Tipos de Contribuciones Bienvenidas

### Nuevos Términos
- Conceptos fundamentales de programación
- Términos específicos de JavaScript/Python
- Conceptos de desarrollo web
- Herramientas de desarrollo

### Mejoras de Contenido
- Aclarar definiciones existentes
- Agregar mejores ejemplos
- Corregir errores
- Mejorar ejemplos de código

### Mejoras de Formato
- Corrección de enlaces
- Mejora de la organización
- Corrección de errores tipográficos

## 🏷️ Convenciones de Commit

Usa estos prefijos para tus commits:

- `feat: agrega término [NombreTermino]`
- `fix: corrige definición de [Término]`
- `docs: mejora documentación`
- `style: mejora formato`

## 📝 Plantilla de Pull Request

```markdown
## Descripción
Breve descripción de los cambios realizados.

## Tipo de cambio
- [ ] Nuevo término
- [ ] Mejora de término existente
- [ ] Corrección de error
- [ ] Mejora de documentación

## Checklist
- [ ] He seguido el formato establecido
- [ ] He verificado que el término no existe
- [ ] He incluido ejemplos claros
- [ ] He revisado la ortografía y gramática
```

## ❓ ¿Necesitas Ayuda?

- 📧 Abre un [Issue](https://github.com/spatiummeum/glosario-desarrollo/issues)
- 💬 Inicia una [Discusión](https://github.com/spatiummeum/glosario-desarrollo/discussions)
- 📖 Revisa la [Wiki](https://github.com/spatiummeum/glosario-desarrollo/wiki)

## 🙏 Reconocimiento

Todos los contribuidores serán reconocidos en:
- El README principal
- La sección de contributors de GitHub
- Nuestro hall of fame (próximamente)

¡Gracias por ayudar a hacer este glosario mejor para toda la comunidad! 🚀
