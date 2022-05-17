class MediaItem: #class for media created)
    def __init__(self,media=None,title=None,price=None,ref=None,director=None,lead_actor=None,author=None): #defines attributes
        self.media=media #allows other parts of program to use via .self
        self.title=title
        self.price=price
        self.ref=ref
        self.director=director
        self.lead_actor=lead_actor
        self.author=author
        