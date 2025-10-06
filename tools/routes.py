from enum import Enum


class AppRoute(str, Enum):
    """
    ENUM содержит перечень адресов запросов
    """
    LOGIN = "./#/auth/login"
    REGISTRATION = "./#/auth/registration"
    DASHBOARD = "./#/dashboard"
    COURSES = "./#/courses"
    CREATE_COURSE = "./#/courses/create"