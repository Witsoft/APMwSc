# -*- coding: utf-8 -*-. 

import sys
import unittest

# Ruta que permite utilizar el módulo category.py
sys.path.append('../app/scrum')

from category import *

class TestCategory(unittest.TestCase):
    
    #############################################      
    #   Suite de Pruebas para insertCategory    #
    #############################################
    
    # Caso Inicial
  
    def testInserCategory(self):
        aCategory = category()
        aCategory.insertCategory('Category1',21)

        # Eliminando la categoria
        aCategory.deleteCategory('Category1')
        
    # Casos Frontera
    
    # Prueba
    def testInserCategoryExists(self):
        aCategory = category()
        result    = aCategory.insertCategory('Category1',21)
        self.assertTrue(result)

        # Eliminando la categoria
        aCategory.deleteCategory('Category1')
        
    # Prueba
    def testInserCategory1Exists(self):
        aCategory = category()
        result    = aCategory.insertCategory('A',1)
        self.assertTrue(result)

        # Eliminando la categoria
        aCategory.deleteCategory('A')
        
    # Prueba
    def testInserCategory50Exists(self):
        aCategory = category()
        result    = aCategory.insertCategory('A'*50,2)
        self.assertTrue(result)

        # Eliminando la categoria
        aCategory.deleteCategory('A'*50)
        
    # Prueba
    def testInserCategory0Exists(self):
        aCategory = category()
        result    = aCategory.insertCategory('',1)
        self.assertFalse(result)

    # Prueba
    def testInserCategory51Exists(self):
        aCategory = category()
        result    = aCategory.insertCategory('A'*51,1)
        self.assertFalse(result)

    # Prueba
    def testInserCategoryLongExists(self):
        aCategory = category()
        result    = aCategory.insertCategory('A'*((2**28)-1),1)
        self.assertFalse(result)
        
    # Prueba
    def testInserCategoryEquals(self):
        aCategory = category()
        result    = aCategory.insertCategory('Categoria',2)
        result1   = aCategory.insertCategory('Categoria',3)
        self.assertFalse(result1)
        
        # Eliminando la categoria
        aCategory.deleteCategory('Categoria')
        
    # Prueba
    def testInserCategory1Equals(self):
        aCategory = category()
        result    = aCategory.insertCategory('C',2)
        result1   = aCategory.insertCategory('C',3)
        self.assertFalse(result1)
        
        # Eliminando la categoria
        aCategory.deleteCategory('C')
    
    # Prueba
    def testInserCategory50Equals(self):
        aCategory = category()
        result    = aCategory.insertCategory('C'*50,2)
        result1   = aCategory.insertCategory('C'*50,3)
        self.assertFalse(result1)
        
        # Eliminando la categoria
        aCategory.deleteCategory('C'*50)
        
    # Prueba
    def testInserCategoryWeight1(self):
        aCategory = category()
        result    = aCategory.insertCategory('Categoria',1)
        self.assertTrue(result)
        
        # Eliminando la categoria
        aCategory.deleteCategory('Categoria')
        
    # Prueba
    def testInserCategoryWeight50(self):
        aCategory = category()
        result    = aCategory.insertCategory('Categoria',((2**28)-1))
        self.assertTrue(result)
        
        # Eliminando la categoria
        aCategory.deleteCategory('Categoria')
        
    # Prueba
    def testInserCategoryWeight0(self):
        aCategory = category()
        result    = aCategory.insertCategory('Categoria',0)
        self.assertTrue(result)
        
        # Eliminando la categoria
        aCategory.deleteCategory('Categoria')
        
    # Casos Esquina
    
    # Prueba
    def testInserCategoryName0Weight0(self):
        aCategory = category()
        result    = aCategory.insertCategory('',0)
        self.assertFalse(result)
        
    # Prueba
    def testInserCategoryName1Weight0(self):
        aCategory = category()
        result    = aCategory.insertCategory('A',0)
        self.assertTrue(result)

        # Eliminando la categoria
        aCategory.deleteCategory('A')
        
    # Prueba
    def testInserCategoryName50Weight0(self):
        aCategory = category()
        result    = aCategory.insertCategory('A'*50,0)
        self.assertTrue(result)

        # Eliminando la categoria
        aCategory.deleteCategory('A'*50)
        
    # Prueba
    def testInserCategoryName1WeightLong(self):
        aCategory = category()
        result    = aCategory.insertCategory('A',((2**28)-1))
        self.assertTrue(result)

        # Eliminando la categoria
        aCategory.deleteCategory('A')
        
    # Prueba
    def testInserCategoryName0WeightLong(self):
        aCategory = category()
        result    = aCategory.insertCategory('',((2**28)-1))
        self.assertFalse(result)
        
    # Casos Malicia
    
    # Prueba
    def testInserCategorySpaceExists(self):
        aCategory = category()
        result    = aCategory.insertCategory(' ',2)
        self.assertTrue(result)
        
        # Eliminando la categoria
        aCategory.deleteCategory(' ')
        
    # Prueba
    def testInserCategoryEnieExists(self):
        aCategory = category()
        result    = aCategory.insertCategory('ñ',2)
        self.assertTrue(result)
        
        # Eliminando la categoria
        aCategory.deleteCategory('ñ')
        
    # Prueba
    def testInserCategoryNumber(self):
        aCategory = category()
        result    = aCategory.insertCategory(12,2)
        self.assertFalse(result)

    # Prueba
    def testInserCategoryArray(self):
        aCategory = category()
        result    = aCategory.insertCategory([],2)
        self.assertFalse(result)
        
    # Prueba
    def testInserCategoryDictionari(self):
        aCategory = category()
        result    = aCategory.insertCategory({},2)
        self.assertFalse(result)
        
    # Prueba
    def testInserCategoryWeightString(self):
        aCategory = category()
        result    = aCategory.insertCategory('categoria','1')
        self.assertFalse(result)
    
    # Prueba
    def testInserCategoryWeightArray(self):
        aCategory = category()
        result    = aCategory.insertCategory('categoria',[])
        self.assertFalse(result)
        
    # Prueba
    def testInserCategoryWeightDictionari(self):
        aCategory = category()
        result    = aCategory.insertCategory('categoria',{})
        self.assertFalse(result)
        
    
    #############################################      
    #   Suite de Pruebas para searchCategory    #
    #############################################
    
    