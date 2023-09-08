import click
from sqlalchemy import create_engine
from datetime import datetime
from sqlalchemy.orm import sessionmaker
from models import Base, Baby
from crud import create_baby, get_all_babies, delete_baby
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

@cli.command()
def view_babies():
    db = SessionLocal()

    try:
        babies = get_all_babies(db)
        
        if babies:
            click.echo("List of Babies:")
            for baby in babies:
                click.echo(f"ID: {baby.baby_id}, Name: {baby.baby_name}, Weight: {baby.baby_weight}, Birth Date: {baby.birth_date}, Sickness Details: {baby.sickness_details}")
        else:
            click.echo("No baby records found.")

    except Exception as e:
        click.echo(f"Error: {str(e)}")

    finally:
        db.close()

@cli.command()
@click.option('--baby_id', type=int, required=True)
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

@cli.command()
@click.option('--baby_id', type=int, required=True)
def view_baby_details(baby_id):
    db = SessionLocal()

    try:
        baby = db.query(Baby).filter(Baby.baby_id == baby_id).first()

        if baby:
            click.echo(f"Baby ID: {baby.baby_id}")
            click.echo(f"Name: {baby.baby_name}")
            click.echo(f"Weight: {baby.baby_weight}")
            click.echo(f"Birth Date: {baby.birth_date}")
            click.echo(f"Sickness Details: {baby.sickness_details}")
        else:
            click.echo(f"No baby found with ID {baby_id}")

    except Exception as e:
        click.echo(f"Error: {str(e)}")

    finally:
        db.close()

@cli.command()
@click.option('--baby_name', type=str, required=True, help='Name of the baby to search for')
def search_baby_by_name(baby_name):
    db = SessionLocal()

    try:
        baby = db.query(Baby).filter(Baby.baby_name.ilike(f'%{baby_name}%')).all()

        if baby:
            click.echo(f"Search Results for Baby Name '{baby_name}':")
            for b in baby:
                click.echo(f"ID: {b.baby_id}, Name: {b.baby_name}, Weight: {b.baby_weight}, Birth Date: {b.birth_date}, Sickness Details: {b.sickness_details}")
        else:
            click.echo(f"No baby found with the name '{baby_name}'")

    except Exception as e:
        click.echo(f"Error: {str(e)}")

    finally:
        db.close()

if __name__ == '__main__':
    cli()


# create a baby 
# python3 -m cli add-baby --baby_name "Jack Reacher" --baby_weight 3.5 --birth_date "2023-09-10" --sickness_details "Cancer"
# python3 -m cli add-baby --baby_name "Nelson Mandela" --baby_weight 2.8 --birth_date "2023-09-11" --sickness_details "Typhoid"
# python3 -m cli add-baby --baby_name "Museveni Yoweri" --baby_weight 3.0 --birth_date "2023-09-12" --sickness_details "Diarrhea"

# view details of a single child
# python3 cli.py view-baby-details --baby_id 6

# view the list of children
# python3 -m cli view-babies

# search baby by name 
# python3 cli.py search-baby-by-name --baby_name "Juan Mata"
