import testresult

class GUITestResult(testresult.TestResult):
    """A TestResult that makes callbacks to its associated GUI TestRunner.
    Used by BaseGUITestRunner. Need not be created directly.
    """
    def __init__(self, callback):
	testresult.TestResult.__init__(self)
	self.callback = callback

    def addError(self, test, err):
	testresult.TestResult.addError(self, test, err)
	self.callback.notifyTestErrored(test, err)

    def addFailure(self, test, err):
	testresult.TestResult.addFailure(self, test, err)
	self.callback.notifyTestFailed(test, err)

    def stopTest(self, test):
        testresult.TestResult.stopTest(self, test)
        self.callback.notifyTestFinished(test)

    def startTest(self, test):
        testresult.TestResult.startTest(self, test)
        self.callback.notifyTestStarted(test)
