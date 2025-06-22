# Patrones de Diseño Estructurales

Este proyecto contiene ejemplos en Python de los patrones de diseño estructurales más representativos. Cada patrón tiene una implementación propia con una ejecución demostrativa.

## 🧰 Requisitos

- Tener un entorno de ejecución Python o
- Tener Docker y Docker Compose instalados.

## ▶️ Cómo ejecutar

Con Python:

Desde una consola (powershell, terminal, etc), moverse dentro del directorio app y ejecutar el main.

```bash
cd app
python main.py
```

Con Docker:

Desde la raíz del proyecto, corré:

```bash
docker-compose up --build
```

Se ejecutarán los ejemplos en orden desde el archivo `main.py`.

---

## 📦 Estructura

```
.
├── Dockerfile
├── docker-compose.yml
└── app/
    ├── main.py
    ├── patron_decorator/
    ├── patron_adapter/
    ├── patron_composite/
    └── patron_facade/
```

---

## 📘 Patrones incluidos

### 🎨 Decorator

- Permite añadir funcionalidades a objetos de forma dinámica.
- Ejemplo: agregar Moka o Pimienta a un `CafeSolo`.
- Ruta: `patron_decorator/`

### 🔌 Adapter

- Permite que clases incompatibles trabajen juntas usando un adaptador.
- Ejemplo: adaptar `Registro` a una interfaz `Filtrable` para usar en `Utilidad`.
- Ruta: `adapter/`

### 🧮 Composite

- Permite tratar objetos individuales y composiciones de objetos de manera uniforme.
- Ejemplo: representar expresiones matemáticas (números y operaciones) como un árbol.
- Ruta: `patron_composite/`

### 🧱 Facade

- Proporciona una interfaz simplificada a un conjunto de interfaces en un subsistema.
- Ejemplo: un `FacadePago` que simplifica la interacción con varios servicios de pago.
- Ruta: `patron_facade/`

---

## 🎯 Actividades sugeridas

1. **Decorator:** Agregá nuevos notificadores.
2. **Adapter:** Creá otro adaptador para un tipo de datos diferente (Ej: txt).
3. **Composite:** Agregá nuevos productos o creá nuevas cajas en el cliente.
4. **Facade:** Añadí un método de compresión específico si se trata de un video .mov o que mantenga el proceso actual si es cualquier otro.
