import unittest

from syntaxEx import *


class SyntaxTest(unittest.TestCase):

    def testSubjPred(self):
        """ Testar Subj och Pred """
        self.assertEqual(kollaGrammatiken("JAG VET"), "Följer syntaxen!")

    def testFelKonj(self):
        self.assertEqual(kollaGrammatiken("JAG VET MEN"), "Fel konjunktion: MEN före . ")

if __name__ == '__main__':
    unittest.main()
