# Sistema de Recetas - Django

Un sistema web para gestionar recetas culinarias desarrollado con Django.

## 🚀 Características

- **Autenticación de usuarios**: Registro, login y logout
- **Gestión de recetas**: Crear, ver y listar recetas
- **Panel administrativo**: Interfaz Django Admin para gestión avanzada
- **Templates dinámicos**: Interfaz web responsive

## 📋 Requisitos

- Python 3.8+
- Django 5.2+

## 🛠️ Instalación

1. **Clonar el repositorio**

```bash
git clone https://github.com/MarceDokken/EV-PortafolioM6.git
cd EV-PortafolioM6
```

2. **Crear entorno virtual**

```bash
python -m venv venv
source venv/Scripts/activate
```

3. **Instalar dependencias**

```bash
pip install -r requirements.txt
```

4. **Configurar base de datos**

```bash
python manage.py migrate
```

5. **Crear superusuario**

```bash
python manage.py createsuperuser
```

6. **Ejecutar servidor**

```bash
python manage.py runserver
```

## 👤 Funcionalidades

- **Usuarios registrados**: Crear y ver recetas
- **Superusuarios**: Panel administrativo completo

## 🎯 URLs Principales

- / - Página de inicio
- /recetas/ - Lista todas las recetas
- /mis-recetas/ - Recetas del usuario
- /crear-receta/ - Crear nuevas recetas
- /registro/ - Registro de usuarios
- /login/ - Inicio de sesión
- /admin/ - Panel administrativo

## 🔧 Tecnologías

- Backend: Django 5.2
- Base de datos: SQLite3
- Frontend: HTML5, Django Templates
- Autenticación: Django Auth System

---

