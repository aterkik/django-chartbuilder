====================
Django Chartbuilder
====================

A simple Django application for integrating
`Chartbuilder <https://github.com/Quartz/Chartbuilder/>`_.

Install
-------
     ``pip install django_chartbuilder``
     
Quick start
-----------

1. Add ``django_chartbuilder`` to your ``INSTALLED_APPS`` setting::

    INSTALLED_APPS = (
        ...
        'django_chartbuilder',
    )

2. Include the django-chartbuilder URLconf in your project ``urls.py``::

    url(r'^/chartbuilder/$', include('django_chartbuilder.urls')),

3. Navigate to ``/chartbuilder/`` to get the default styled Chartbuilder
   chart generator (i.e. identical to http://quartz.github.io/Chartbuilder/)


Customization
-------------

You can extend the ``chartbuilder.html`` template to customize the chart
generator.

In your project's ``templates/django_chartbuilder/`` directory, create a
template ``chartbuilder.html`` and extend
``djangno_chartbuilder/index.html``::

        <!-- templates/django_chartbuilder/chartbuilder.html -->
        {% extends "django_chartbuilder/index.html" %}
        
        {% block title %}My Custom Chartbuilder Generator{% endblock %}
    
        {% block extrajs %}
            <script src="some_random_script.js"></script>
        {% endblock %}


Take a look at ``django_chartbuilder/templates/django_chartbuilder/index.html``
to find out (a lot of) additional sections you can override.

License
-------
MIT
