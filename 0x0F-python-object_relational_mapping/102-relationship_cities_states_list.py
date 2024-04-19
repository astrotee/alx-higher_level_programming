#!/usr/bin/python3
"""list states with their cities
"""
import sys
from relationship_state import Base
from relationship_city import City

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, selectinload

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    cities = session.query(City).options(
                selectinload(City.state)
                                          ).order_by(City.id)
    for city in cities:
        print(f"{city.id}: {city.name} -> {city.state.name}")
