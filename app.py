###
# TODO
# track current page
# move get_clothes to a service
#   get urls based on gender and category selected
###

# run script for windows
# ${env:FLASK_APP}='app.py'; ${env:FLASK_ENV}='development'; flask run

from models.Websites import Websites
from models.UserSettings import UserSettings
from models.Genders import Genders
from models.Categories import Categories
from services.scrapers import scrape_website
import flask

app = flask.Flask(__name__)
user_settings = UserSettings()

@app.route("/", methods=['GET'])
def index():
    get_clothes()
    return flask.render_template('index.html', websites = Websites, user_settings = user_settings)

def get_clothes():
    for website in Websites:
        if website.get('id') in user_settings.websites:
            scrape_website(user_settings, website)

@app.route("/config", methods=['GET', 'POST'])
def config():
    if flask.request.method == 'POST':       
        user_settings.save_settings(flask.request.json)
        return flask.url_for('index')
    else:
        return flask.render_template('config.html', websites = Websites, genders = Genders, categories = Categories, user_settings = user_settings)
