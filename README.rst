Digital Saarthi
===============

digital saarthi


Basic Commands
--------------

Celery
^^^^^^

This app comes with Celery.

To run a celery worker:

.. code-block:: bash

    cd digital_saarthi
    celery -A config.celery_app worker -l info

Please note: For Celery's import magic to work, it is important *where* the celery commands are run. If you are in the same folder with *manage.py*, you should be right.




