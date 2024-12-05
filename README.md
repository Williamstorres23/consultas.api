
# Appointment Scheduling API 🩺

This is a **FastAPI** project for managing medical appointments. It provides basic CRUD functionality to handle patients, doctors, and their appointments. A great tool for learning and implementing FastAPI APIs.

---

## Features ✨

- 📋 List all appointments.
- 🔍 Retrieve an appointment by ID.
- ➕ Add a new appointment.
- ✏️ Update an existing appointment.
- ❌ Delete an appointment.

---

## Endpoints 🌐

### 1. **List All Appointments** 📋
**GET** `/consultas`

Retrieve the list of all scheduled appointments.

**Response:**
```json
[
  {
    "id": 1,
    "paciente": "João Silva",
    "medico": "Dra. Maria",
    "data": "2024-12-10",
    "horario": "10:00",
    "descricao": "Consulta de rotina"
  }
]
```

---

### 2. **Retrieve Appointment by ID** 🔍
**GET** `/consultas/{consulta_id}`

Retrieve the details of a specific appointment using its unique ID.

**Response (if found):**
```json
{
  "id": 1,
  "paciente": "João Silva",
  "medico": "Dra. Maria",
  "data": "2024-12-10",
  "horario": "10:00",
  "descricao": "Consulta de rotina"
}
```

---

### 3. **Add a New Appointment** ➕
**POST** `/consultas`

**Request Body:**
```json
{
  "paciente": "Ana Costa",
  "medico": "Dr. Carlos",
  "data": "2024-12-12",
  "horario": "14:30",
  "descricao": "Exames de acompanhamento"
}
```

**Response:**
```json
{
  "id": 3,
  "paciente": "Ana Costa",
  "medico": "Dr. Carlos",
  "data": "2024-12-12",
  "horario": "14:30",
  "descricao": "Exames de acompanhamento"
}
```

---

### 4. **Update an Appointment** ✏️
**PUT** `/consultas/{consulta_id}`

Update the details of an existing appointment using its ID.

**Request Body:**
```json
{
  "data": "2024-12-20",
  "horario": "15:00"
}
```

**Response:**
```json
{
  "id": 3,
  "paciente": "Ana Costa",
  "medico": "Dr. Carlos",
  "data": "2024-12-20",
  "horario": "15:00",
  "descricao": "Exames de acompanhamento"
}
```

---

### 5. **Delete an Appointment** ❌
**DELETE** `/consultas/{consulta_id}`

Delete an appointment using its ID.

**Response:**
```json
{
  "message": "Consulta 3 removida com sucesso"
}
```

---

## Environment Management ⚙️

Here are some useful Conda commands for managing your Python environment:

- **View created environments**:
  ```bash
  conda info --envs
  ```

- **Remove an environment**:
  ```bash
  conda env remove --name agendamento
  ```

- **Create a new environment**:
  ```bash
  conda create --name agendamento pip python=3.10
  ```

- **Activate an environment**:
  ```bash
  conda activate agendamento
  ```

- **Deactivate an environment**:
  ```bash
  conda deactivate
  ```

---

## How to Run 🚀

### Prerequisites

- 🐍 Python 3.9 or higher installed.
- 🛠 Required libraries: `fastapi`, `uvicorn`.

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repository-url.git
   cd your-repository
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Start the development server:
   ```bash
   uvicorn main:app --reload
   ```

4. Open your browser and navigate to:
   - API Docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) 📄
   - Redoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc) 📚

---

## License 📜

This project is licensed under the MIT License. Feel free to use and modify it.

---
