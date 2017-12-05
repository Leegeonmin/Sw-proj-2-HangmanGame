import unittest

from guess import Guess

class TestGuess(unittest.TestCase):
    def setUp(self):
        self.g1 = Guess('default')
        self.g2 = Guess('self')
        self.g3 = Guess

    def tearDown(self):
        pass

    def testDisplayCurrent(self):
        self.assertEqual(self.g1.displayCurrent(), '_ e _ _ _ _ _ ')
        
        self.g1.guess('a')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a _ _ _ ')               
        self.g1.guess('t')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a _ _ t ')               
        self.g1.guess('u')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a u _ t ')
        self.g1.guess('x')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a u _ t ')

    def testDisplayGuessed(self):
        self.assertEqual(self.g1.displayGuessed(), ' e n ')            
        self.g1.guess('a')                
        self.assertEqual(self.g1.displayGuessed(), ' a e n ')          
        self.g1.guess('t')               
        self.assertEqual(self.g1.displayGuessed(), ' a e n t ')        
        self.g1.guess('u')               
        self.assertEqual(self.g1.displayGuessed(), ' a e n t u ')      
        self.g1.guess('x') 
        self.assertEqual(self.g1.displayGuessed(), ' a e n t u x ')

    def testGuess(self):
        self.assertIsNotNone(self.g1.guessedChars)
        self.assertEqual(self.g1.guessedChars, { '', 'e', 'n'})    
        self.assertEqual(self.g1.currentStatus, '_e_____') 
        self.assertTrue(self.g1.guess('a'))  
        self.assertEqual(self.g1.guessedChars, {'a', '', 'e', 'n'})
        self.assertEqual(self.g1.currentStatus, '_e_a___') 
        self.assertTrue(self.g1.guess('t'))       
        self.assertEqual(self.g1.guessedChars, {'t', 'a', '', 'e', 'n'})      
        self.assertEqual(self.g1.currentStatus, '_e_a__t')       
        self.assertTrue(self.g1.guess('u'))        
        self.assertEqual(self.g1.guessedChars, {'u', 't', 'a', '', 'e', 'n'})     
        self.assertEqual(self.g1.currentStatus, '_e_au_t')         
        self.assertFalse(self.g1.guess('z'))       
        self.assertEqual(self.g1.guessedChars, {'z', 'u', 't', 'a', '', 'e', 'n'})       
        self.assertEqual(self.g1.currentStatus, '_e_au_t')

if __name__ =='__main__':
    unittest.main()
