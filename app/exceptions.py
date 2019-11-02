class ValidationError(ValueError):
    pass


# @app.errorhandler(CSRFError)
# def handle_csrf_error(e):
#     return render_template('csrf_error.html', reason=e.description), 400


# NB: for later use.
# from .decorators import admin_required, permission_required
# 
# @main.route('/admin')
# @login_required
# @admin_required
# def for_admins_only():
# 	return "For administrators!"

# @main.route('/moderate')
# @login_required
# @permission_required(Permission.MODERATE)
# def for_moderators_only():
# 	return "For comment moderators!"