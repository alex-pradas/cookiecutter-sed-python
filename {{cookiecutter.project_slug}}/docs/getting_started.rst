Getting started
===============

Setting up the developer environment
------------------------------------

.. note::
   This section assumes that you are using ``conda`` to manage your environment. Substitute it with ``python -m venv`` or other python environment manager as required.

.. note::
   This section also assumes that you are using VS Code. If you are using PyCharm or other IDEs, check the file ``.vscode\tasks.json`` for the actual commands.

1. Create a development (``dev``) environment. Activate it.
   
   .. code-block::

      conda create -n dev python
      conda activate dev

2. install the package in development mode.
      
   Navigate to the root folder of the package (where the ``setup.cfg`` file is)

   .. code-block::
      
      pip install -e .[dev]

   .. tip::

      Usual errors involve:

      - having and old version of pip. type ``pip install -U pip`` to upgrade.
      - Command line not being at the root folder.
  



Documentation
-------------

RST and Sphinx
^^^^^^^^^^^^^^

RST is the language in which documentation is written. The file extension is ``.rst``. is It is similar to other languages such as LaTeX; you define the content in a plain file and it is compiled into a pretty format.
The tool to complie the plain text files is called `Sphinx <https://www.sphinx-doc.org/en/master/index.html>`_. You can ``pip install Sphinx`` in your python environment.

We can go into much more details on how rst and sphinx work, but it is actually very well documented.

If you are using VS Code, then all you need to compile and show the docs is ``Ctrl + Shift + B``.

Documenting areas
^^^^^^^^^^^^^^^^^
