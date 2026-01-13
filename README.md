# Whistleblower AI Report System 🛡️

A microservice developed in Django REST Framework for the automatic generation of anonymous complaint reports using generative artificial intelligence.

## 🚀 Features
* **AI Integration:** Utilizes the `llama-3.3-70b-versatile` model from Groq for ultra-fast natural language processing.
* **Security:** Implementation of **Token** authentication to protect endpoints.
* **Clean Architecture:** Separation of concerns using a service layer (`services.py`) and data validation.
* **Resilience:** Handling of quota errors (HTTP 429) and AI provider failures.

---

## 🛠️ Prerequisites
* Python 3.10+
* Virtualenv
* **Groq Cloud** API Key https://console.groq.com/keys

---

## 📥 Installation
1. **Clone the repository:**
   ```Bash
   git clone https://github.com/er-contreras/whistleblower
   cd whistleblower
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

2. **Generate Report (Protected)**

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

## 📝 License
This project is for technical evaluation purposes.
This project is [MIT](./LICENCE.md) licensed.

