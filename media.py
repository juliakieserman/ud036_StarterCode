import webbrowser


class Movie:
    """Class to represent movie and associated attributes"""
    def __init__(self, title, storyline,
                 poster_image_url, trailer_youtube_url):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    def show_trailer(self):
        """Open object trailer in a web browser"""
        webbrowser.open(self.trailer_youtube_url)
