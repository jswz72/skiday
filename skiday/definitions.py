import os

_ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
DATA_PATH = os.path.join(_ROOT_DIR, 'data/')
DB_PATH = os.path.join(DATA_PATH, 'data.db')

RESORTS = [{
    'name': 'cannon',
    'display': 'Cannon Mountain',
    'webpage': 'https://www.cannonmt.com/mountain-report'
    }]
METRICS = ['hours', 'snow', 'trails', 'lifts']
