import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import random
from faker import Faker
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Technician, Ticket, Assignment

fake = Faker()

def seed_technicians(db: Session):
    cert_options = [
        ['A+', 'Network+'],
        ['ACSP'],
        ['A+', 'Micro-soldering'],
        ['Network+', 'Security+'],
        ['A+'],
        ['Micro-soldering', 'Hardware'],
        ['Network+'],
        ['ACSP', 'A+']
    ]
    
    tool_options = [
        ['Multimeter', 'Oscilloscope'],
        ['Multimeter'],
        ['Oscilloscope', 'Logic Analyzer'],
        ['Multimeter', 'Soldering Iron']
    ]
    
    for i in range(15):
        tech = Technician(
            name=fake.name(),
            certs=random.choice(cert_options),
            tools=random.choice(tool_options),
            avg_resolution_time=round(random.uniform(20, 90), 1),
            current_queue=random.randint(0, 4),
            location_lat=round(random.uniform(32.75, 32.85), 4),
            location_lng=round(random.uniform(-96.85, -96.75), 4)
        )
        db.add(tech)
    
    db.commit()
    print("15 technicians seeded!")

def seed_tickets(db: Session):
    device_types = ['Laptop', 'Desktop', 'Server', 'Printer', 'Monitor']
    issue_categories = ['Boot Loop', 'Liquid Damage', 'Screen Crack', 'No Power', 'Overheating']
    urgencies = ['Critical', 'High', 'Medium', 'Low']
    
    techs = db.query(Technician).all()
    
    for i in range(60):  # 50 past + 10 open
        ticket = Ticket(
            device_type=random.choice(device_types),
            issue_category=random.choice(issue_categories),
            urgency=random.choice(urgencies),
            est_revenue=round(random.uniform(50, 800), 2),
            customer_lat=round(random.uniform(32.7, 32.9), 4),
            customer_lng=round(random.uniform(-96.9, -96.7), 4)
        )
        db.add(ticket)
    
    db.commit()
    print("60 tickets seeded!")

def seed_assignments(db: Session):
    tickets = db.query(Ticket).all()
    techs = db.query(Technician).all()
    
    for i in range(100):
        assignment = Assignment(
            ticket_id=random.choice([t.id for t in tickets]),
            tech_id=random.choice([t.id for t in techs]),
            match_score=round(random.uniform(65, 98), 1)
        )
        db.add(assignment)
    
    db.commit()
    print("100 assignments seeded!")

def main():
    db = SessionLocal()
    try:
        seed_technicians(db)
        seed_tickets(db)
        seed_assignments(db)
        print("\n Hardware Handoff fully seeded!")
    finally:
        db.close()

if __name__ == "__main__":
    main()