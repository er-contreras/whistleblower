# Whistleblower AI Report System 🛡️

Microservicio desarrollado en **Django REST Framework** para la generación automática de reportes de denuncias anónimas utilizando inteligencia artificial generativa.

## 🚀 Características
* **Integración con IA:** Utiliza el modelo `llama-3.3-70b-versatile` de **Groq** para procesamiento ultra-rápido de lenguaje natural.
* **Seguridad:** Implementación de autenticación vía **Token** para proteger los endpoints.
* **Arquitectura Limpia:** Separación de responsabilidades mediante una capa de servicios (`services.py`) y validación de datos.
* **Resiliencia:** Manejo de errores de cuota (HTTP 429) y fallos del proveedor de IA.

---

## 🛠️ Requisitos Previos
* Python 3.10+
* Virtualenv
* API Key de **Groq Cloud**

---

## 📥 Instalación

1. **Clonar el repositorio:**
   ```bash
   git clone 
   cd whistleblower-ai
   ```

2. **Set up a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Environment variables:** Create a ```.env``` file in the root directory:
    ```bash
    GROQ_API_KEY=<groq-api-key>
    ```

5. **Run Migrations & Create Superuser:**
    ```bash
    python manage.py migrate
    python manage.py createsuperuser
    ```

6. **Start the server:**
    ```bash
    python manage.py runserver
    ```

## 🚦 API Usage
1. **Authentication**

Endpoint: ```POST /api-token-auth/```

Payload:

JSON

```json
{
    "username": "your_admin",
    "password": "your_password"
}
```

## 2. Generate Report (Protected)

Endpoint: ```POST /api/report/```

Header: Authorization: Bearer <your_access_token>

Payload:

JSON

```json
{
    "victim_name": "Carlos López",
    "classification": "fraud"
}
```

📝 License
This project is for technical evaluation purposes.
