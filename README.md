# Bidx Backend

A high-performance, real-time auction and bidding backend built using FastAPI. This system enables secure, scalable, and real-time auction management with support for live bidding, user authentication, and concurrent bid processing.

Designed with production-grade architecture, this project demonstrates scalable backend design using modern Python technologies.

---

## Features

- Real-time bidding support
- Auction creation and management
- Secure user authentication
- Session-based authentication
- Concurrent bid handling
- RESTful API architecture
- Scalable service-layer design
- Database-integrated auction tracking
- Production-ready backend structure

---

## Tech Stack

**Backend**
- FastAPI
- Python 3.12+

**Database**
- PostgreSQL (based on configuration)

**Architecture**
- REST API
- Service Layer Pattern
- Dependency Injection
- Modular architecture

**Other Tools**
- SQLAlchemy (ORM)
- Pydantic (validation)
- Uvicorn (ASGI server)
---

## Installation

### 1. Clone repository
```bash
git clone https://github.com/RuteshPatel/bidx-backend.git
cd bidx-backend
```

### 2. Create a virtual environment
```bash
python -m venv venv
```
##### Activate virtual environment:
#### Mac/Linux
```bash
source venv/bin/activate
```
#### Windows
```bash
venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```
### 4. Run server
```bash
uvicorn main:app --reload
```



