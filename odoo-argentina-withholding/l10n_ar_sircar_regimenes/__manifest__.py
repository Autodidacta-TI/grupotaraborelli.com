{
    'name': 'SIRCAR Regimenes de Provincias',
    'license': 'AGPL-3',
    'author': 'Exemax, Codize',
    'category': 'Accounting & Finance',
    'data': [
        'views/sircar_regimenes_views.xml',
        'security/ir.model.access.csv',
        'data/regimen_data.xml'
    ],
    'depends': [
        'base',
        'contacts',
        'account',
        'l10n_ar',
    ],
    'installable': True,
    'version': '14.0.1.0.0',
}
