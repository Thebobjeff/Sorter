import sorts, Filemanager, os.path,os,csv
import pandas as pd
from PyQt6.QtWidgets import QLineEdit, QPushButton, QHBoxLayout, QMainWindow, QLabel, QWidget, QVBoxLayout,QComboBox, QApplication, QFileDialog, QMessageBox, QTableWidget, QTableWidgetItem, QFrame
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt



class AnotherWindow(QWidget):
    def __init__(self,array):
        super().__init__()
        print("setp 1")
        self.resize(60, 80)
        ray = array
        self.selected_item = None
        layout = QVBoxLayout()
        self.label = QLabel("Another Window")
        layout.addWidget(self.label)
        
        # Create a QComboBox
        self.combo_box = QComboBox()
        self.combo_box.addItems(ray)
        layout.addWidget(self.combo_box)
        
        # Connect a function to handle item selection
        self.combo_box.currentIndexChanged.connect(self.handle_combobox_selection)
        self.setLayout(layout)

        
    def handle_combobox_selection(self, index):
        # Get the selected item text
        self.selected_item = self.combo_box.currentText()
        self.item()
    
    def item(self):
        return self.selected_item

class Mainface(QMainWindow):
    def __init__(self):
        
        # Set the window icon
        icon = QIcon("path_to_icon.png")  # Replace with the path to your icon file
       

        super().__init__()
        self.setWindowTitle("Testing app")
        #size of window is set here
        self.setMinimumSize(1040,650)
        
        # Label belong Here
        self.skul = QLabel("SKU")
        self.skul.setStyleSheet("font-weight: bold; font-size: 20;")
        self.product_name = QLabel("Product Name")
        self.product_name.setStyleSheet("font-weight: bold; font-size: 20;")
        self.Quantity = QLabel("Quantity")
        self.Quantity.setStyleSheet("font-weight: bold; font-size: 20;")
        self.price = QLabel("Price")
        self.price.setStyleSheet("font-weight: bold; font-size: 20;")
        entry_title = QLabel("Entry Feilds")
        # entry_title.setFont
        entry_title.setStyleSheet("font-weight: bold; font-size: 30px;")
        
        
        # Input Feild belong Here
        # Sku Feild
        self.skuf = QLineEdit()
        self.skuf.setPlaceholderText("SKU")
        self.skuf.setFixedSize(120,25)
        self.skuf.returnPressed.connect(self.scanned_entry)
        # Product Name Feild
        self.product_namef = QLineEdit()
        self.product_namef.setFixedSize(120,25)
        self.product_namef.setPlaceholderText("Product Name")
        # self.skuf.textChanged.connect(self.len)
        # Quantity Feild
        self.quantityf = QLineEdit()
        self.quantityf.setFixedSize(120,25)
        self.quantityf.setPlaceholderText("Quantity")
        
        # Price Feild
        self.pricef = QLineEdit()
        self.pricef.setFixedSize(120,25)
        self.pricef.setPlaceholderText("Price")

        # Above top of the layout
        self.tops = QHBoxLayout()
        self.tops.addWidget(entry_title, alignment=Qt.AlignmentFlag.AlignBottom)

        # The top of the layout
        self.top1 = QHBoxLayout()
        self.top1.addWidget(self.skul, alignment=Qt.AlignmentFlag.AlignBottom)
        self.top1.addWidget(self.product_name, alignment=Qt.AlignmentFlag.AlignBottom)
        self.top1.addWidget(self.Quantity, alignment=Qt.AlignmentFlag.AlignBottom)
        self.top1.addWidget(self.price, alignment=Qt.AlignmentFlag.AlignBottom)
        
        # Buttons come here
        self.entry = QPushButton("Enter")
        self.entry.setFixedWidth(80)
        self.entry.clicked.connect(self.get_data)

        # works when the Enter key is pressed and calls said functions 
        self.skuf.returnPressed.connect(self.scanned_entry)
        self.pricef.returnPressed.connect(self.get_data)
        self.product_namef.returnPressed.connect(self.quantityf.setFocus)
        self.quantityf.returnPressed.connect(self.pricef.setFocus)

        # The bottom below the bottom of the layout
        self.enter = QHBoxLayout()
        self.enter.addWidget(self.entry, alignment = Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignRight)

        # Bottom of the layout
        self.bottom1 = QHBoxLayout()
        self.bottom1.addWidget(self.skuf, alignment=Qt.AlignmentFlag.AlignTop)
        self.bottom1.addWidget(self.product_namef, alignment=Qt.AlignmentFlag.AlignTop)
        self.bottom1.addWidget(self.quantityf, alignment=Qt.AlignmentFlag.AlignTop)
        self.bottom1.addWidget(self.pricef, alignment=Qt.AlignmentFlag.AlignTop)

        # Entry Feild belong Here on this main layout
        self.B1 = QVBoxLayout()
        # Adding this to the layout
        self.B1.addLayout(self.tops)
        self.B1.addLayout(self.top1)
        self.B1.addLayout(self.bottom1)
        self.B1.addLayout(self.enter)
        

        # Items of B2
        self.labelFilePath = QLabel("File Path")
        self.labelFilePath.setFixedHeight(35)
        self.labelFilePath.setMinimumWidth(50)
        self.labelFilePath.setStyleSheet("background-color: white; padding: 5px; text-align: center; font-size: 20; border-radius: 10px;")

        self.labelFileName = QLabel("Select A File")
        self.labelFileName.setFixedHeight(40)
        self.labelFileName.setMinimumWidth(50)
        self.labelFileName.setStyleSheet("background-color: white; padding: 5px; text-align: center; font-weight: bold; font-size: 20; border-radius: 10px;")

        self.labelTitle = QLabel("Select File To Write To")
        self.labelTitle.setFixedHeight(35)
        self.labelTitle.setMinimumWidth(50)
        self.labelTitle.setStyleSheet("background-color: white; padding: 5px; text-align: center; font-size: 20; border-radius: 10px;")

        self.layoutTitle = QHBoxLayout()
        self.layoutTitle.addWidget(self.labelTitle, alignment=Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignLeft)

        self.layoutFile = QHBoxLayout()
        self.layoutFile.addWidget(self.labelFileName, alignment=Qt.AlignmentFlag.AlignLeft)

        self.new_File = QPushButton("Create New File")
        self.new_File.setMinimumWidth(80)
        self.new_File.setToolTip("Click me to create a new file")
        self.buttonSelectFile = QPushButton("Select File")
        self.buttonSelectFile.setFixedWidth(80)
        self.buttonSelectFile.clicked.connect(self.find_file2)
        self.buttonSelectFile.setToolTip("Lets you Search For Files")

        # Empty labels for design reasons
        emptyLabel1 = QLabel()
        emptyLabel2 = QLabel()
        emptyLabel3 = QLabel()

        self.layoutAFile = QHBoxLayout()
        self.layoutAFile.addWidget(self.buttonSelectFile, alignment=Qt.AlignmentFlag.AlignLeft)
        self.layoutAFile.addWidget(self.labelFilePath, alignment=Qt.AlignmentFlag.AlignLeft)

        self.buttonlay = QHBoxLayout()
        self.new_File1 = QPushButton("New File")
        self.new_File1.setMinimumWidth(80)
        self.new_File1.setToolTip("Click me to create a new file")
        self.buttonlay.addWidget(self.new_File1, alignment=Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        self.new_File.clicked.connect(self.create_new_file)

        # Adding the empty labels
        self.layoutAFile.addWidget(emptyLabel1, alignment=Qt.AlignmentFlag.AlignLeft)
        self.layoutAFile.addWidget(emptyLabel2, alignment=Qt.AlignmentFlag.AlignLeft)
        self.layoutAFile.addWidget(emptyLabel3, alignment=Qt.AlignmentFlag.AlignLeft)

        self.BM = QVBoxLayout()
        self.BM.addLayout(self.layoutTitle)
        self.BM.addLayout(self.layoutFile)
        self.BM.addLayout(self.layoutAFile)  
        self.BM.addLayout(self.buttonlay)     
        # Adding Items to B2
        self.B2 = QVBoxLayout()
        self.B2.addLayout(self.BM)  
        self.B2.setAlignment(Qt.AlignmentFlag.AlignCenter)   
        

        # Items of B3
        self.file_path = QLabel("File Path")
        self.file_path.setFixedHeight(35)
        self.file_path.setMinimumWidth(50)
        self.file_path.setStyleSheet("background-color: white; padding: 5px; text-align: center; font-size: 20; border-radius: 10px;")

        self.file_name = QLabel("Select A File")
        self.file_name.setFixedHeight(40)
        self.file_name.setMinimumWidth(50)
        self.file_name.setStyleSheet("background-color: white; padding: 5px; text-align: center; font-weight: bold; font-size: 20; border-radius: 10px;")
        
        self.title = QLabel("Select the file you recived from live pos")
        self.title.setFixedHeight(35)
        self.title.setMinimumWidth(50)
        self.title.setStyleSheet("background-color: white; padding: 5px; text-align: center; font-size: 20; border-radius: 10px;")
        self.titleL = QHBoxLayout()
        self.titleL.addWidget(self.title, alignment=Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignLeft)

        self.fname = QHBoxLayout()
        self.fname.addWidget(self.file_name, alignment=Qt.AlignmentFlag.AlignLeft)
        self.open_File = QPushButton("Select File")
        self.open_File.setFixedWidth(80)
        self.open_File.clicked.connect(self.find_file)
        self.open_File.setToolTip("Lets you Search For Files")
        

        # Empty labels for desgin reasons ༼ つ ◕_◕ ༽つ
        l1 = QLabel()
        l2 = QLabel()
        l3 = QLabel()

        self.afile = QHBoxLayout()
        self.afile.addWidget(self.open_File, alignment=Qt.AlignmentFlag.AlignLeft)
        self.afile.addWidget(self.file_path, alignment=Qt.AlignmentFlag.AlignLeft)
        
        # Adding the empty lables （￣︶￣）↗　
        self.afile.addWidget(l1, alignment=Qt.AlignmentFlag.AlignLeft)
        self.afile.addWidget(l2, alignment=Qt.AlignmentFlag.AlignLeft)
        self.afile.addWidget(l3, alignment=Qt.AlignmentFlag.AlignLeft)
        # works well ψ(｀∇´)ψ

        # Create a QWidget to act as a colored background
        background_widget = QWidget()
        background_widget.setStyleSheet("background-color: lightblue;")  # Set the background color

        # Adding Items to B3
        self.B3 = QVBoxLayout()
        self.B3.addLayout(self.titleL)
        self.B3.addLayout(self.fname)
        self.B3.addLayout(self.afile)

        self.datalay = QVBoxLayout()

        self.table_widget = QTableWidget()
        self.table_widget.setFixedSize(550, 320)
        self.table_widget.itemChanged.connect(self.on_item_changed)
        self.datalay.addWidget(self.table_widget, alignment= Qt.AlignmentFlag.AlignCenter) 
        self.row_mapping = {}  # Initialize a mapping to track QTableWidget rows and DataFrame rows

        self.load_button = QPushButton("Update File")
        self.load_button.clicked.connect(self.save_csv)
        self.datalay.addWidget(self.load_button)

        delete_button = QPushButton("Delete Selected Row")
        delete_button.clicked.connect(self.delete_selected_row)
        self.datalay.addWidget(delete_button)

        self.last_modified_time = None
        self.B4 = QHBoxLayout()
        self.B4.addLayout(self.datalay)
        

        # Setting each order 
        self.V1box = QVBoxLayout()
        # Adding each label to the layout
        # self.V1box.addWidget(self.input1)
        self.V1box.addLayout(self.B1)
        self.V1box.addLayout(self.B2)
        

        self.V2box = QVBoxLayout()
        # Adding each label to the layout
        self.V2box.addLayout(self.B3)
        self.V2box.addLayout(self.B4)

        self.Hbox = QHBoxLayout()
        self.Hbox.addLayout(self.V1box)
        self.Hbox.addLayout(self.V2box)
        
        main_container = QWidget()# alld widgets will be added to this
        main_container.setLayout(self.Hbox)#all widgets will be added to this
        # Set the central widget of the Window.
        self.setCentralWidget(main_container)
    
    def get_selected_row(self):
        return self.table_widget.currentRow()

    def delete_selected_row(self):
        selected_row = self.get_selected_row()
        try:
            # Find the corresponding DataFrame row using the mapping
            df_row = self.row_mapping[selected_row]
            # Remove the selected row from self.loaded_dataframe
            self.loaded_dataframe = self.loaded_dataframe.drop(df_row)
            # Update the mapping for remaining rows
            self.row_mapping = {table_row: df_row for table_row, df_row in enumerate(self.loaded_dataframe.index)}
            # Update the QTableWidget
            self.update_table_widget()
        except KeyError:
            print(f"KeyError: Row {selected_row} not found in mapping.")

    def update_table_widget(self):
        self.table_widget.setRowCount(len(self.loaded_dataframe))
        for table_row, (df_row, row_data) in enumerate(zip(self.loaded_dataframe.index, self.loaded_dataframe.values)):
            self.row_mapping[table_row] = df_row  # Update the mapping
            for col_index, cell_value in enumerate(row_data):
                item = QTableWidgetItem(str(cell_value))
                self.table_widget.setItem(table_row, col_index, item)
    
    def explorer(self):
        """
        Opens a file explorer dialog for the user to select a file.

        :return: The selected file name.
        """
        options = QFileDialog.Option.ReadOnly  # Make it read-only if necessary
        filters = "CSV Files (*.csv);;Text Files (*.txt);;All Files (*)"
        filename, _ = QFileDialog.getOpenFileName(window, "Select Files", "", filters, "", options=options)
        return filename
    
    def find_file(self):
        """
        Find a file and perform some operations based on the file name.

        This function first calls the `explorer` method to get a list of filenames.
        If the list is not empty, it creates a `Filesystem` object with the first filename
        in the list and adds a specific path to it. It then creates a `Sorter` object 
        with the `posPath` attribute of the `Filesystem` object. Finally, it sets the 
        text of `self.file_name` and `self.file_path` based on the filename.

        If the list of filenames is empty, it sets the text of `self.file_path` to 
        "File Not Found!, Please Try again".

        Parameters:
        None

        Returns:
        None
        """
        filenames = self.explorer()
        if filenames: 
            self.file = Filemanager.Filesystem(f"{filenames}")
            self.file.add_path("Files\Bobsmeat.csv")
            self.name = sorts.Sorter(self.file.posPath)          
            self.file_name.setText(os.path.splitext(os.path.basename(filenames))[0])
            self.file_path.setText(filenames)
        else:
            # self.file_path.setStyleSheet("color: red")
            self.file_path.setText("File Not Found!, Please Try again")
  
    def find_file2(self):
        """
        Finds a file using the `explorer` method and updates the file path and name labels accordingly.
        
        Parameters:
            None
            
        Returns:
            None
        """
        namea = self.explorer()
        try:
            if namea:
                self.labelFilePath.setText(f"{namea}")
                self.file.add_path(f"{namea}") 
                self.labelFileName.setText(os.path.splitext(os.path.basename(namea))[0])
                self.update_display()
            else:
                self.labelFilePath.setText("File Not Found!, Please Try again")
        except:
            self.labelFilePath.setText("File Not Found!, Please Try again")

    def on_item_changed(self, item):
        """
        Update the value in the loaded dataframe at the specified row and column.

        Parameters:
            item (QTableWidgetItem): The QTableWidgetItem object representing the cell in the table widget.

        Returns:
            None
        """
        row = item.row()
        col = item.column()
        new_value = item.text()
        self.loaded_dataframe.iat[row, col] = new_value
    
    def load_csv(self):
        """
        Load a CSV file and update the display if the file exists.

        Parameters:
            None

        Returns:
            None
        """
        
        if self.file.stockPath:
            self.last_modified_time = os.path.getmtime(self.file.stockPath)
            self.update_display()

    def check_for_updates(self):
        """
        Checks for updates in the stock file and updates the display if necessary.
        """
        if self.file.stockPath:
            current_modified_time = os.path.getmtime(self.file.stockPath)
            if current_modified_time != self.last_modified_time:
                self.last_modified_time = current_modified_time
                self.update_display()
   
    def save_csv(self):
        """
        Save the DataFrame as a CSV file.

        This function saves the DataFrame as a CSV file. If the loaded DataFrame is not None and the stock path is provided, it saves the DataFrame to the stock path using the `to_csv` method. It then updates the display to reflect the changes.

        If the DataFrame is not None and the stock path is provided, it saves the DataFrame to the stock path using the `to_csv` method. It also updates the display to reflect the changes.

        Parameters:
            None

        Returns:
            None
        """
        if self.loaded_dataframe is not None and self.file.stockPath:
            try:
                self.loaded_dataframe.to_csv(self.file.stockPath, index=False)
                # Reload the data to reflect changes
                self.update_display()
            except:
                pass
        if self.df is not None and self.file.stockPath:
            self.df.to_csv(self.file.stockPath, index=False)
            self.update_display()  # Reload the data to reflect changes

    def update_display(self):
        """
        Updates the display with the latest data from the stockPath file.

        This function reads the CSV file specified by `self.file.stockPath` and assigns the contents to the `self.df` variable.
        Then, it assigns the `self.df` variable to the `self.loaded_dataframe` variable.
        Finally, it calls the `self.display_dataframe()` method to display the updated dataframe.

        Parameters:
            None

        Returns:
            None
        """
        if self.file.stockPath:
            self.df = pd.read_csv(self.file.stockPath)
            self.loaded_dataframe = self.df
            self.display_dataframe()

    def display_dataframe(self):
        """
        Sets up the display of the dataframe in the table widget.

        This function sets the number of rows and columns in the table widget based on the shape of the dataframe.
        It also sets the horizontal header labels of the table widget to match the columns of the dataframe.

        Parameters:
            self (object): The instance of the class.
        
        Returns:
            None
        """
        self.table_widget.setRowCount(self.df.shape[0])
        self.table_widget.setColumnCount(self.df.shape[1])
        self.table_widget.setHorizontalHeaderLabels(self.df.columns)

        for row in range(self.df.shape[0]):
            for col in range(self.df.shape[1]):
                item = QTableWidgetItem(str(self.df.iloc[row, col]))
                self.table_widget.setItem(row, col, item)

    def no_file(self):
        """
        Displays an error message if no file is selected to read from.

        Parameters:
            self: The instance of the class.
        
        Returns:
            None
        """
        dlg = QMessageBox(self)
        dlg.setWindowTitle("Error")
        dlg.setText("Please Select A File To Read From")
        icon = QIcon("Files\error_logo.png")
        dlg.setWindowIcon(icon)
        button = dlg.exec()
        if button == QMessageBox.StandardButton.Ok:
            self.open_File.setFocus()    

    def create_new_file(self):
        """
        Creates a new file by opening a file dialog to select the location and name for the new file.
        
        Parameters:
            self (object): The instance of the class.
        
        Returns:
            None
        """
        # Open a file dialog to select the location and name for the new file
        options = QFileDialog.Option.ReadOnly
        file_dialog = QFileDialog()
        file_dialog.setDefaultSuffix(".csv")  # Set the default file extension if needed
        file_name, _ = file_dialog.getSaveFileName(
            self, "Save New File", "", "CSV Files (*.csv);;All Files (*)", options=options
        )

        if file_name:
            # Create the new file
            try:
                self.file.create_file(file_name)
                self.file.add_path(f"{file_name}")
                self.labelFilePath.setText(file_name)
                self.labelFileName.setText(os.path.splitext(os.path.basename(file_name))[0])
                self.update_display()
            except Exception as e:
                # Handle any errors that occur during file creation
                self.labelFilePath.setText(f"Error creating new file: {str(e)}")
            
    def get_data(self):
        """
        Appends data to a file, clears input fields, sets a placeholder text, and updates the display.

        Parameters:
            None

        Returns:
            None
        """
        self.file.append_to_file([self.skuf.text(),self.product_namef.text(),self.quantityf.text(),self.pricef.text()])
        (self.skuf.clear(),self.product_namef.clear(),self.quantityf.clear(),self.pricef.clear(),self.skuf.setFocus())
        self.product_namef.setPlaceholderText("Product Name")
        self.update_display()
        # return  self.skuf.text(),self.product_namef.text(),self.quantityf.text(),self.pricef.text()
        
    def to_large(self, holder):
        """
        Converts the given `holder` into a larger format and returns a boolean value indicating if the conversion was successful.

        Parameters:
            holder (list): A list containing elements to be converted.

        Returns:
            bool: True if the conversion was successful, False otherwise.
        """
        con = False
        array = []
        for items in enumerate(holder):
            array.append(items[1][2])
        self.rals = array
        try:
            if array[1]:
                con = True
        except IndexError:
            pass

        return con 

    def scanned_entry(self):
        """
        Generate the function comment for the given function body.

        This function is responsible for handling the scanned entry. It performs the following steps:
        1. Initializes the variable 'sorte' as an empty string.
        2. Tries to assign the value of 'sorts.Sorter(self.file.posPath)' to 'sorte' if 'self.file.posPath' is truthy.
        3. Catches any exceptions raised and calls the 'self.no_file()' method.
        4. Tries to perform the following steps if the length of 'self.skuf.text()' is greater than or equal to 6:
            a. Calls the 'sorte.complete(self.skuf.text())' method.
            b. If the method call returns a truthy value, sets the text of 'self.product_namef' to the value of 'sorte.complete(self.skuf.text())[0][2]'.
                Sets the focus to 'self.quantityf'.
            c. If the method call returns a falsy value, sets the placeholder text of 'self.product_namef' to "Item not found".
                Sets the focus to 'self.product_namef'.
        5. Catches any exceptions raised and sets the placeholder text of 'self.product_namef' to "Item not found".
            Sets the focus to 'self.product_namef'.

        This function does not have any parameters.

        This function does not return anything.
        """
        sorte = ""
        try:
            if self.file.posPath:
                sorte = sorts.Sorter(self.file.posPath)
        except:
            self.no_file()  

        try:
          if len(self.skuf.text()) >= 6:
            if sorte.complete(self.skuf.text()):
                    if self.to_large(sorte.complete(self.skuf.text())):
                        # self.product_namef.setText(self.rals[0])
                        self.button_clicked(True)
                        print("setp 2")
                        
                        self.quantityf.setFocus()
                    else:
                        # print("setp 2.0")
                        self.product_namef.setText(sorte.complete(self.skuf.text())[0][2])
                        self.quantityf.setFocus()
            else: self.product_namef.setPlaceholderText("Item not found"); self.product_namef.setFocus()
        except:
            self.product_namef.setPlaceholderText("Item not found")
            self.product_namef.setFocus()
    def button_clicked(self, checked):
        self.w = AnotherWindow(self.rals)
        print(self.w.selected_item)
        self.w.show()

app = QApplication([])
icon = QIcon("Files\com_logo.png")
window = Mainface()
window.setWindowIcon(icon)
window.show()
app.exec()
