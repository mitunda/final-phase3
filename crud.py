# Import necessary modules and classes
from sqlalchemy.orm import Session
from models import Baby

# Create a new baby record
def create_baby(db: Session, baby_name: str, baby_weight: float, birth_date: str, sickness_details: str):
    db_baby = Baby(baby_name=baby_name, baby_weight=baby_weight, birth_date=birth_date, sickness_details=sickness_details)
    db.add(db_baby)
    db.commit()
    db.refresh(db_baby)
    return db_baby

# Delete a baby record by ID
def delete_baby(db: Session, baby_id: int):
    db_baby = db.query(Baby).filter(Baby.baby_id == baby_id).first()
    if db_baby:
        db.delete(db_baby)
        db.commit()
        return True
    return False

# Get all baby records
def get_baby_records(db: Session):
    return db.query(Baby).all()

# Get a specific baby record by ID
def get_baby_record_by_id(db: Session, baby_id: int):
    return db.query(Baby).filter(Baby.baby_id == baby_id).first()


