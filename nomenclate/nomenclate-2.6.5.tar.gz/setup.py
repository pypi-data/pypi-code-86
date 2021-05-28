# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nomenclate', 'nomenclate.core']

package_data = \
{'': ['*'], 'nomenclate.core': ['template/*']}

install_requires = \
['PyYAML>=5.4.1,<6.0.0',
 'python-dateutil>=2.8.1,<3.0.0',
 'toml>=0.10.2,<0.11.0']

setup_kwargs = {
    'name': 'nomenclate',
    'version': '2.6.5',
    'description': 'A tool set for automating and generating strings based on arbitrary user-defined naming conventions.',
    'long_description': '###############################################################################################################\nNomenclate: A tool set for automating and generating strings based on arbitrary user-defined naming conventions\n###############################################################################################################\n\n`Online Documentation (ReadTheDocs) <http://nomenclate.readthedocs.io/en/latest/>`_\n\n.. image:: https://readthedocs.org/projects/nomenclate/badge/?version=latest\n    :target: http://nomenclate.readthedocs.io/en/latest/?badge=latest\n    :alt: Documentation Status\n\n.. image:: https://badge.fury.io/py/nomenclate.svg\n    :target: https://badge.fury.io/py/nomenclate\n\n.. image:: https://circleci.com/gh/AndresMWeber/Nomenclate.svg?style=svg\n    :target: https://circleci.com/gh/AndresMWeber/Nomenclate\n\n.. image:: https://coveralls.io/repos/github/AndresMWeber/Nomenclate/badge.svg?branch=master\n    :target: https://coveralls.io/github/AndresMWeber/Nomenclate?branch=master\n\n.. image:: https://img.shields.io/pypi/pyversions/nomenclate.svg\n   :target: https://pypi.python.org/pypi/nomenclate\n\n.. contents::\n\n.. section-numbering::\n\nSynopsis\n########\n\nNomenclate is a tool which creates persistent objects that can be used to generate strings that follow naming\nconventions that you designate.\nThere are sets of current naming conventions (format strings) that can be replaced or extended following certain rules\nfor creation. You can add arbitrary tokens as needed and register token filtering of your own designation.\n\nThere is a full set of YAML defined suffix/side substitution strings which gets created in `~/.nomenclate.yml`.  This is where you can customize your configuration.\n\nConcept Definitions\n*******************\ntoken\n    : A component of the format string which is a meaningful symbol/definition pair that will be filtered by\n    a grammar of regular expressions.\n    A simplified representation could be token=value wherein the token (as found in the format string) will be resolved\n    to the value as is adheres to the token\'s syntax/grammar rules\n\nformat string\n    : A string that represents a series of tokens separated with arbitrary delimiters.\n\n    e.g. - ``side_location_nameDecoratorVar_childtype_purpose_type``\n\n    Note: Nomenclate automatically supports camelCasing the tokens to separate them as a natural delimiter.\n\n`For a review of parsing/composition look here <https://en.wikipedia.org/wiki/Parsing>`_\n\nFeatures\n********\n-  Applies a naming convention with arbitrary syntax/grammar to the formatting of string tokens\n-  Top down parsing of format string given token-specific grammar rule classes that are extensible\n-  Persistent state object instances\n-  Up to date with online help docs\n-  User-customizable YAML/human-readable config file\n-  Easy object property or dictionary state manipulation\n-  Cross-Python compatible: Tested and working with Python 3.6, 3.7 and 3.8\n-  Cross-Platform compatible: Works under Linux, Mac OS ,Windows environments\n-  Full module/class documentation\n-  Sensible token value entry/conversion (like ``side=\'left\'`` with automatic token syntax replacement)\n\nInstallation\n############\nWindows, etc.\n*************\nA universal installation method (that works on Windows, Mac OS X, Linux, ..., and always provides the latest version) is to use `pip`:\n\n.. code-block:: bash\n\n    $ pip install Nomenclate\n\n.. code-block:: bash\n\n    $ poetry add Nomenclate\n\n\n(If ``pip`` installation fails for some reason, you can try ``easy_install nomenclate`` as a fallback.)\n\nUsage\n########\n\nPython Package Usage\n********************\nUse this tool via package level functions\n\n.. code-block:: python\n\n    import nomenclate\n    # Create empty name object\n    nomenclate_empty = nomenclate.Nom()\n\n    # At any time you can query the state of the nomenclate object through the state property\n    >>> nomenclate_empty.state\n    {\'name\': \'\', \'childtype\': \'\', \'location\': \'\', \'var\': \'\', \'type\': \'\', \'side\': \'\', \'decorator\': \'\', \'purpose\': \'\'}\n\n    # You can also create a nomenclate with initialized kwargs\n    nomenclate_init_kwargs = nomenclate.Nom(name=\'test\', type=\'group\')\n\n    # Your Nomenclate object has now been initialized and all of the default token set have been added based on\n    # The default format_string property from the `~/.nomenclate.yml` config file\n    # default: side_location_nameDecoratorVar_childtype_purpose_type\n    >>> nomenclate_init_kwargs.state\n    {\'name\': \'test\', \'childtype\': \'\', \'location\': \'\', \'var\': \'\', \'type\': \'group\', \'side\': \'\', \'decorator\': \'\', \'purpose\': \'\'}\n\n    # Feel free to manipulate each token\'s value on a property basis\n    >>> nomenclate_init_kwargs.location = \'rear\'\n\n    # Now that you\'re all set up you can use the get method to obtain a string representation of your conventionalized output:\n    >>> nomenclate_init_kwargs.get()\n    \'rr_test_GRP\'\n\n    # As you\'ll notice both tokens group and location have been composed following the replacements that can be found in the config YAML file.  This way things like "left" just need to be entered as "left" and then based on the yaml will replace automatically with anything you want.  Finally you don\'t need to enter things like "L" and worry about it later on!\n\n    # The format string will automate the process of hot swapping naming formats allows any string to be input.\n    >>> nomenclate_init_kwargs.format\n    \'side_location_nameDecoratorVar_childtype_purpose_type\'\n    >>> nomenclate_init_kwargs.format = \'name_type\'\n    >>> nomenclate_init_kwargs.state\n    {name:\'test\', type=\'group\'}\n\n    # You can enter static text that will always be present in the name by surrounding with parenthesis\n    # For now they only support alphanumeric characters.\n\n    >>> nomenclate_init_kwargs.format = \'side_location_nameDecoratorVar_(static.text)childtype_purpose_type\'\n    >>> nomenclate_init_kwargs.name = \'test\'\n    >>> nomenclate_init_kwargs.location = \'rear\'\n    >>> nomenclate_init_kwargs.type = \'group\'\n    \'rr_test_staticText_GRP\'\n\n    # Now entering all these values by properties is fun and all, however there is a convenience function that can digest dictionaries\n    >>> test_nom = nomenclate.Nom()\n    >>> test_nom.merge_serialization({\'name\':\'test\', \'location\':\'rear\', \'type\':\'group\'})\n    >>> test_nom.get()\n\n    # As you might have guessed, using state and merge_serialization you can pass naming values from instance to instance (as you can see __eq__ has been defined for Nomenclate instances):\n    >>> nom_a = nomenclate.Nom(name=\'test\', location=\'rear\')\n    >>> nom_b = nomenclate.Nom()\n    >>> nom_b == nom_a\n    False\n    >>> nom_b.merge_serialization(nom_a.state)\n    >>> nom_b == nom_a\n    True\n\n    # Optionally you can just pass the nomenclate object itself\n    >>> nom_b.token_dict.reset() # Internal function to be made into a public method later...\n    >>> nom_b == nom_a\n    False\n    >>> nom_b.merge_serialization(nom_a)\n    >>> nom_b == nom_a\n    True\n\n\n\nYAML Configuration File Rules\n*****************************\n\nSo far the suffixes is a look up dictionary for Maya objects, however I will be adding support for more later.\n\nTo properly enter a naming format string:\n\n    Enter all tokens you want to use with descriptive value that naming token\'s label e.g:\n        ``name``\n\n    and place it where you want it in order in the formatting string you set.\n    If you want something to space out or separate the names just input whatever separator\n    you want to use like ``_`` or ``.`` and it will keep those as delimiters.\n    ``name_side_type``\n\n    Additionall if you want them camel cased for example name and type:\n    ``side_nameType``\n    and it will automatically camelcase your for whatever you input for the given token values.\n\n    In the config YAML file (`~/.nomenclate.yml`) define your format under the header ``naming_formats`` with a sub-section name you think is appropriate (the following example is optionally nested under "node"):\n\n    .. code-block:: yaml\n\n        naming_formats:\n            node:\n                your_format: name_sidePurpose_type\n\n\n    If you want a static string to always be present in a format string just enclose it with parenthesis (for now only alphanumeric characters are accepted), for example a version:\n        ``(v)version``\n        in format string:\n        ``side_name_(v)version_(static_text_example)``\n\n        Example:\n            If version is 3 and your version padding config is set to 2\n            will evaluate to:\n            ``v02``\n\nFurther version/var/date specific token notes:\n    There are 3 naming tokens with specific formatting functions that will give you customized results.  You can designate multiple fields for added granularity by adding a number after e.g. var1, var2\n\n      :var:\n        this depends on var in the config being set to upper or lower\n\n        ``a``: returns a character based on position in alphabet, if you go over it starts aa -> az -> ba -> bz etc.\n\n        ``A``: returns a character based on position in alphabet, if you go over it starts AA -> AZ -> BA -> BZ etc.\n\n      :version:\n        Will return a string number based on the version_padding config setting\n\n      :date:\n        Will return a date as a string based on a datetime module formatted string\n        that the user will input or default to YYYY-MM-DD\n\n        Please specify whichever separators (or lack of) you want to override the default behavior just modify the config\n\n        The full list of options can be found here:\n        `Datetime Documentation <https://docs.python.org/2/library/datetime.html#strftime-strptime-behavior>`_\n\n If you need any custom token value conversion functions you can specify them by inheriting from ``nomenclate.core.rendering.RenderBase`` and implementing its render function like so:\n\n    .. code-block:: python\n\n        import nomenclate\n\n        class RenderCustom(nomenclate.core.rendering.RenderBase):\n            token = \'custom\'\n            def render(cls, value, token, nomenclate_object, **kwargs):\n                """ Always prepend "meh"\n\n                :param value: str, the un-parsed/formatted token value\n                :param token: str, the name of the token in question\n                :param nomenclate_object: nomenclate.Nom, the nomenclate instance (for checking attribute values/config settings)\n                :return: str, the final syntax adhering token value\n                """\n                return \'meh\' + value\n\n    Otherwise, unless you specify an options list for a specific naming token in the custom renderer\n    it will just replace the text with whatever you set that naming token to\n    on the nomenclate object.  The options lists will be used as a filter for the\n    naming token validity or as a look up table for UIs and if you specify\n    different lengths after it. It will use the first in the list unless\n    otherwise specified in the overall_config section under "<naming_token>_length"\n    If there is no abbreviation list afterwards then just write it as a list with -\n\n\nVersion Support\n###############\nCurrently this package supports Python 2.7, 3.5 and 3.6\n\nAttribution\n###########\nWPZOOM Developer Icon Set by WPZOOM License_ Source_ - Designed by David Ferreira.\n    .. _License: http://creativecommons.org/licenses/by-sa/3.0/\n    .. _Source: http://www.wpzoom.com\n\nIcon made by iconauth_ from www.flaticon.com\n    .. _iconauth: https://www.flaticon.com/authors/freepik\n',
    'author': 'Andres Weber',
    'author_email': 'andresmweber@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://nomenclate.andresmweber.com',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
