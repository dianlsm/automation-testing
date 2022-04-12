import unittest

class PaymentTest(unittest.TestCase):
    def test_paymentindodollor(self):
        print("This is payment is dollor test")
        self.assertTrue(True)
    def test_paymentinrupees(self):
        print("This is payment is rupess test")
        self.assertTrue(True)


if __name__== "__main__":
    unittest.main()
    