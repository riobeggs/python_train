import unittest


class TestExamples(unittest.TestCase):
    """Common testing unit testing methods"""

    def test_is_equal(self):
        """Tests that a == b"""
        
        a = 10
        b = 10

        self.assertEqual(a, b)

    def test_is_not_equal(self):
        """Tests that a != b"""
        
        a = 5
        b = 10

        self.assertNotEqual(a, b)

    def test_is_true(self):
        """Tests that a == True"""
        
        a = True

        self.assertTrue(a)

    def test_is_false(self):
        """Tests that a == False"""
        
        a = False

        self.assertFalse(a)

    def test_is_none(self):
        """Tests that a == None"""
        
        a = None

        self.assertIsNone(a)

    def test_is_not_none(self):
        """Tests that a != None"""
        
        a = "test"

        self.assertIsNotNone(a)

    def test_is_in(self):
        """Tests that a is in ["a", "b", "c"]"""
        
        test_list = ["a", "b", "c"]

        self.assertIn("a", test_list)

    def test_is_not_in(self):
        """Tests that a is not in ["x", "y", "z"]"""
        
        test_list = ["x", "y", "z"]

        self.assertNotIn("a", test_list)

    def test_is_instance(self):
        """Tests that a is an instance of an integer"""
        
        a = 100

        self.assertIsInstance(a, int)

    def test_is_not_instance(self):
        """Tests that a is an instance of a string"""
        
        a = 100

        self.assertNotIsInstance(a, str)


if __name__ == "__main__":
    unittest.main()
