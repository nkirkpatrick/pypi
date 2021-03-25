import flask
import services.package_service as package_service 
#from infrastructure.view_modifiers import response
#from pypi_org.infrastructure.view_modifiers import response

blueprint = flask.Blueprint('packages', __name__, template_folder='templates')

@blueprint.route('/project/<package_name>')
# @app.route('/')
# @response(template_file='home/index.html')
def package_details(package_name: str):
    return "Package details for {}".format(package_name)
    #test_packages = package_service.get_latest_packages()
    #return {'packages': test_packages}
    #return flask.render_template('packages/details.html', packages=test_packages)


@blueprint.route('/<int:rank>')
def popular(rank: int):
    return "The details for the {}th most popular package".format(rank)
