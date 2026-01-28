# 🚀 Pydantic Learning

Hands-on **Pydantic examples and learning notes** focused on Python data validation, type safety, and real-world backend use cases.

---

## 📌 What This Repo Covers

✔️ Pydantic `BaseModel` basics  
✔️ Field types, defaults, and optional values  
✔️ Data validation & parsing  
✔️ Nested models  
✔️ Date & time handling  
✔️ Practical patterns used in APIs (FastAPI-ready)

---

## 🤔 Why Pydantic?

Pydantic makes Python code **safer, cleaner, and more predictable** by validating data using standard type hints.

It is widely used in:
- FastAPI
- Backend services
- Configuration management
- Data pipelines

---

## 🧠 Quick Example

```python
from pydantic import BaseModel
from datetime import datetime

class User(BaseModel):
    id: int
    name: str
    is_active: bool = True
    created_at: datetime

user = User(
    id=1,
    name="Ritik Sharma",
    created_at="2025-01-01T10:00:00"
)

print(user)
