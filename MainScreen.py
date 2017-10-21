import tkMessageBox

from tkinter import *

from Solution import Solution


class MainScreen:
    """
    This class is responsible creating the frame and various components of the GUI
    """

    def __init__(self):
        """
        Constructor for the class
        """
        self.__init_main_screen()

    def __init_main_screen(self):
        """
        This method is responsible for the creation of frame
        :return:nothing
        """
        self.__main_screen = Tk()
        self.__main_screen.title("CHEERS")
        self.__main_screen.minsize(450, 300)
        self.__main_screen.maxsize(450, 300)
        self.__create_items()

    def __create_items(self):
        """
        This method is creation of various components of GUI
        :return:nothing
        """
        menu_bar = Menu(self.__main_screen)

        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="About", command=self.__show_description)
        file_menu.add_separator()
        file_menu.add_command(label="Save", command=self.__save)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.__exit)

        menu_bar.add_cascade(label="File", menu=file_menu)

        frame = Frame(self.__main_screen, borderwidth=2, padx=10, pady=10)

        lbl_radius = Label(frame, text="Coaster Radius:")
        lbl_radius.pack(side=LEFT, fill=NONE, expand=NO)

        self.__txt_radius = Entry(frame)
        self.__txt_radius.pack(side=LEFT, fill=BOTH, expand=YES, padx=12)

        btn_calculate = Button(frame, text="Calculate", command=self.__calculate_length)
        btn_calculate.pack(side=LEFT, fill=NONE, expand=NO)

        result_frame = Frame(self.__main_screen, borderwidth=2, padx=10, pady=5)

        lbl_result = Label(result_frame, text="Result: ", anchor=W, pady=5)
        lbl_result.pack(side=TOP, fill=X, expand=YES)

        self.__txt_result = Text(result_frame)
        self.__txt_result.config(state=DISABLED)

        scroll_bar = Scrollbar(result_frame, orient=VERTICAL, command=self.__txt_result.yview)

        self.__txt_result['yscroll'] = scroll_bar.set
        scroll_bar.pack(side=RIGHT, fill=Y)
        self.__txt_result.pack(side=TOP, fill=BOTH, expand=YES)

        frame.pack(side=TOP, fill=X, expand=YES)
        result_frame.pack(side=TOP, fill=BOTH, expand=YES)

        self.__main_screen.config(menu=menu_bar)

    def __calculate_length(self):
        """
        This method is responsible for calculating the length between the Coasters
        :return:nothing
        """
        try:
            if self.__txt_radius.get() == "":
                tkMessageBox.showwarning("Invalid Output", "The radius field can't be empty")
            else:
                length = Solution.get_length(float(self.__txt_radius.get()))
                self.__txt_result.config(state=NORMAL)
                result = "Result for Radius:" + str(self.__txt_radius.get()) + "\n" + "Alpha:" + str(
                    Solution.get_alpha()) + \
                         "\n" + "Length:" + str(length) + "\n\n"
                self.__txt_result.insert(END, result)
                self.__txt_result.config(state=DISABLED)
        except BaseException as e:
            if e.message.__contains__("could not convert string to float:"):
                tkMessageBox.showwarning("Error", "Please enter a number!!!!")
            else:
                tkMessageBox.showwarning("Error", e.message)

    @staticmethod
    def __show_description():
        """
        This method is responsible for showing the description of the project
        :return:nothing
        """
        tkMessageBox.showinfo("Description",
                              "Suppose there are two circular beverage coasters of equal area.The purpose is to find "
                              "how far the two coasters need to be moved on top of each other,such that the area of the"
                              "overlapping region is half the area of any of the coasters.The input should be the "
                              "radius of the circles and the output would be the distance at which coasters must be "
                              "placed in order to meet the condition."
                              "\n\nImage ref. -\nhttp://users.encs.concordia.ca/~kamthan/courses/soen-6441/"
                              "project_description.pdf")

    def display(self):
        """
        This method makes the window to be displayed
        :return:nothing
        """
        self.__main_screen.mainloop()

    def __save(self):
        """
        This method is responsible for saving of the functionality not yet implemented
        :return:nothing
        """
        pass

    @staticmethod
    def __exit(self):
        """
        This method is responsible for closing the application
        :return:nothing
        """
        sys.exit()
