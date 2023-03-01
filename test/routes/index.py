# We need to import the render_template and Blueprint classes so that we can
# run our simple functions
from flask import render_template, Blueprint


# This is the name of the class we will import in the main file
class Index:

    def __init__(self, username):
        self.username = username
        self.index = self.create_index()

    # This is the function that actually creates the blueprint
    def create_index(self):
               
        index_page = Blueprint("index", __name__)       
        @index_page.route("/", methods=['GET'])       
        def index():           
            return render_template("index.html", username=self.username)

        
        return index_page
