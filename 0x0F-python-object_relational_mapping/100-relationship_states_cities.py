#!/usr/bin/python3
"""add city with relationship
"""
import sys
from relationship_state import Base, State
from relationship_city import City

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    state = State(name="California")
    state.cities = [City(name="San Francisco")]
    session.add(state)
    session.commit()
