import logging
import os

if __name__ == '__main__':
    logging.warning('Watch out!')
    # Will not print anything.
    logging.info('I told you so')

    logger = logging.getLogger()

    file_handler = logging.FileHandler('example.log')
    formatter = logging.Formatter('%(asctime)s – %(levelname)s – %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    logger.debug('This message should go to the log file')
    logger.info('So should this')
    logger.warning('And this, too')
    logger.error('And non-ASCII stuff, too, like Øresund and Malmö')

    with open('example.log', 'r') as f:
        for line in f:
            print(line)
    
    os.remove('example.log')
