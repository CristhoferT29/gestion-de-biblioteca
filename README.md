# Proyecto: Sistema de Gestión de Biblioteca (CLI)

Este proyecto es una aplicación de línea de comandos (CLI) desarrollada en Python para la gestión de una biblioteca. Permite realizar operaciones CRUD (crear, leer, actualizar y eliminar) sobre libros almacenados en memoria.

---

## 📚 Funcionalidades

- Agregar libros
- Modificar libros
- Eliminar libros
- Consultar libros disponibles
- Validación de campos obligatorios y valores únicos (como el título o ISBN)

---

## 👨‍💼 Tecnologías utilizadas

- Python 3.13.2
- Programación estructurada y modular
- Entrada y salida por consola

---

## ⚖️ Estructura del proyecto

```
proyecto-biblioteca/
├── controllers/          # Acciones principales (CRUD)
├── models/               # Modelo en memoria (estructura de datos)
├── utils/                # Funciones reutilizables (menú, validación, etc)
├── main.py               # Punto de entrada del programa
└── .gitignore            # Archivos ignorados por Git
```

---

## ▶️ Ejecución

Ejecuta:

```bash
python main.py
```

---

## 🚀 Autor

Cristhofer Tibaquicha.

---

## ✍️ Notas adicionales

- Todos los datos se almacenan temporalmente en memoria (no hay persistencia en disco).
- Este proyecto fue desarrollado como parte de un trabajo universitario sobre estructuras de datos lineales.