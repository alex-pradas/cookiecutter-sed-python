
Welcome to {{cookiecutter.project_name}} documentation!
=======================================================

Introduction
------------
{{cookiecutter.project_short_description}}

Then you can add another paragraph to give more details of your module. The first stand alone sentence gives the possible users a punch about what the module is intended to do, and will be use by external tools to provide a summary of whe module. In this paragraph, you can add more info. This documentation has a double purpose: It gives the developer a working example to start playing around, and it also provides some tips.

Other sections
--------------

This is another section to show that you can put more text here. The template uses it to give more instruction to
the developer.

This document should have a ``.. toctree::`` directive as a minimum, and then the module developer can add more rst pages there.
It is recommended that you have at least an API section to check each function available (to be consulted when writing
code) and another section with examples and tutorials (to be used when learning to use the module).

Every page in the toctree should exist as an .rst file in the same folder as this file (`index.rst`). 

.. note::
   * you can remove the rst extension.
   * you can actually refer to files in other folder with a relative path to this folder.



.. toctree::
   
   api
   cheatsheet
   getting_started
   changelog-link

