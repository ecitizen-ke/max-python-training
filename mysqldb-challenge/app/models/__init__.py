from app.db import Connection


class State:
    """This is a model of a state"""

    states = []
    capitals = []
    states_capitals = []

    def __init__(self):
        self.db = Connection()

    def get_states(self):
        """Get all states"""

        query = "SELECT * FROM states"
        self.db.cursor.execute(query)
        rows = self.db.cursor.fetchall()
        if rows:
            for row in rows:

                state = {
                    "id": row[0],
                    "name": row[1],
                    "abbreviation": row[2],
                    "population": row[3],
                    "year_admitted": row[4],
                }
                self.states.append(state)
            return self.states
        # Close cursor
        self.db.cursor.close()
        # Close connection
        self.db.conn.close()

    def filter(self):
        """Filter states by first letter"""

        query = "SELECT * FROM states WHERE name LIKE 'A%'"
        self.db.cursor.execute(query)
        rows = self.db.cursor.fetchall()
        if rows:
            for row in rows:

                state = {
                    "id": row[0],
                    "name": row[1],
                    "abbreviation": row[2],
                    "population": row[3],
                    "year_admitted": row[4],
                }
                self.states.append(state)
            return self.states
        # Close cursor
        self.db.cursor.close()
        # Close connection
        self.db.conn.close()

    def create(self, name, abbreviation, population, year_admitted):
        """Create state method"""

        self.name = name
        self.abbreviation = abbreviation
        self.population = population
        self.year_admitted = year_admitted

        state = (self.name, self.abbreviation, self.population, self.year_admitted)

        query = "INSERT INTO states(name, abbreviation, population, year_admitted) VALUES(%s,%s,%s,%s)"

        self.db.cursor.execute(query, state)

        # If query execution is successful
        if self.db.cursor.rowcount:
            # Commit data to the database
            self.db.conn.commit()
            return {
                "name": self.name,
                "abbreviation": self.abbreviation,
                "population": self.population,
                "year_admitted": year_admitted,
            }
        # Close cursor
        self.db.cursor.close()
        # Close connection
        self.db.conn.close()

    def update(self, id, population):
        """Update state population method"""
        self.population = population
        self.id = id
        query = "UPDATE states SET population=%s WHERE id=%s"
        self.db.cursor.execute(query, (self.population, self.id))
        # If query execution is successful
        if self.db.cursor.rowcount:
            # Commit data to the database
            self.db.conn.commit()
            self.db.cursor.execute("SELECT * FROM states WHERE id=%s", [self.id])
            updated_state = self.db.cursor.fetchone()
            return {
                "id": updated_state[0],
                "name": updated_state[1],
                "abbreviation": updated_state[2],
                "population": updated_state[3],
                "year_admitted": updated_state[4],
            }
        # Close cursor
        self.db.cursor.close()
        # Close connection
        self.db.conn.close()

    def delete(self, id):
        """delete state method"""
        self.id = id
        query = "DELETE FROM states WHERE id=%s"
        self.db.cursor.execute(query, [self.id])
        # If query execution is successful
        if self.db.cursor.rowcount:
            # Commit data to the database
            self.db.conn.commit()
            return {"message": "State deleted successfully"}
        # Close cursor
        self.db.cursor.close()
        # Close connection
        self.db.conn.close()

    def search(self, name):
        """delete state method"""
        self.name = name
        query = "SELECT * FROM states WHERE name=%s"
        self.db.cursor.execute(query, [self.name])
        # If query execution is successful
        state = self.db.cursor.fetchone()
        # Close cursor
        self.db.cursor.close()
        # Close connection
        self.db.conn.close()
        return {
            "id": state[0],
            "name": state[1],
            "abbreviation": state[2],
            "population": state[3],
            "year_admitted": state[4],
        }

    def get_capitals(self):
        """fetch state capitals method"""
        query = "SELECT * FROM capitals"
        self.db.cursor.execute(query)
        rows = self.db.cursor.fetchall()
        if rows:
            for row in rows:
                capital = {"id": row[0], "state_id": row[1], "name": row[2]}
                self.capitals.append(capital)
            return self.capitals
        # Close cursor
        self.db.cursor.close()
        # Close connection
        self.db.conn.close()

    def get__most_populous(self):
        """fetch the most populous state"""
        query = "SELECT * FROM  states WHERE population = (SELECT MIN(population) FROM states)"
        self.db.cursor.execute(query)
        state = self.db.cursor.fetchone()
        # Close cursor
        self.db.cursor.close()
        # Close connection
        self.db.conn.close()
        return {
            "id": state[0],
            "state": state[1],
            "abbreviation": state[2],
            "population": state[3],
            "year_admitted": state[4],
        }

    def get_states_capitals(self):
        """fetch states with their capitals"""
        query = "SELECT states.id, states.name,states.abbreviation,capitals.name,states.population, \
            states.year_admitted FROM states INNER JOIN capitals ON states.id=capitals.state_id"
        self.db.cursor.execute(query)
        rows = self.db.cursor.fetchall()
        if rows:
            for row in rows:
                state = {
                    "id": row[0],
                    "name": row[1],
                    "abbreviation": row[2],
                    "capital": row[3],
                    "population": row[4],
                    "year_admitted": row[5],
                }
                self.states_capitals.append(state)
            return self.states_capitals
        # Close cursor
        self.db.cursor.close()
        # Close connection
        self.db.conn.close()
