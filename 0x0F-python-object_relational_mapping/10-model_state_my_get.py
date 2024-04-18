#!/usr/bin/python3
"""fetch the given state
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
    state = session.query(State).order_by(State.id).filter(
            State.name == sys.argv[4])
    if state.count() == 0:
        print("Not found")
    else:
        print(f"{state.one().id}")
