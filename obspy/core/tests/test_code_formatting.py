# -*- coding: utf-8 -*-

from obspy.core.util.decorator import skipIf
from obspy.core.util.testing import check_flake8
import os
import unittest


class CodeFormattingTestCase(unittest.TestCase):
    """
    Test codebase for compliance with the flake8 tool.
    """
    @skipIf('OBSPY_NO_FLAKE8' in os.environ, 'flake8 check disabled')
    def test_flake8(self):
        """
        Test codebase for compliance with the flake8 tool.
        """
        error_file_count, message, file_count = check_flake8()
        self.assertTrue(file_count > 10)
        self.assertEqual(error_file_count, 0, message)


def suite():
    return unittest.makeSuite(CodeFormattingTestCase, 'test')


if __name__ == '__main__':
    unittest.main(defaultTest='suite')
