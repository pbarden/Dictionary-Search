"""
monograph.py
@Paul Barden

Module to handle dictionary data from Webster's Unabridged English Dictionary (Gutenberg Project, compiled 8/22/09)
"""
import json

class Word:
    """
    Parameters
    -----------
    w : str
        The word
    d : str
        Definition of the word

    Attributes
    -----------
    w : str
        The word
    d : str
        Definition of the word

    Methods
    -----------
    show()
        Returns the word
    define()
        Returns the definition
    change()
        Changes the word
    means()
        Changes the definition
    """
    def __init__(self, w="None", d=""):
        self.w = w.lower()
        self.d = d

    def show(self):
        return self.w
    
    def define(self):
        return self.d

    def change(self, nw):
        """
        Parameters
        -----------
        nw : str
            The new word that will replace the old word
        """
        self.w = nw
    
    def means(self, dls):
        """
        Parameters
        -----------
        dls : str
            The new definition that will replace the old definition
        """
        self.d = dls

class LanguageDictionary:
    """
    Parameters
    -----------
    fp : str
        File path to dictionary data in JSON format
    lang : str (optional)
        Language declaration for dictionary (default: "en")

    Attributes
    -----------
    lang : str
        Represents dictionary language
    contents : library
        Stores all words and definitions as keys and values

    Methods
    -----------
    open()
        Opens a dictionary file to replace dictionary contents
    dump()
        Returns all dictionary data as library
    query()
        Returns definition of word used in query
    check()
        Returns a boolean value if term is in dictionary
    """
    def __init__(self, fp="", lang="en"):
        self.lang = lang

        try:
            e_raised = False
            new_dictionary = json.load(open(fp))
        except FileNotFoundError:
            print("Could not add data to new language dictionary: File not found.")
            e_raised = True
        except:
            print("Could not add data to new language dictionary: An error occurred.")
            e_raised = True
        finally:
            if e_raised:
                self.contents = {}
            else:
                self.contents = new_dictionary 
        
    def open(self, f_name):
        """
        Parameters
        -----------
        f_name : str
            File path to dictionary data in JSON format
        """
        try:
            e_raised = False
            new_dictionary = json.load(open(f_name))
        except FileNotFoundError:
            print("Could not create new language dictionary: File not found.")
            e_raised = True
        except:
            print("Could not create new language dictionary: An error occurred.")
            e_raised = True
        finally:
            if e_raised:
                self.contents = {}
            else:
                self.contents = new_dictionary
    
    def dump(self):
        return self.contents
    
    def query(self, s_term):
        """
        Parameters
        -----------
        s_term : str
            Term to search against words stored in dictionary
        """
        try:
            if s_term in self.contents.keys():
                return self.contents[s_term]
            else:
                return ""
        except:
            print("An error occured - please try again.")
            return ""
    
    def check(self, s_term):
        """
        Parameters
        -----------
        s_term : str
            Term to search against words stored in dictionary
        """
        if s_term in self.contents:
            return True
        else:
            return False