def thisRaisesAZeroDivisionError():
    x = 1/0

def thisRaisesAValueError():
    y = int('Five')

def thisDoesNotRaiseAnyErrors():
    z = 'just a string'

def tryExercise():
    print 'A',
    try:
        # Line Of Code Is Inserted Here #
        thisDoesNotRaiseAnyErrors()
        print 'B',
    except ZeroDivisionError as e:
        print 'C',
    else:
        print 'D',
    finally:
        print 'E',
    print 'F'
