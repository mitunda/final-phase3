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

# Get all babies
def get_all_babies(db: Session):
    return db.query(Baby).all()

# Delete a baby by ID
def delete_baby(db: Session, baby_id: int):
    baby = db.query(Baby).filter(Baby.baby_id == baby_id).first()
    
    if baby:
        db.delete(baby)
        db.commit()
        return True
    else:
        return False