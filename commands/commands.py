from database.database import DatabaseManager

db = DatabaseManager()


# Creating a table
class CreateCommand:
    @staticmethod
    def execute(db_name: str) -> None:
        db.create_table(db_name, {
            'number': 'integer',
            'order_number': 'integer',
            'cost_dol': 'integer',
            'delivery_date': 'text',
            'cost_rub': 'integer'
        })


# Adding an entry
class AddCommands:
    @staticmethod
    def execute(db_name: str, data: dict) -> None:
        db.add(db_name, data)


# Deleting an entry
class DeleteCommand:
    @staticmethod
    def execute(db_name: str) -> None:
        db.delete(db_name)
