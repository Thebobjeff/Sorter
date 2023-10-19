import re,os
import pandas as pd
import numpy as np

def _numpy_pathChecker(file_numpy_Ray):
        """
        Used to ensure said file does exsit
        """
        return os.path.isfile(file_numpy_Ray)

class Sorter:
    """
        Accepts the file name as well as take in file path for future usecase  
    """
   
    def __init__(self, file_numpy_Ray):
        if not _numpy_pathChecker(file_numpy_Ray):
            raise NameError
        self._numpy_Ray =  pd.read_csv(file_numpy_Ray).to_numpy()
        self._count = []

    @property
    def numpy_Ray(self):
        return self._numpy_Ray
    
    @numpy_Ray.setter
    def numpy_Ray(self, numpy_Ray):
        if _numpy_pathChecker(numpy_Ray):
            self._numpy_Ray = numpy_Ray
        else:
            raise ValueError

    def _non_nums(self,sku):
        """
        Check if the given SKU contains any non-numeric characters.
        
        Parameters:
        - sku (str): The SKU to be checked.
        
        Returns:
        - bool: True if the SKU contains non-numeric characters, False otherwise.
        """
        if re.findall(r"[/()\s+]", sku): return True 

    def _splits(self,sku):
        """
        This function takes a string parameter `sku` and splits it into multiple parts based on the characters '/', '(', ')', and whitespace. It returns a list of the split parts, where each part is converted to uppercase.

        Parameters:
        - `sku` (str): The string to be split.

        Returns:
        - `splita` (list): A list of the split parts, with each part converted to uppercase.
        """
        splita = []
        try:
            for index,items in np.ndenumerate(re.split(r"[/()\s+]",sku)):
                splita.append(str(items).upper())
        except:
            for items in enumerate(sku):
                    splita.append(str(items).upper())
        return splita

    def _ones(self,item):
        """
        Check if the given item contains only a single element.

        Parameters:
            item (any): The item to be checked.

        Returns:
            bool: True if the item contains only a single element, False otherwise.
        """
        ray = self._splits(item)
        try: 
            if ray[1]: return False
        except:
            return True

    def _last(self,tocomp,comper):
        """
        Checks if the last six characters of the string representation of `comper` are equal to the string representation of `tocomp`.
        
        Parameters:
            tocomp (object): The object whose string representation will be compared.
            comper (object): The object whose string representation will be checked.
        
        Returns:
            bool: True if the last six characters of `comper` are equal to `tocomp`, False otherwise.
        """
        fullval = str(comper)
        lastsix = str(tocomp)
        if fullval.endswith(lastsix): return True
        
    def _compare_values(self,value1, value2):
        """
        This function takes two parameters, `value1` and `value2`, and performs some operations on `value2`.
        The function first checks if `value2` is a string that contains non-numeric characters using the `non_nums` function.
        If `value2` contains non-numeric characters, it splits `value2` using the `splits` function and assigns the result to `value2`.
        Otherwise, it converts `value2` to uppercase using the `str.upper` method.

        The function then prints the value of `value2`.

        Next, it calls the `ones` function with `value2` as the argument.

        After that, there is a commented out block of code that compares `value1` and `value2`.

        The function then iterates over the characters in `value2` using the `enumerate` function.
        For each character, it checks if `value1` is equal to the character.
        If `value1` is equal to the character, it sets `val` to `True`, prints "Pass", and returns `val`.

        If the loop completes without finding a match, the function checks if the result of the `ones` function is `True`
        and if `value1` is equal to `value2`.
        If both conditions are true, it sets `val` to `True` and returns `val`.

        The function does not have any explicit return type specified.
        """
        val = False
        value2 = self._splits(value2) if self._non_nums(str(value2)) else str(value2).upper()
        self._ones(value2)
        for index,item in enumerate(value2):
            if value1 == item or self._last(value1,item): val = True 
        else: 
            if self._ones(value2) & (value1 == value2) or self._last(value1,value2): val = True
        return val
    
    def complete(self,product_Sku):
        """
        Search for a product SKU in the given numpy array and return whether it was found or not, along with the list of indices and counts where the SKU was found.

        Parameters:
            product_Sku (str): The product SKU to search for.

        Returns:
            tuple: A tuple containing a boolean value indicating whether the product SKU was found or not, and a list of lists where each inner list contains the index
            and count of the SKU found in the numpy array.
        """
        product_Sku = str(product_Sku).upper()
        for index,all_terms in enumerate(self._numpy_Ray):
            terms = str(all_terms[0]).upper()
            if self._compare_values(product_Sku,terms):
                self._count.append([index, all_terms[0],all_terms[1]])
        return self._count
    
    def complete_name(self,product_Sku):
        """
        Retrieves the count of product SKUs that match the given SKU.

        Parameters:
            product_Sku (Any): The SKU of the product to match.

        Returns:
            list: A list containing the count of product SKUs that match the given SKU.
        """
        product_Sku = str(product_Sku).upper()
        for index,all_terms in enumerate(self._numpy_Ray):
            terms = str(all_terms[0]).upper()
            if self._compare_values(product_Sku,terms):
                self._count.append(all_terms[1])
        return self._count
                

#//////////////////////////////////////////////////////////////TESTING/////////////////////////////////////////////         
