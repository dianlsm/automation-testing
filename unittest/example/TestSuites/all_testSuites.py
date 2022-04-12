import unittest
from Package1.tc_login import LoginTest
from Package1.tc_signup import SignUpTest

from Package2.tc_payment import PaymentTest
from Package2.tc_paymentreturn import PaymentReturnTest

# Get all test LoginTest, SignupTest, PaymentTest, PaymentReturnTest
tc_1 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc_2 = unittest.TestLoader().loadTestsFromTestCase(SignUpTest)
tc_3 = unittest.TestLoader().loadTestsFromTestCase(PaymentTest)
tc_4 = unittest.TestLoader().loadTestsFromTestCase(PaymentReturnTest)

# create test suites
sanityTestSuite = unittest.TestSuite(tc_1, tc_2) # sanity test suite
unittest.TextTestRunner().run(sanityTestSuite)