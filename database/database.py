import psycopg2
from config.config import host, user, password, db_name


class DatabaseManager:
    def __init__(self):
        self.connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
        self.connection.autocommit = True

    # Performing all actions with the database
    def _execute(self, statement: str, values=None):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute(statement, values or [])  # Setting cursor parameters
            return cursor

    # Creating a table in a DB
    def create_table(self, table_name: str, columns: dict) -> None:
        columns_with_types = [f'{column_name} {data_type}' for column_name, data_type in
                              columns.items()]  # Sets a list with the table name and columns with their types
        self._execute(
            f"""
            CREATE TABLE IF NOT EXISTS {table_name}
            ({', '.join(columns_with_types)});
            """
        )

    # Adding an enrty to the database
    def add(self, table_name: str, data: dict) -> None:
        column_names = ', '.join(data.keys())  # Setting column names
        column_values = tuple(data.values())  # Setting column values

        self._execute(
            f"""
            INSERT INTO {table_name} ({column_names})
            VALUES {column_values};
            """
        )

    # Deleting an entry from database
    def delete(self, table_name: str) -> None:
        self._execute(
            f'''
            DELETE FROM {table_name};
            ''')
