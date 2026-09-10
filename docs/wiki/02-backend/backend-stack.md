# 🔵 Module 02: Backend Engineering

This module explains the tools used to build the brain of BountyHunter.

## 1. FastAPI
FastAPI is a modern, high-performance web framework for building APIs with Python.
- **Asynchronous (`async`)**: Unlike old frameworks, FastAPI can handle other tasks while waiting for a database or API response. This is why our agents can search the web in the background without freezing the UI.
- **Type Hinting**: It uses Python's type hints to automatically generate documentation (Swagger UI).

## 2. Pydantic (The Validator)
Pydantic ensures that data entering the system is correct.
- **Schemas**: We define "Schemas" (e.g., `UserProfileCreate`). If a user sends a string where a number is expected, Pydantic catches it and returns a clear error message.

## 3. SQLAlchemy (The ORM)
ORM stands for **Object Relational Mapper**.
- **The Problem**: Databases speak SQL; Python speaks Objects.
- **The Solution**: SQLAlchemy lets us treat database rows as Python objects.
- **Session Management**: We use a `get_db` dependency to ensure every request gets its own database connection and closes it when finished.

## 4. PostgreSQL
A professional, relational database.
- **ACID Compliance**: Ensures that transactions are processed reliably (e.g., you won't lose data if the power goes out mid-update).
- **JSONB Support**: Allows us to store lists of skills and roles directly as JSON while still being able to query them.
