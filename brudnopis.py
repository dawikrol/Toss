


def get_arguments(self):
    try:
        a = input('Enter name: ')
        if len(a) > 20:
            raise TossErrors.DataError('Input is incorrect', 'The name is too long!')
    except TossErrors as e:
        print('TossError: {}'.format(e))
    else:
        self.arguments.append(a)