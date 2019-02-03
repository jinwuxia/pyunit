from framework.testresult import TestResult

class TextTestResult(TestResult):
    """A test result class that can print formatted text results to a stream.

    Used by TextTestRunner.
    """
    separator1 = '=' * 70
    separator2 = '-' * 70

    def __init__(self, stream, descriptions, verbosity):
        TestResult.__init__(self)
        self.stream = stream
        self.showAll = verbosity > 1
        self.dots = verbosity == 1
        self.descriptions = descriptions

    def getDescription(self, test):
        if self.descriptions:
            return test.shortDescription() or str(test)
        else:
            return str(test)

    def startTest(self, test):
        TestResult.startTest(self, test)
        if self.showAll:
            self.stream.write(self.getDescription(test))
            self.stream.write(" ... ")

    def addSuccess(self, test):
        TestResult.addSuccess(self, test)
        if self.showAll:
            self.stream.writeln("ok")
        elif self.dots:
            self.stream.write('.')

    def addError(self, test, err):
        TestResult.addError(self, test, err)
        if self.showAll:
            self.stream.writeln("ERROR")
        elif self.dots:
            self.stream.write('E')
        if err[0] is KeyboardInterrupt:
            self.shouldStop = 1

    def addFailure(self, test, err):
        TestResult.addFailure(self, test, err)
        if self.showAll:
            self.stream.writeln("FAIL")
        elif self.dots:
            self.stream.write('F')

    def printErrors(self):
        if self.dots or self.showAll:
            self.stream.writeln()
        self.printErrorList('ERROR', self.errors)
        self.printErrorList('FAIL', self.failures)

    def printErrorList(self, flavour, errors):
        for test, err in errors:
            self.stream.writeln(self.separator1)
            self.stream.writeln("%s: %s" % (flavour,self.getDescription(test)))
            self.stream.writeln(self.separator2)
            for line in apply(traceback.format_exception, err):
                for l in string.split(line,"\n")[:-1]:
                    self.stream.writeln("%s" % l)
