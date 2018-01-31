from viewelsRemove import remove_vow
from charindex import ch_index
from mario import mario
from dic import dictionary
from multiblication import multiply
from area import calcArea



import unittest

class TestAssignmentOne(unittest.TestCase):
    def remove_vow(self):
        self.assertEqual(remove_vow('mobile'), 'mbl')

    def ch_index(self):
        self.assertEqual(ch_index('This is javaScript','i'), [2,5,15])


    def dictionary(self):
        l1 = ["toqa", "rana", "aya"]
        d1 = {'a':['aya'], 'r':['rana'],'t':['toqa']}
        self.assertEqual(dictionary(l1), d1) 


    def multiply(self):
        self.assertEqual(multiply(3), [[1],[2,4],[3,6,9]])

    def calcArea(self):
      self.assertEqual(calcArea("r"))      




    def mario(self):
       self.assertEqual(mario(4),""" *
       **
       ***
       ****
       """ 
       )




    


























if __name__ == '__main__':
    unittest.main()        