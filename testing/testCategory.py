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
  
#     def testInserCategory(self):
#         aCategory = category()
#         aCategory.insertCategory('Category1',21)
# 
#         # Eliminando la categoria
#         aCategory.deleteCategory('Category1')
#         
#     # Casos Frontera
#     
#     # Prueba
#     def testInserCategoryExists(self):
#         aCategory = category()
#         result    = aCategory.insertCategory('Category1',21)
#         self.assertTrue(result)
# 
#         # Eliminando la categoria
#         aCategory.deleteCategory('Category1')
#         
#     # Prueba
#     def testInserCategory1Exists(self):
#         aCategory = category()
#         result    = aCategory.insertCategory('A',1)
#         self.assertTrue(result)
# 
#         # Eliminando la categoria
#         aCategory.deleteCategory('A')
#         
#     # Prueba
#     def testInserCategory50Exists(self):
#         aCategory = category()
#         result    = aCategory.insertCategory('A'*50,2)
#         self.assertTrue(result)
# 
#         # Eliminando la categoria
#         aCategory.deleteCategory('A'*50)
#         
#     # Prueba
#     def testInserCategory0Exists(self):
#         aCategory = category()
#         result    = aCategory.insertCategory('',1)
#         self.assertFalse(result)
# 
#     # Prueba
#     def testInserCategory51Exists(self):
#         aCategory = category()
#         result    = aCategory.insertCategory('A'*51,1)
#         self.assertFalse(result)
# 
#     # Prueba
#     def testInserCategoryLongExists(self):
#         aCategory = category()
#         result    = aCategory.insertCategory('A'*((2**28)-1),1)
#         self.assertFalse(result)
#         
#     # Prueba
#     def testInserCategoryEquals(self):
#         aCategory = category()
#         result    = aCategory.insertCategory('Categoria',2)
#         result1   = aCategory.insertCategory('Categoria',3)
#         self.assertFalse(result1)
#         
#         # Eliminando la categoria
#         aCategory.deleteCategory('Categoria')
#         
#     # Prueba
#     def testInserCategory1Equals(self):
#         aCategory = category()
#         result    = aCategory.insertCategory('C',2)
#         result1   = aCategory.insertCategory('C',3)
#         self.assertFalse(result1)
#         
#         # Eliminando la categoria
#         aCategory.deleteCategory('C')
#     
#     # Prueba
#     def testInserCategory50Equals(self):
#         aCategory = category()
#         result    = aCategory.insertCategory('C'*50,2)
#         result1   = aCategory.insertCategory('C'*50,3)
#         self.assertFalse(result1)
#         
#         # Eliminando la categoria
#         aCategory.deleteCategory('C'*50)
#         
#     # Prueba
#     def testInserCategoryWeight1(self):
#         aCategory = category()
#         result    = aCategory.insertCategory('Categoria',1)
#         self.assertTrue(result)
#         
#         # Eliminando la categoria
#         aCategory.deleteCategory('Categoria')
#         
#     # Prueba
#     def testInserCategoryWeight50(self):
#         aCategory = category()
#         result    = aCategory.insertCategory('Categoria',((2**28)-1))
#         self.assertTrue(result)
#         
#         # Eliminando la categoria
#         aCategory.deleteCategory('Categoria')
#         
#     # Prueba
#     def testInserCategoryWeight0(self):
#         aCategory = category()
#         result    = aCategory.insertCategory('Categoria',0)
#         self.assertTrue(result)
#         
#         # Eliminando la categoria
#         aCategory.deleteCategory('Categoria')
#         
#     # Casos Esquina
#     
#     # Prueba
#     def testInserCategoryName0Weight0(self):
#         aCategory = category()
#         result    = aCategory.insertCategory('',0)
#         self.assertFalse(result)
#         
#     # Prueba
#     def testInserCategoryName1Weight0(self):
#         aCategory = category()
#         result    = aCategory.insertCategory('A',0)
#         self.assertTrue(result)
# 
#         # Eliminando la categoria
#         aCategory.deleteCategory('A')
#         
#     # Prueba
#     def testInserCategoryName50Weight0(self):
#         aCategory = category()
#         result    = aCategory.insertCategory('A'*50,0)
#         self.assertTrue(result)
# 
#         # Eliminando la categoria
#         aCategory.deleteCategory('A'*50)
#         
#     # Prueba
#     def testInserCategoryName1WeightLong(self):
#         aCategory = category()
#         result    = aCategory.insertCategory('A',((2**28)-1))
#         self.assertTrue(result)
# 
#         # Eliminando la categoria
#         aCategory.deleteCategory('A')
#         
#     # Prueba
#     def testInserCategoryName0WeightLong(self):
#         aCategory = category()
#         result    = aCategory.insertCategory('',((2**28)-1))
#         self.assertFalse(result)
#         
#     # Casos Malicia
#     
#     # Prueba
#     def testInserCategorySpaceExists(self):
#         aCategory = category()
#         result    = aCategory.insertCategory(' ',2)
#         self.assertTrue(result)
#         
#         # Eliminando la categoria
#         aCategory.deleteCategory(' ')
#         
#     # Prueba
#     def testInserCategoryEnieExists(self):
#         aCategory = category()
#         result    = aCategory.insertCategory('ñ',2)
#         self.assertTrue(result)
#         
#         # Eliminando la categoria
#         aCategory.deleteCategory('ñ')
#         
#     # Prueba
#     def testInserCategoryNumber(self):
#         aCategory = category()
#         result    = aCategory.insertCategory(12,2)
#         self.assertFalse(result)
# 
#     # Prueba
#     def testInserCategoryArray(self):
#         aCategory = category()
#         result    = aCategory.insertCategory([],2)
#         self.assertFalse(result)
#         
#     # Prueba
#     def testInserCategoryDictionari(self):
#         aCategory = category()
#         result    = aCategory.insertCategory({},2)
#         self.assertFalse(result)
#         
#     # Prueba
#     def testInserCategoryWeightString(self):
#         aCategory = category()
#         result    = aCategory.insertCategory('categoria','1')
#         self.assertFalse(result)
#     
#     # Prueba
#     def testInserCategoryWeightArray(self):
#         aCategory = category()
#         result    = aCategory.insertCategory('categoria',[])
#         self.assertFalse(result)
#         
#     # Prueba
#     def testInserCategoryWeightDictionari(self):
#         aCategory = category()
#         result    = aCategory.insertCategory('categoria',{})
#         self.assertFalse(result)
#         
#     
#     #############################################      
#     #   Suite de Pruebas para updateCategory    #
#     #############################################
#     
#     # Caso Normal
#     
#     # Prueba
#     def testUpdateCategoryExist(self):
#         aCategory = category()
#         aCategory.insertCategory('Categoria',1)
#         result    = aCategory.updateCategory('Categoria', 'Nueva Categoria', 2)
#         self.assertTrue(result)
#         
#         # Eliminando la categoria
#         aCategory.deleteCategory('Nueva Categoria')
#         
#     # Prueba
#     def testUpdateCategoryNotExist(self):
#         aCategory = category()
#         aCategory.insertCategory('Categoria',1)
#         result    = aCategory.updateCategory('Cate', 'Nueva Categoria', 2)
#         self.assertFalse(result)
#         
#         # Eliminando la categoria
#         aCategory.deleteCategory('Categoria')
#         
#     # Casos Frontera
#     
#     # Prueba
#     def testUpdateCategoryName1Newname1(self):
#         aCategory = category()
#         aCategory.insertCategory('C',1)
#         result    = aCategory.updateCategory('C', 'N', 2)
#         self.assertTrue(result)
#         
#         # Eliminando la categoria
#         aCategory.deleteCategory('N')
#         
#     # Prueba
#     def testUpdateCategoryName1Newname(self):
#         aCategory = category()
#         aCategory.insertCategory('C',1)
#         result    = aCategory.updateCategory('C', 'Nueva Categoria', 2)
#         self.assertTrue(result)
#         
#         # Eliminando la categoria
#         aCategory.deleteCategory('Nueva Categoria') 
#         
#     # Prueba
#     def testUpdateCategoryName0(self):
#         aCategory = category()
#         aCategory.insertCategory('',1)
#         result    = aCategory.updateCategory('', 'N', 2)
#         self.assertFalse(result)
#         
#     # Prueba
#     def testUpdateCategoryNameNewname1(self):
#         aCategory = category()
#         aCategory.insertCategory('Categoria',1)
#         result    = aCategory.updateCategory('Categoria', 'N', 2)
#         self.assertTrue(result)
#         
#         # Eliminando la categoria
#         aCategory.deleteCategory('N')
#         
#     # Prueba
#     def testUpdateCategoryName50Newname(self):
#         aCategory = category()
#         aCategory.insertCategory('C'*50,1)
#         result    = aCategory.updateCategory('C'*50, 'Nueva Categoria', 2)
#         self.assertTrue(result)
#         
#         # Eliminando la categoria
#         aCategory.deleteCategory('Nueva Categoria')
#         
#     # Prueba
#     def testUpdateCategoryNameNewname50(self):
#         aCategory = category()
#         aCategory.insertCategory('Categoria',1)
#         result    = aCategory.updateCategory('Categoria', 'N'*50, 2)
#         self.assertTrue(result)
#         
#         # Eliminando la categoria
#         aCategory.deleteCategory('N'*50)
#     
#     # Prueba
#     def testUpdateCategoryNewname51(self):
#         aCategory = category()
#         aCategory.insertCategory('Categoria',1)
#         result    = aCategory.updateCategory('C', 'N'*51, 2)
#         self.assertFalse(result)
#         
#         # Eliminando la categoria
#         aCategory.deleteCategory('Categoria')
#         
#     # Prueba
#     def testUpdateCategoryNameNewname0(self):
#         aCategory = category()
#         aCategory.insertCategory('Categoria',1)
#         result    = aCategory.updateCategory('Categoria', '', 2)
#         self.assertFalse(result)
#         
#         # Eliminando la categoria
#         aCategory.deleteCategory('Categoria')
#         
#     # Prueba
#     def testUpdateCategoryNewnameLong(self):
#         aCategory = category()
#         aCategory.insertCategory('Categoria',1)
#         result    = aCategory.updateCategory('Categoria', 'N'*((2**28)-1), 2)
#         self.assertFalse(result)
#         
#         # Eliminando la categoria
#         aCategory.deleteCategory('Categoria')
#         
#     # Prueba
#     def testUpdateCategoryWeight0(self):
#         aCategory = category()
#         aCategory.insertCategory('Categoria',1)
#         result    = aCategory.updateCategory('Categoria', 'Nueva Categoria', 0)
#         self.assertTrue(result)
#         
#         # Eliminando la categoria
#         aCategory.deleteCategory('Nueva Categoria')
#         
#     # Prueba
#     def testUpdateCategoryWeightLong(self):
#         aCategory = category()
#         aCategory.insertCategory('Categoria',1)
#         result    = aCategory.updateCategory('Categoria', 'Nueva Categoria', ((2**28)-1))
#         self.assertTrue(result)
#         
#         # Eliminando la categoria
#         aCategory.deleteCategory('Nueva Categoria')
#         
#     # Casos Esquina
#     
#     # Prueba
#     def testUpdateCategoryName0Newname0Weight0(self):
#         aCategory = category()
#         aCategory.insertCategory('',1)
#         result    = aCategory.updateCategory('', '', 0)
#         self.assertFalse(result)
# 
#     # Prueba
#     def testUpdateCategoryName1Newname0Weight0(self):
#         aCategory = category()
#         aCategory.insertCategory('C',1)
#         result    = aCategory.updateCategory('C', '', 0)
#         self.assertFalse(result)
#         
#         # Eliminando la categoria
#         aCategory.deleteCategory('Categoria')
#         
#     # Prueba
#     def testUpdateCategoryName50Newname0Weight0(self):
#         aCategory = category()
#         aCategory.insertCategory('C'*50,1)
#         result    = aCategory.updateCategory('C'*50, '', 0)
#         self.assertFalse(result)
#         
#         # Eliminando la categoria
#         aCategory.deleteCategory('C'*50)
#         
#     # Prueba
#     def testUpdateCategoryNameLongNewname0Weight0(self):
#         aCategory = category()
#         aCategory.insertCategory('C'*((2**28)-1),1)
#         result    = aCategory.updateCategory('C'*((2**28)-1), '', 0)
#         self.assertFalse(result)
#         
#     # Prueba
#     def testUpdateCategoryName0Newname1Weight0(self):
#         aCategory = category()
#         aCategory.insertCategory('',1)
#         result    = aCategory.updateCategory('', 'N', 0)
#         self.assertFalse(result)
#             
#     # Prueba
#     def testUpdateCategoryName0Newname50Weight0(self):
#         aCategory = category()
#         aCategory.insertCategory('',1)
#         result    = aCategory.updateCategory('', 'N'*50, 0)
#         self.assertFalse(result)
# 
#     # Prueba
#     def testUpdateCategoryName0NewnameLongWeight0(self):
#         aCategory = category()
#         aCategory.insertCategory('',1)
#         result    = aCategory.updateCategory('', 'N'*((2**28)-1), 0)
#         self.assertFalse(result)
#         
#     # Prueba
#     def testUpdateCategoryName0Newname0Weight1(self):
#         aCategory = category()
#         aCategory.insertCategory('',1)
#         result    = aCategory.updateCategory('', '', 1)
#         self.assertFalse(result)
#         
#     # Prueba
#     def testUpdateCategoryName0Newname0WeightLong(self):
#         aCategory = category()
#         aCategory.insertCategory('',1)
#         result    = aCategory.updateCategory('', '', (2**28)-1)
#         self.assertFalse(result)
#         
#     # Prueba
#     def testUpdateCategoryName1Newname1WeightLong1(self):
#         aCategory = category()
#         aCategory.insertCategory('C',1)
#         result    = aCategory.updateCategory('C', 'N', 1)
#         self.assertTrue(result)
#         
#         # Eliminando la categoria
#         aCategory.deleteCategory('N')
#         
#     # Prueba
#     def testUpdateCategoryName50Newname1WeightLong1(self):
#         aCategory = category()
#         aCategory.insertCategory('C'*50,1)
#         result    = aCategory.updateCategory('C'*50, 'N', 1)
#         self.assertTrue(result)
#         
#         # Eliminando la categoria
#         aCategory.deleteCategory('N')
#         
#     # Prueba
#     def testUpdateCategoryNameLongNewname1WeightLong1(self):
#         aCategory = category()
#         aCategory.insertCategory('C'*((2**28)-1),1)
#         result    = aCategory.updateCategory('C'*((2**28)-1), 'N', 1)
#         self.assertFalse(result)
#           
#     # Prueba
#     def testUpdateCategoryName1Newname50WeightLong1(self):
#         aCategory = category()
#         aCategory.insertCategory('C',1)
#         result    = aCategory.updateCategory('C', 'N'*50, 1)
#         self.assertTrue(result)
#         
#         # Eliminando la categoria
#         aCategory.deleteCategory('N'*50)
#         
#     # Prueba
#     def testUpdateCategoryName1NewnameLongWeightLong1(self):
#         aCategory = category()
#         aCategory.insertCategory('C',1)
#         result    = aCategory.updateCategory('C', 'N'*((2**28)-1), 1)
#         self.assertFalse(result)
#         
#         # Eliminando la categoria
#         aCategory.deleteCategory('C')
#         
#     # Prueba
#     def testUpdateCategoryName1Newname1WeightLong(self):
#         aCategory = category()
#         aCategory.insertCategory('C',1)
#         result    = aCategory.updateCategory('C', 'N', (2**28)-1)
#         self.assertTrue(result)
#         
#         # Eliminando la categoria
#         aCategory.deleteCategory('N')
#         
#     # Prueba
#     def testUpdateCategoryName50Newname50WeightLong(self):
#         aCategory = category()
#         aCategory.insertCategory('C'*50,1)
#         result    = aCategory.updateCategory('C'*50, 'N'*50, (2**28)-1)
#         self.assertTrue(result)
#         
#         # Eliminando la categoria
#         aCategory.deleteCategory('N'*50)
#         
#     # Prueba
#     def testUpdateCategoryName50NewnameLongWeightLong1(self):
#         aCategory = category()
#         aCategory.insertCategory('C'*50,1)
#         result    = aCategory.updateCategory('C', 'N'*((2**28)-1), 1)
#         self.assertFalse(result)
#         
#         # Eliminando la categoria
#         aCategory.deleteCategory('C'*50)        
#         
#     # Casos Malicia
#     
#     # Prueba
#     def testUpdateCategoryNameNewnameEnieWeight(self):
#         aCategory = category()
#         aCategory.insertCategory('Categoria',1)
#         result    = aCategory.updateCategory('Categoria', 'ñ', 3)
#         self.assertTrue(result)
#         
#         # Eliminando la categoria
#         aCategory.deleteCategory('ñ')
#         
#     # Prueba
#     def testUpdateCategoryNameNewnameArrayWeight(self):
#         aCategory = category()
#         aCategory.insertCategory('Categoria',1)
#         result    = aCategory.updateCategory('Categoria', [], 3)
#         self.assertFalse(result)
#         
#         # Eliminando la categoria
#         aCategory.deleteCategory('Categoria')
#         
#     # Prueba
#     def testUpdateCategoryNameNewnameDictionariWeight(self):
#         aCategory = category()
#         aCategory.insertCategory('Categoria',1)
#         result    = aCategory.updateCategory('Categoria', {}, 3)
#         self.assertFalse(result)
#         
#         # Eliminando la categoria
#         aCategory.deleteCategory('Categoria')
#         
#     # Prueba
#     def testUpdateCategoryNameNewnameNumberWeight(self):
#         aCategory = category()
#         aCategory.insertCategory('Categoria',1)
#         result    = aCategory.updateCategory('Categoria', 21, 3)
#         self.assertFalse(result)
#         
#         # Eliminando la categoria
#         aCategory.deleteCategory('Categoria')
#         
#     # Prueba
#     def testUpdateCategoryNameNewnameWeightNegativeNumber(self):
#         aCategory = category()
#         aCategory.insertCategory('Categoria',1)
#         result    = aCategory.updateCategory('Categoria', 'Nueva Categoria', -3)
#         self.assertFalse(result)
#         
#         # Eliminando la categoria
#         aCategory.deleteCategory('Categoria')
        
    #############################################      
    #  Suite de Pruebas para searchIdCategory   #
    #############################################
        
    # Caso Normal
    
    # Prueba
    def testSearchIdCategory(self):
        aCategory = category()
        aCategory.insertCategory('Categoria',1)
        result    = aCategory.searchIdCategory(1)
        self.assertTrue(result)
         
        # Eliminando la categoria
        aCategory.deleteCategory('Categoria')
        
        
        
        
        
        
        
        
        
        
        