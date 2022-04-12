import unittest


class SignUpTest(unittest.TestCase):
    def test_signByEmail(self):
        print("This is sign by email test")
        self.assertTrue(True)
    def test_signByFacebook(self):
        print("This is sign by facebook test")
        self.assertTrue(True)
    def test_signByTwitter(self):
        print("This is sign by Twitter test")
        self.assertTrue(True)
    
    

    
if __name__== "__main__":
    unittest.main()
    