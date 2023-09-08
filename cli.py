import click
from sqlalchemy import create_engine
from datetime import datetime
from sqlalchemy.orm import sessionmaker
from models import Base,Baby
from crud import create_baby, delete_baby,get_baby_records, get_baby_record_by_id

# Database setup
DATABASE_URL = 'sqlite:///records.db'
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@click.group()
def cli():
    pass

@cli.command()
@click.option('--baby_name', type=str, required=True)
@click.option('--baby_weight', type=float, required=True)
@click.option('--birth_date', type=str, required=True)
@click.option('--sickness_details', type=str, required=True)
def add_baby(baby_name, baby_weight, birth_date, sickness_details):
    db = SessionLocal()

    try:
        birth_date = datetime.strptime(birth_date, '%Y-%m-%d').date()

        baby = create_baby(db, baby_name, baby_weight, birth_date, sickness_details)
        click.echo(f"Added baby {baby.baby_name} with ID {baby.baby_id}")

    except Exception as e:
        click.echo(f"Error: {str(e)}")

    finally:
        db.close()


if __name__ == '__main__':
    cli()

#delete feature
@cli.command()
@click.option('--baby_id', type=int, required=True, help='ID of the baby to delete')
def delete_baby(baby_id):
    db = SessionLocal()

    try:
        deleted = delete_baby(db, baby_id)
        if deleted:
            click.echo(f"Deleted baby with ID {baby_id}")
        else:
            click.echo(f"Baby with ID {baby_id} not found.")
    except Exception as e:
        click.echo(f"Error: {str(e)}")

    finally:
        db.close()

#view baby records
@cli.command()
@click.option('--baby_id', type=int, help='ID of the baby to view')
def view_babies(baby_id):
    db = SessionLocal()

    try:
        if baby_id:
            # View a specific baby's details
            baby = db.query(Baby).filter(Baby.baby_id == baby_id).first()
            if baby:
                click.echo(f"Baby ID: {baby.baby_id}")
                click.echo(f"Name: {baby.baby_name}")
                click.echo(f"Weight: {baby.baby_weight} kg")
                click.echo(f"Birth Date: {baby.birth_date}")
                click.echo(f"Sickness Details: {baby.sickness_details}")
            else:
                click.echo(f"Baby with ID {baby_id} not found.")
        else:
            # View a list of all babies
            babies = db.query(Baby).all()
            if babies:
                click.echo("List of Babies:")
                for baby in babies:
                    click.echo(f"ID: {baby.baby_id}, Name: {baby.baby_name}")
            else:
                click.echo("No babies found in the database.")
    except Exception as e:
        click.echo(f"Error: {str(e)}")

    finally:
        db.close()


