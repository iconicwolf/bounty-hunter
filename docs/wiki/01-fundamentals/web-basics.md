# 🟢 Module 01: Web Fundamentals

This module covers the absolute basics of how the internet and web applications communicate.

## 1. The Client-Server Model
The web operates on a simple request-response cycle.
- **The Client**: Your browser (e.g., Chrome). It sends a **Request**.
- **The Server**: A computer somewhere (e.g., our FastAPI app). It sends a **Response**.

## 2. HTTP (HyperText Transfer Protocol)
HTTP is the language the client and server use to speak.
- **Methods**:
  - `GET`: "Give me some data" (Read).
  - `POST`: "Here is some new data, create it" (Create).
  - `PUT`: "Update this existing data" (Update).
  - `DELETE`: "Remove this data" (Delete).
- **Status Codes**:
  - `200 OK`: Success.
  - `201 Created`: Resource successfully created.
  - `400 Bad Request`: Client sent something wrong.
  - `404 Not Found`: Resource doesn't exist.
  - `500 Internal Server Error`: The server crashed.

## 3. JSON (JavaScript Object Notation)
JSON is the universal format for moving data. It looks like a Python dictionary.
```json
{
  "full_name": "John Doe",
  "skills": ["Python", "FastAPI"]
}
```

## 4. REST APIs
REST is a set of rules for building APIs. A RESTful API uses standard HTTP methods and unique URLs (endpoints) to manage resources (like `/profile` or `/applications`).
