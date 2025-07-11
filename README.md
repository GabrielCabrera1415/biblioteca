# biblioteca
Este es un proyecto hecho en Python para gestionar libros en una biblioteca. Incluye el uso de **programación orientada a objetos (POO)** y **herencia** entre clases, ideal para practicar conceptos intermedios.

---

## 🚀 ¿Qué puede hacer?

- Agregar libros físicos o digitales
- Mostrar todos los libros
- Buscar libros por título
- Prestar y devolver libros físicos
- Mostrar libros disponibles

---

## 🧱 Clases usadas

- `Libro` → clase base (título, autor, año, disponibilidad)
- `LibroFisico` → hereda de `Libro`, incluye `ubicacion_estante`
- `LibroDigital` → hereda de `Libro`, incluye `formato`

---

## 🖥️ Ejecución

```bash
python biblioteca.py
