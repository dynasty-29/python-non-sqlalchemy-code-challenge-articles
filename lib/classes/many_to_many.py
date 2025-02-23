class Article:
    # I expect more articles so i will store them in this list
    all = []
    
    def __init__(self, author, magazine, title):
        # ensuring author is from Author class
        if not isinstance(author, Author):
            raise TypeError("Author must be an instance of Author class.") 
        #Ensuring magazine is part of Magazine class
        if not isinstance(magazine,Magazine):
            raise TypeError("Magazine must be an instance of Magazine class.")       
        # Titles must be between 5 and 50 characters, inclusive
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters.") 
        self.author = author
        self.magazine = magazine
        self.title = title
        # adding all articles togthet into our class list
        Article.all.append(self)
        
     
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, new_title):
        if not isinstance(new_title, str) or not (5 <= len(new_title) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters.")
        self._title = new_title
        
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, new_author):
        if not isinstance(new_author, Author):
            raise TypeError("Author must be an instance of Author class.")
        self._author = new_author
    
    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, new_magazine):
        if not isinstance(new_magazine, Magazine):
            raise TypeError("Magazine must be an instance of Magazine class.")
        self._magazine = new_magazine    
class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string")
        if hasattr(self, "name"):
            raise AttributeError("Cannot change name after instantiation")
        self._name = name
    
    @property
    def name(self):
        return self._name
        
    # Returns the author object for that article
    # Must be of type Author
    # Authors can be changed after the article object is initialized  
    def articles(self):
        return [article for article in Article.all if article.author == self]

    # Returns the magazine object for that article
    # Must be of type Magazine
    # Magazines can be changed after the article object is initialized
    def magazines(self):
        # going through all articles and check if its a type of magazine
        # once done we set it into a list that will return
        return list(set(article.magazine for article in self.articles()))
              

    # Receives a Magazine instance, and a title as arguments
    # Creates and returns a new Article instance and associates it with that author, the magazine provided
    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    # Returns a unique list of strings with the categories of the magazines the author has contributed to
    # Returns None if the author has no articles
    def topic_areas(self):
        return list(set(my_topics.category for my_topics in self.magazines())) or None
            
        

class Magazine:
    # There can be more than one magazine by same authour so i will store them in this list
    all = []
    
    def __init__(self, name, category):
        # Names must be between 2 and 16 characters, inclusive
        if not isinstance(name, str) or not (2 <= len(name) <=16):
            raise ValueError("Name must be a string between 2 and 16 characters, inclusive")
        
        # Categories must be longer than 0 characters
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Category must be non-empty string") 
        self._name = name
        self._category = category
        
        # adding all magazines to the class
        Magazine.all.append(self)
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str) or not (2 <= len(new_name) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters.")
        self._name = new_name

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, new_category):
        if not isinstance(new_category, str) or len(new_category) == 0:
            raise ValueError("Category must be a non-empty string.")
        self._category = new_category   
    # Returns a list of all the articles the magazine has published
    # Must be of type Article      
    def articles(self):
        #returning a list of articles
        #  iterating through every article in the article class list to get articles that the magazine has published and add then to our empty list
        return [article for article in Article.all if article.magazine == self]
    
    # Returns a unique list of authors who have written for this magazine
    # Must be of type Author    
    def contributors(self):
        # list of unique authors
        return list(set(article.author for article in self.articles()))
          

    # Returns a list of the titles strings of all articles written for that magazine
    # Returns None if the magazine has no articles
    def article_titles(self):
        # the list will store our title atrings
        return [article.title for article in self.articles()] or None
            
    # Returns a list of authors who have written more than 2 articles for the magazine
    # Authors must be of type Author
    #Returns None if the magazine has no authors with more than 2 publications
    def contributing_authors(self):
        # store our list of authors and the count of articles authored in a dictionary
        count_authors = {}
        
        # go over every article checking for authors with more than 2 articles
        for article in self.articles():
            # checking the new encountered author already in my dict
            #  if already we keep the count of their article by adding 1
            count_authors[article.author] = count_authors.get(article.author, 0) + 1
        # once we have gone throw all articles and kept count of how many each author has authored we need to return authors who has written more than 2 artcles
        # there will now go throught the dictionary we created shoul dbe with a key for author and a value of number of articles authored
        #  will now store our list of authors in a list
        top_authors = [author for author, count in count_authors.items() if count > 2]
        return top_authors or None
    
    # Magazine classmethod top_publisher()
    #     Returns the Magazine instance with the most articles
    #     Returns None if there are no articles.
    #     Uncomment lines 206-224 in the magazine_test file
    #     hint: will need a way to remember all magazine objects      
    @classmethod
    def top_publisher(cls):
        # ensureing we have articles first and if not return none
        if not Article.all:
            return None
        # also returning magazine instance with most articles
        return max(cls.all, key=lambda mag: len(mag.articles()))   