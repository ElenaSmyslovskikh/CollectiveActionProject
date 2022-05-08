from os import environ

SESSION_CONFIGS = [
    dict(
        name='colactionsurvey',
        display_name='Опрос студентов московских вузов',
        app_sequence=['colactionsurvey'],
        num_demo_participants=1,
        treatment=None
    ),
    # dict(
    #     name='colactionsurvey_ingroup_success',
    #     display_name='Опрос студентов московских вузов - ingroup_success',
    #     app_sequence=['colactionsurvey'],
    #     num_demo_participants=1,
    #     treatment='ingroup_success'
    # ),
    # dict(
    #     name='colactionsurvey_ingroup_failure',
    #     display_name='Опрос студентов московских вузов - ingroup_failure',
    #     app_sequence=['colactionsurvey'],
    #     num_demo_participants=1,
    #     treatment='ingroup_failure'
    #     ),
    # dict(
    #     name='colactionsurvey_outgroup_success',
    #     display_name='Опрос студентов московских вузов - outgroup_success',
    #     app_sequence=['colactionsurvey'],
    #     num_demo_participants=1,
    #     treatment='outgroup_success'
    #     ),
    #
    # dict(
    #     name='colactionsurvey_outgroup_failure',
    #     display_name='Опрос студентов московских вузов - outgroup_failure',
    #     app_sequence=['colactionsurvey'],
    #     num_demo_participants=1,
    #     treatment='outgroup_failure'
    #     ),
    # dict(
    #     name='colactionsurvey_control',
    #     display_name='Опрос студентов московских вузов - control',
    #     app_sequence=['colactionsurvey'],
    #     num_demo_participants=1,
    #     treatment='control'
    #     ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = []
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

if environ.get('OTREE_PRODUCTION') not in {None, '', '0'}:
    DEBUG = True
else:
    DEBUG = False

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '1119431484832'

ROOMS = [
    dict(
        name='colactionsurvey_test',
        display_name='Опрос студентов московских вузов_test',
        participant_label_file='_rooms/participant_.txt',
        use_secure_urls=True
    ),
    dict(
        name='colactionsurvey',
        display_name='Опрос студентов московских вузов',
        participant_label_file='_rooms/participant.txt',
        use_secure_urls=True
    ),
]
