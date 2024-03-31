import os
import logging
from logging.handlers import RotatingFileHandler


class LoggerSetup:
    """
    Класс для настройки и управления логированием.

    Позволяет создавать логгеры с предварительной настройкой обработчиков
    для записи в файлы и вывода в консоль. Поддерживает ротацию файлов логов.

    :ivar logger_name: Имя логгера.
    """

    def __init__(self, logger_name='app'):
        """
            Инициализатор логгера
        :param logger_name: Имя логгера
        """
        self.logger = logging.getLogger(logger_name)

        self.log_directory = 'logs'
        self.info_logfile = 'log.log'
        self.error_logfile = 'log_errors.log'

        self.log_format = '%(asctime)s | %(name)s | [%(levelname)s] | %(message)s'
        self.date_time_format = "%d.%m.%Y %H:%M:%S"

        self.setup_logger()

    def setup_logger(self) -> None:
        """
        Вызов всех основных функций логгера
        """
        self.logger.setLevel(logging.DEBUG)
        self.setup_directories()
        self.setup_file_handler()
        self.setup_error_file_handler()
        self.setup_console_handler()

    def setup_directories(self) -> None:
        """
        Создает директорию для логов, если она не существует.
        """
        if not os.path.exists(self.log_directory):
            os.makedirs(self.log_directory)

    def setup_file_handler(self) -> None:
        """
        Добавляет обработчик для записи логов в файл.
        """
        file_handler = self.setup_file_for_logs(self.info_logfile)
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(logging.Formatter(self.log_format, datefmt=self.date_time_format))
        self.logger.addHandler(file_handler)

    def setup_error_file_handler(self) -> None:
        """
        Добавляет обработчик для записи ошибок в отдельный файл.
        """
        error_file_handler = self.setup_file_for_logs(self.error_logfile)
        error_file_handler.setLevel(logging.ERROR)
        error_file_handler.setFormatter(logging.Formatter(self.log_format, datefmt=self.date_time_format))
        self.logger.addHandler(error_file_handler)

    def setup_console_handler(self) -> None:
        """
        Добавляет обработчик для вывода логов в консоль.
        """
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)
        console_handler.setFormatter(logging.Formatter(self.log_format, datefmt=self.date_time_format))
        self.logger.addHandler(console_handler)

    def setup_file_for_logs(self, logger_file: str) -> RotatingFileHandler:
        """
        Создает и возвращает обработчик файла логов с поддержкой ротации.

        :param logger_file: Имя файла лога.
        :return: Обработчик файла лога.
        """
        return RotatingFileHandler(
            os.path.join(self.log_directory, logger_file),
            maxBytes=5000000,
            backupCount=5,
            encoding='utf-8'
        )
