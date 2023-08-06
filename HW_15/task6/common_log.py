import logging

FORMAT = ("{asctime} - {levelname}: {msg}")

logging.basicConfig(filename='task6.log', filemode='w', format=FORMAT, style='{', level=logging.NOTSET)
common_log = logging.getLogger()

if __name__ == '__main__':
    print("Не предназначен для отдельного использования")