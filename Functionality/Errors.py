class DataError(Exception):
    def __init__(self, text, kind):
        super().__init__(text)
        self.kind = kind

    def __str__(self):
        return '{}. {}.'.format(super().__str__(), self.kind)



try:
    raise DataError('a', 'i')
except DataError as error:
    print('{}'.format(error))