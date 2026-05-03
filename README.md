# Clinical Multi-Drug Scheduling & Conflict Detection System

## 🚀 Overview

This project is a backend system that generates realistic medication schedules for patients taking multiple drugs, while detecting potential conflicts in timing and dosage clustering.

It simulates real-world hospital prescription workflows by combining time-based scheduling with safety-aware conflict detection.

---

## 🧠 Problem

Patients are often prescribed multiple medications with different dosing frequencies (e.g., BD, TDS, QID).

In practice, this leads to:

* Overlapping medication times
* Doses scheduled too close together
* Poorly distributed regimens that reduce adherence

Most simple systems generate schedules but **do not evaluate their safety or practicality**.

---

##  Solution

This system:

* Generates **exact time-based schedules** using medically consistent intervals
* Supports **multi-drug prescriptions**
* Merges schedules into a **single patient timeline**
* Detects:

  * ⏱️ Time proximity conflicts
  * 💊 Drug overload at a single time
* Uses **risk-tier abstraction** to handle unknown drugs safely without requiring a full drug database

---

## ⚙️ Features

* FastAPI-based REST API
* Frequency-based scheduling (OD, BD, TDS, QID)
* Multi-day prescription support
* Multi-drug schedule merging
* Conflict detection engine:

  * Time proximity analysis
  * Overload detection
* Extensible design (ready for ML or drug APIs)

---

##  Example

### Input

```json
{
  "drugs": [
    { "name": "Amoxicillin", "frequency": "TDS" },
    { "name": "Paracetamol", "frequency": "QID" },
    { "name": "Ibuprofen", "frequency": "BD" }
  ],
  "days": 2,
  "start_hour": 8
}
```

### Output (excerpt)

```json
{
  "time": "08:00",
  "drugs": ["Amoxicillin", "Paracetamol", "Ibuprofen"]
}
```

---

## ⚠️ Conflict Detection

The system flags:

* Doses scheduled too close together
* Excessive number of drugs at a single time

Conflicts are **advisory**, not enforced—allowing flexibility for real-world clinical judgment.

---

## 🌐 Live Demo

👉 https://your-app.onrender.com/docs

---

##  Tech Stack

* Python
* FastAPI
* Uvicorn

---

## Future Improvements

* Integration with real drug interaction databases (e.g., RxNorm, OpenFDA)
* ML-based schedule optimization
* Patient-specific personalization
* Frontend visualization dashboard

---

## 👤 Author

austine steve

---

## 📌 Notes

This project is designed as a **clinical decision-support prototype**, not a replacement for professional medical systems.
