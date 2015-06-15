MEMPy-Ruby
==========

"Supporting" code for a MemPy presentation on the peaceful coexistence of Ruby and Python "microservices".

This code is not intended as a reference for any type of architecture. Much of what you see here is taken directly from the documentation for Tornado, Flask, Angelo, HTTParty, and Sinatra.

Setup
-----

This code was loosely tested against Python 2.7, Ruby 2.2, and JRuby.

	pip install requirements.txt
	bundle install
	
Running
-------

Simply execute a server followed by a client. e.g.

	python python/server_async.py
	
Followed by

	ruby ruby/client_async.rb
	
server_sync.rb will actually appear to behave asyncronously as your Ruby webserver likely runs in threaded mode and sleep() will not hold the GIL.
