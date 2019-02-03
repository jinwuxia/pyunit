import time
import sys
import traceback
import string
import os
import types

class TestResult:
    """Holder for test result information.

    Test results are automatically managed by the TestCase and TestSuite
    classes, and do not need to be explicitly manipulated by writers of tests.

    Each instance holds the total number of tests run, and collections of
    failures and errors that occurred among those test runs. The collections
    contain tuples of (testcase, exceptioninfo), where exceptioninfo is a
    tuple of values as returned by sys.exc_info().
    """
    def __init__(self):
        self.failures = []
        self.errors = []
        self.testsRun = 0
        self.shouldStop = 0

    def startTest(self, test):
        "Called when the given test is about to be run"
        self.testsRun = self.testsRun + 1

    def stopTest(self, test):
        "Called when the given test has been run"
        pass

    def addError(self, test, err):
        "Called when an error has occurred"
        self.errors.append((test, err))

    def addFailure(self, test, err):
        "Called when a failure has occurred"
        self.failures.append((test, err))

    def addSuccess(self, test):
        "Called when a test has completed successfully"
        pass

    def wasSuccessful(self):
        "Tells whether or not this result was a success"
        return len(self.failures) == len(self.errors) == 0

    def stop(self):
        "Indicates that the tests should be aborted"
        self.shouldStop = 1

    def __repr__(self):
        return "<%s run=%i errors=%i failures=%i>" % \
               (self.__class__, self.testsRun, len(self.errors),
                len(self.failures))
