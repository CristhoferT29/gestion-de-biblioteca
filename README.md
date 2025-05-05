# 📚 Proyecto: Sistema de Gestión de Biblioteca (CLI)

Este proyecto es una aplicación de línea de comandos (CLI) desarrollada en Python para la gestión de una biblioteca. Permite realizar operaciones CRUD sobre libros, usuarios y préstamos, utilizando árboles binarios de búsqueda para mantener los datos ordenados y eficientes.

---

## ✨ Funcionalidades

- 📘 Gestión de Libros:
  - Agregar, consultar, buscar y eliminar libros.
  - Validación de campos únicos como título e ISBN.
  
- 👤 Gestión de Usuarios:
  - Registro, consulta y búsqueda por ID o nombre.
  
- 🔄 Gestión de Préstamos:
  - Asociar un libro a un usuario.
  - Verificar disponibilidad del libro y existencia del usuario.
  - Registro de préstamos activos.

- 💾 Persistencia de datos:
  - Uso de archivos `.json` para guardar y recuperar los datos automáticamente al cerrar y abrir la aplicación.

---

## 🛠 Tecnologías utilizadas

- Python `3.13.2`
- Árbol Binario de Búsqueda (ABB)
- Módulo `json` (para persistencia)
- Programación modular

---

## ⚙️ Estructura del proyecto
```
proyecto-sistema-biblioteca/
├── controllers/ # Lógica de control (libros, usuarios, préstamos)
├── models/ # Clases base y estructuras de datos (Libro, Usuario, Prestamo, ArbolBB)
├── utils/ # Funciones auxiliares (menús, validaciones, persistencia)
├── main.py # Punto de entrada del programa
├── README.md # Documentación del proyecto
└── .gitignore # Archivos ignorados por Git
```
## ▶️ Ejecución

Desde la raíz del proyecto, ejecuta:

```bash
python main.py
```

👨‍💻 Autor

Cristhofer Tibaquicha — Proyecto académico para la asignatura de estructuras de datos.