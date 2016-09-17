# -*- coding: utf-8 -*-
def TestAssert(i_input):
    ''' assert expression, erroMessage
    '''
    assert isinstance(i_input, int), 'The input is not an integer'
    assert i_input > 10, 'The input is not greater than 10'

def TestLogging(i_input):
    '''
        import logging
        logging.exception(e)
    '''
    import logging
    try:
        assert i_input > 30, 'The input is not greater than 30'
    except Exception as e:
        logging.exception(e)

def TestLoggingConfig():
    '''
    logging.basicConfig(level=logging.INFO)
    '''
    import logging
    logging.basicConfig(level=logging.INFO)
    logging.info('This is test logging config')


def main():
    print(TestAssert.__doc__)
    print(TestLogging.__doc__)
    userIn = int(input('Please input a int number>'))
    try:
        TestAssert(userIn)
        TestLogging(userIn)
        TestLoggingConfig()
    except Exception as e:
        print("An unexpected error occurred!", e)

if __name__ == '__main__':
    main()
   
