# -*- coding: utf-8 -*-. 
 
import unittest

from testAccions                import *
from testActorsUserHistory      import *
from testBackLog                import *
from testCategory               import *
from testHistory                import *
from testLogin                  import *
from testObjective              import *
from testObjectivesUserHistory  import *
from testRole                   import *
from testTask                   import *
from testUser                   import *

def suite():

    suite = unittest.TestSuite()
    suite.addTest (TestAccions)
    suite.addTest (TestActorsUserHistory)
    suite.addTest (TestBacklog)
    suite.addTest (TestCategory)
    suite.addTest (TestHistory)
    suite.addTest (TestLogin)
    suite.addTest (TestObjectives)
    suite.addTest (TestObjectivesUserHistory)
    suite.addTest (TestActors)
    suite.addTest (TestTask)
    suite.addTest (TestUser)
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    test_suite = suite()
    runner.run (test_suite)