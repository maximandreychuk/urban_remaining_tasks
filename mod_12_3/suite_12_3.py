import unittest

from tests_12_3 import RunnerTest, TournamentTest


suite1 = unittest.TestLoader().loadTestsFromTestCase(RunnerTest)
suite2 = unittest.TestLoader().loadTestsFromTestCase(TournamentTest)
alltests = unittest.TestSuite([suite1, suite2])

runner = unittest.TextTestRunner(verbosity=2)
runner.run(alltests)