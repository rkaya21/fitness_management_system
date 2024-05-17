import tkinter as tk
from tkinter import messagebox
from database import Database

class FitnessApp:
    def __init__(self, root):
        self.db = Database()

        self.root = root # Create the main window.
        self.root.title("Fitness Management System")

        self.create_widgets() # Create the interface components.

