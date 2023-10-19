import os, csv
# from datetime import date as dt

def _pathChecker(file_Path):
        """
        Used to ensure said file does exsit
        """
        return os.path.isfile(file_Path)

class Filesystem:
    """
        Accepts the file name as well as take in file path for future usecase  
    """
    def __init__(self, pos_File_Path):
            self._posPath = pos_File_Path

    
    @classmethod    
    def add_path(self, stock_File_Path):
        self.val = False
        if _pathChecker(stock_File_Path):
            self.val = True
            self._stockPath = stock_File_Path            
    @property
    def posPath(self):
        """
        Returns the value of the `posPath` attribute.

        :return: The value of the `posPath` attribute.
        """
        return self._posPath
    
    @property
    def stockPath(self):
        """
        Returns the value of the `stockPath` attribute.
        """
        return self._stockPath

    @stockPath.setter
    def stockPath(self, stockPath):
        """
        Setter method for the `stockPath` attribute.
        """
        if _pathChecker(stockPath):
            self._stockPath = stockPath
        else:  
            print(f"There was an error finding {stockPath}. Please ensure that this files exsits.\n The file path has not been updated!")

    @posPath.setter
    def posPath(self, posPath):
        """
        Setter method for the `posPath` attribute.

        Parameters:
            posPath (str): The new path to be set.

        Returns:
            None

        Description:
            This method sets the `posPath` attribute of the class to the specified path if the path exists. If the path does not exist, an error message is printed.

        Example:
            >>> obj = ClassName()
            >>> obj.posPath = "new/path"
            There was an error finding new/path. Please ensure that this file exists.
            The file path has not been updated!
        """
        # We make sure that the new path exsists before moving on
        if _pathChecker(posPath):
            self._posPath = posPath
        else: 
            print(f"There was an error finding {posPath}. Please ensure that this files exsits.\n The file path has not been updated!")
    
    def create_file(self,file_Name):
        """
        Create a new file with the given file name.

        Parameters:
            file_Name (str): The name of the file.

        Returns:
            None
        """
        # Creation of a new file is done here 
        with open(f'{file_Name}', 'w', newline='') as file:
            writer = csv.writer(file)
            field = ["Sku", "Product Name", "Quantity", "Price"]
            writer.writerow(field) 
             
    def create_file_path(self,file_Name, file_path):
        """
        Creates a file at the specified path with the given name.

        Parameters:
            file_Name (str): The name of the file to be created.
            file_Path (str): The path where the file should be created.

        Returns:
            None
        """
        # Creation of a new file is done here 
        self._stockPath = file_path
        with open((os.path.join(file_path, f'{file_Name}.csv')), 'x', newline='') as file:
            writer = csv.writer(file)
            field = ["Sku", "Product Name", "Quantity", "Price"]
            writer.writerow(field) 

    def append_to_file(self,data):
        """
        Appends the given data to the specified file.
        """
        with open(self._stockPath , 'a', newline='') as file:
            try: 
                data[1]
                writer = csv.writer(file)
                writer.writerow(data)
            except:
                pass
    def append_to_path(self,data,file_path):
        """
        Appends the given data to the specified file.
        """
        with open(file_path , 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(data)
#////////////////////////////////////////////////////////////////Testing///////////////////////////////////////////////////////////////////////////

    