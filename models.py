# Import necessary modules and classes
from sqlalchemy import Column, Integer, String, Float, Date, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

# Create a declarative base for SQLAlchemy models
Base = declarative_base()

# Define the Baby class
class Baby(Base):
    __tablename__ = 'baby'

    baby_id = Column(Integer, primary_key=True)
    baby_name = Column(String)
    baby_weight = Column(Float)
    birth_date = Column(Date)
    sickness_details = Column(Text)
    created_at = Column(DateTime)

    # Define the relationship to Assignments
    assignments = relationship('Assignment', back_populates='baby')

# Define the HealthcareProfessional class
class HealthcareProfessional(Base):
    __tablename__ = 'healthcare_professional'

    professional_id = Column(Integer, primary_key=True)
    professional_name = Column(String)
    created_at = Column(DateTime)

    # Define the relationship to Assignments
    assignments = relationship('Assignment', back_populates='professional')

# Define the Assignment class
class Assignment(Base):
    __tablename__ = 'assignment'

    assignment_id = Column(Integer, primary_key=True)
    professional_id = Column(Integer, ForeignKey('healthcare_professional.professional_id'))
    baby_id = Column(Integer, ForeignKey('baby.baby_id'))
    assigned_date = Column(Date)
    end_date = Column(Date)
    created_at = Column(DateTime)

    # Define the relationships to Baby and HealthcareProfessional
    baby = relationship('Baby', back_populates='assignments')
    professional = relationship('HealthcareProfessional', back_populates='assignments')
