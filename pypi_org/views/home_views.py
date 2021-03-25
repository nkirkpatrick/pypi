import flask
import services.package_service as package_service 
#from infrastructure.view_modifiers import response
#from pypi_org.infrastructure.view_modifiers import response

blueprint = flask.Blueprint('home', __name__, template_folder='templates')

@blueprint.route('/')
# @app.route('/')
# @response(template_file='home/index.html')
def index():
    test_packages = package_service.get_latest_packages()
    #return {'packages': test_packages}
    return flask.render_template('home/index.html', packages=test_packages)


@blueprint.route('/about')
# @app.route('/about')
# @response(template_file='home/about.html')
def about():
    return flask.render_template('home/about.html')

