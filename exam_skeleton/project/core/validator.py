class Validator:
    @staticmethod
    def raise_message_if_string_is_empty(string, message):
        if string == '':
            raise ValueError(message)

    @staticmethod
    def raise_message_if_amount_is_less_or_equal_to_zero(amount, message):
        if amount <= 0:
            raise ValueError(message)
