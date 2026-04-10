# HardwareHandoff - Hardware Repair Dispatch System

[![FastAPI](https://img.shields.io/badge/FastAPI-0.115-brightgreen)](https://fastapi.tiangolo.com)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.39-blue)](https://streamlit.io)

## Objective
Automated hardware repair ticket assignment using skill matching, queue management, and location awareness. Cuts manual dispatch from 5min → 10sec.

## Quick Start
```bash
pip install -r requirements.txt
python data/seed_data.py
uvicorn app.main:app --reload    # http://localhost:8000/docs
streamlit run dashboard/app.py   # http://localhost:8501
```

## Results


## Tech Stack
FastAPI • SQLAlchemy • SQLite • Streamlit • Pandas