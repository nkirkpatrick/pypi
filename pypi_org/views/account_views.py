import flask

blueprint = flask.Blueprint('account', __name__, template_folder='templates')

# ############################# INDEX #######################################

@blueprint.route('/account')
# @app.route('/')
# @response(template_file='home/index.html')
def index():
    #test_packages = package_service.get_latest_packages()
    #return {'packages': test_packages}
    return flask.render_template('account/index.html', {})

# ############################# REGISTER #######################################

@blueprint.route('/account/register', methods=['GET'])
# @app.route('/')
# @response(template_file='home/index.html')
def register_get():
    #test_packages = package_service.get_latest_packages()
    #return {'packages': test_packages}
    return flask.render_template('account/register.html', {})

@blueprint.route('/account/register', methods=['POST'])
# @app.route('/')
# @response(template_file='home/index.html')
def register_post():
    #test_packages = package_service.get_latest_packages()
    #return {'packages': test_packages}
    return flask.render_template('account/register.html', {})

# ############################# LOGIN #######################################

@blueprint.route('/account/login', methods=['GET'])
# @app.route('/')
# @response(template_file='home/index.html')
def login_get():
    #test_packages = package_service.get_latest_packages()
    #return {'packages': test_packages}
    return flask.render_template('account/login.html', {})

@blueprint.route('/account/login', methods=['POST'])
# @app.route('/')
# @response(template_file='home/index.html')
def login_post():
    #test_packages = package_service.get_latest_packages()
    #return {'packages': test_packages}
    return flask.render_template('account/login.html', {})

# ############################# LOGOUT #######################################

@blueprint.route('/account/logout')
# @app.route('/')
# @response(template_file='home/index.html')
def logout():
    #test_packages = package_service.get_latest_packages()
    #return {'packages': test_packages}
    return flask.render_template({})

