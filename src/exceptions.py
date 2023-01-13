from abc import ABC

MESSAGE_BOOKING_FAILED_NO_CREDIT = "No credit available"
MESSAGE_BOOKING_FAILED_UNKNOWN = "Unknown error"


class ErrorResponse(ABC, Exception):
    key_phrase = None


class TooManyWrongAttempts(ErrorResponse):
    key_phrase = "demasiadas veces"


class IncorrectCredentials(ErrorResponse):
    key_phrase = "incorrecto"


class BookingFailed(Exception):
    pass


class NoBookingGoal(Exception):
    pass
