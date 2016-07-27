## @package webapp.assets
# defines all assets
from flask_assets import Bundle

## a bundle of CSS Files
common_css = Bundle(
    'css/bootstrap.min.css',
    'css/bootstrap-theme.min.css',
     output='public/css/common.css')

## a bundle of JS Files
common_js = Bundle(
    'js/jquery.min.js',
    'js/bootstrap.min.js',
    'js/app.js',
    output='public/js/common.js')
