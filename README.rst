================
how to run tests
================

to run the test you can use the `make` command

.. code-block:: shell

	# run all unit test
	make test
	# for run pep8 and flake
	make style_test
	# or you can use
	make pep8; make flakes

to open the coverage report you can use

.. code-block:: shell

	make open_report_firefox
	# or
	firefox .coverage_html_report/index.html
