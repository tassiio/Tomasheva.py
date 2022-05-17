import random


class Error(Exception):
    pass


class KillError(Error):
    pass


class DrunkError(Error):
    pass


class CarCrashError(Error):
    pass


class GluttonyError(Error):
    pass


class DepressionError(Error):
    pass


class Life:
    karma_max = 500

    def __init__(self):
        self.your_karma = 0

    def one_day(self):
        krm = open('karma_errors.log', 'a+')
        try:
            check = random.choices([0, random.choice([KillError, DrunkError, CarCrashError, GluttonyError,
                                                      DepressionError])], [9 / 10, 1 / 10])[0]
            if check == 0:
                self.your_karma += random.choice([i for i in range(1, 8)])
            else:
                raise check
        except KillError:
            print('KillError')
            krm.write('KillError\n')
        except DrunkError:
            print('DrunkError')
            krm.write('DrunkError\n')
        except CarCrashError:
            print('CarCrushError')
            krm.write('CarCrushError\n')
        except GluttonyError:
            print('GluttonyError')
            krm.write('GluttonyError\n')
        except DepressionError:
            print('DepressionError')
            krm.write('DepressionError\n')
        finally:
            krm.close()
