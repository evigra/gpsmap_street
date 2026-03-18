{
    'name' : 'GPSMap - Street',
    'price' : '89.0',
    'currency' : 'EUR',
    'license' : 'LGPL-3',
    'images': ['static/description/map_online.png'],

    'author': "SolesGPS :: Eduardo Vizcaino",
    'category': 'Human Resources/Fleet GPS',
    "version": "16.0.0.0.0",
    'website' : 'https://solesgps.com',
    'summary' : 'Note the location of the coordinates at street level, using Google Street View',
    'depends': [
        'gpsmap',
    ],
    'data': [
        # VIEW
        'views/menuitem.xml',
    ],
    'assets': {
        'web.assets_backend': [
            '/gpsmap_street/static/js/AbstractAction.js',
            '/gpsmap_street/static/xml/*.xml',
        ],
        'web.assets_qweb': [
            '/gpsmap_street/static/xml/*.xml',
        ],        
    },    
    #'demo': ['data/demo.xml'],
    'installable': True,
    'application': False,
}