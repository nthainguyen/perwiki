from flask_login import current_user
from flask_nav import Nav
from flask_nav.elements import Navbar, View, Subgroup
from flask import current_app

def mynavbar():
    return Navbar(current_app.config.get('SITE_NAME'),
                 )

def secnavbar():
    secnav = list(mynavbar().items)

    if current_user.is_authenticated:
        secnav.extend([
                View('Wiki', 'Wiki'),
                ])
        secnav.append(View('Log out', 'Logout'))
    else:
        secnav.append(View('Log in', 'Login'))
        secnav.append(View('Register', 'Register'))

    return Navbar(current_app.config.get('SITE_NAME'), *secnav)


def configure_nav(app):
    nav = Nav()
    nav.register_element('mynavbar', mynavbar)
    nav.register_element('secnavbar', secnavbar)
    nav.init_app(app)
