import unittest
import lib
# ..........................commented lines are incorrect

# class Test(unittest.TestCase):
#     def test(self):
#         for i in range (1,500):
#             self.assertEqual(lib.even(i*2),True)
#         for i in range (1,500):
#             self.assertEqual(lib.even(i*2-1),False)
    
#         # for i in range (1,500):
#         #     self.assertEqual(lib.even(i*(-2)),True) #выводит False
#         for i in range (1,500):
#             self.assertEqual(lib.even(i*(-2)+1),False)
#         # self.assertEquals(lib.even(0), True)  #выводит 0
#         #self.assertEquals(lib.even(0.0), True)  #выводит ноль

#         for i in range (1,500):
#             self.assertEqual(lib.even(i*(-2)+0.1),False)
#         for i in range (1,500):
#             self.assertEqual(lib.even(i*(2)+0.1),False)
# unittest.main(verbosity=2)








# from lib import factorial as f
# def fact(n):
#     s=1
#     if n==0:
#         return 1
#     else:
#         for i in range(1,n+1):
#             s*=i
#         return s

# class Test(unittest.TestCase):
#     def test(self):
        # for i in range (0,500):
        #     self.assertEqual(f(i),fact(i)) #на больштх числах выводит float
        # for i in range (1,500):
        #     self.assertEqual(f(i*(-1)),1) #выыодит -1 вместо единицы
        # for i in range (1,500):
        #     self.assertEqual(f(i*(-1)+0.1),1) #выыодит -1 вместо единицы
        
# unittest.main(verbosity=2)





# from lib import palindrome as p
# class Test(unittest.TestCase):
#     def test(self):
#         self.assertEqual(p('a'),True) #return False
#         self.assertEqual(p('aa'),True)
#         self.assertEqual(p('aca'),True) #return False
#         self.assertEqual(p('aaa'),True) #return False
#         self.assertEqual(p('xopox'),True) #return False
#         self.assertEqual(p('acac'),False)
#         self.assertEqual(p(''),True)
#         self.assertEqual(p('acca'),True)
#         self.assertEqual(p('pppp'),True)
# unittest.main(verbosity=2)



#class Test(unittest.TestCase):
#    def test(self):
#        self.assertEqual(lib.prime(1),False) #return True
#        self.assertEqual(lib.prime(0),False) #return True
#        self.assertEqual(lib.prime(-1),False) #return True
#        self.assertEqual(lib.prime(101),True)
#unittest.main(verbosity=2)


# import math
# import numpy as np
# class Test(unittest.TestCase):
#     def test(self):
#         self.assertEqual(lib.sin(0),0)
#         for i in np.arange(0,3.14,0.0001):
#             self.assertEqual(lib.sin(i),np.sin(i))
#         for i in np.arange(-3.14,0,0.0001):
#             self.assertEqual(lib.sin(i),np.sin(i))
#         for i in np.arange(3.14,100,0.0001):
#             self.assertEqual(lib.sin(i),np.sin(i)) #wrong
#         for i in np.arange(-100,-3.14,0.0001):
#             self.assertEqual(lib.sin(i),np.sin(i)) #wrong
# unittest.main(verbosity=2)


# 'sqrt' was taken as an example
# Подключаем библиотеку для тестирования
import unittest
# Подключаем тестируемую библиотеку
import lib

# Класс, описывающий набор тестов
class LibTest(unittest.TestCase):

    # Тестируем работу sqrt с положительными аргументами
    def test_sqrt_non_negative_arg(self):
        # Набор проверок
        self.assertEqual(lib.sqrt(9), 3)
        self.assertEqual(lib.sqrt(1), 1)
        self.assertEqual(lib.sqrt(0), 0)

    def test_sqrt_negative(self):
        # Набор проверок
        self.assertEqual(lib.sqrt(-1), 0)


# Запускаем тесты на исполнение
unittest.main(verbosity=2)
