"""
Tests for version number
"""

import unittest
import nash


class TestVersion(unittest.TestCase):
    def test_bi_matrix_init(self):
        self.assertIsInstance(nash.__version__, str)
