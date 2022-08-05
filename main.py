from google_api import google_sheets_api
from course import course_translation as cs
from commands import commands
from telegram_messages import bot
from datetime import datetime
from time import sleep
import logging

commands.CreateCommand().execute('GoogleSheets')  # Creating a table in a database

gs = google_sheets_api.GoogleSheet()  # GoogleSheet object from imported module
test_range = 'test_list!A2:D'  # The range for reading data from the Google Sheet object

# Logging
logging.basicConfig(filename='log.log', level=logging.ERROR)
logging.error(f'\nNew program start - {datetime.now()}')


def main() -> None:
    """Main function:
       1) Gets the current Google sheet, the current dollar rate and cleaning the current Google sheet
       2) Gets lated orders and send telegram message
       3) Writing the current Google sheet"""
    google_sheet = gs.read_data(test_range)  # Google sheet
    dollar = cs.get_course()  # To get the dollar rate
    commands.DeleteCommand().execute('GoogleSheets')  # Cleaning the current google sheet

    try:
        lated_orders = ([int(data[0]) for data in google_sheet if
                        datetime.strptime(data[3], '%d.%m.%Y') < datetime.now()])  # list of lated orders
        bot.check_fresh_order(lated_orders)  # Checking the freshness of the order


        # Writing in google sheet
        if google_sheet is not None:
            for row in google_sheet:
                number = row[0]  # The first column
                order_number = row[1]  # The second column
                cost_dol = row[2]  # The third column
                delivery_date = row[3]  # The fourth column
                cost_rub = int(float(cost_dol) * float(dollar))  # To get the ruble rate

                # Accessing and writing to the database
                commands.AddCommands().execute('GoogleSheets', {
                    'number': number,
                    'order_number': order_number,
                    'cost_dol': cost_dol,
                    'delivery_date': delivery_date,
                    'cost_rub': cost_rub
                })

    except Exception as _error:
        print(f'''[INFO] ERROR: {_error};
                         Возможно таблица еще редактируется.''')
        logging.error(f'{_error} - {datetime.now()}')


if __name__ == '__main__':
    while 1:
        sleep(1)  # Eliminates the error of the limit of access per minute to GoogleSheetApi
        main()
