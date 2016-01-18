""" Tests for the main module of calculator """

import os
import unittest

from calculator import main
from calculator.main import (
    run,
    DEFAULT_OUT,
    tokenize_line
)

TEST_INPUT = 'tests/test_input/'

class TestMain(unittest.TestCase):

    def setUp(self):
        main.sys.argv = ['']

    def test_read_file(self):
        test_file = TEST_INPUT + 'test_read.in'

        main.sys.argv = ['', test_file]
        
        run()

        in_file = open(test_file, 'r')
        out_file = open(DEFAULT_OUT, 'r')

        in_lines = in_file.readlines()
        out_lines = out_file.readlines()

        self.assertEqual(
            in_lines,
            out_lines,
        )

        os.remove(DEFAULT_OUT)

    def test_split_add(self):
        test_file = TEST_INPUT + 'test_split_add.in'

        test_file = open(test_file, 'r')

        line = test_file.read()

        result = tokenize_line(line)

        self.assertEqual(
            result,
            ['1', '+', '2'],
        )

