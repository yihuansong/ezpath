DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'ezpath',                      # Or path to database file if using sqlite3.
        'USER': 'root',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                    # Set to empty string for default. Not used with sqlite3.
        # 'OPTIONS': {
        #   'autocommit': True,
        # },
    },
    'ezpathdb': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'ezpathdb',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    },
}
