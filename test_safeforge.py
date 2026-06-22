# test_safeforge.py
"""
Tests for SafeForge module.
"""

import unittest
from safeforge import SafeForge

class TestSafeForge(unittest.TestCase):
    """Test cases for SafeForge class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SafeForge()
        self.assertIsInstance(instance, SafeForge)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SafeForge()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
