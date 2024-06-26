#!/usr/bin/python3
"""fetch states with 'a'
"""
import sys
from model_state import Base, State

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    states = session.query(State).order_by(State.id).filter(
            State.name.ilike('%a%'))
    for state in states:
        print(f"{state.id}: {state.name}")
