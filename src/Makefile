all:

install:
	. /etc/environ.sh; use -e -r anaconda-6; python -m compileall ../site-packages

clean:

distclean: clean
	find ../site-packages -name "*.pyc" -exec /bin/rm -f {} \;

.PHONY: all install clean distclean

