# Django Upwork portfolio

Simple portfolio website based on Django. It pulls the data from the Upwork's API.

### Live demo

[dionysio.com](https://www.dionysio.com)

### Acknowledgements

* HTML template based off [devportfolio-template](https://github.com/RyanFitzgerald/devportfolio-template) by Ryan Fitzgerald
* [python-upwork](https://github.com/TechnicalBro/python-upwork) which is a Python 3 wrapper around the Upwork API

### Reusing this project

Customize the [templates](base/templates) to your liking. Then you have to set the correct configuration in [secrets.py](portfolio/settings/secrets.py):
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = ''

DATABASES = {
    'default': {
        'ENGINE': '',
        'NAME': '',
    }
}

UPWORK_KEYS = {
    'public_key': '',
    'secret_key': '',
    'oauth_access_token': '',
    'oauth_access_token_secret': ''
}

UPWORK_PROFILE_ID = ''

CACHES = {
    'default': {
        'BACKEND': '',
        'LOCATION': '',
    }
}

EMAIL_HOST = ''
```


### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details