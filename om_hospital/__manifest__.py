{
    'name': 'Hospital Management',
    'version':'1.0.0',
    'sequence': -100,
    'depends': ['mail', 'product'],
    'category': 'Hospital',
    'description': """Hospital management system""",
    'data':[
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/patient_view.xml',
        'views/female_patient_view.xml',
        'views/appointment_view.xml',
    ],
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
