from twisted.application import service, internet
from twisted.internet import endpoints, protocol
from twisted.python import log
from twisted.python import usage
from twisted.web import server
from twisted.web.resource import Resource
from twisted.internet.protocol import Protocol

DEFAULT_STRPORT = 'tcp:8000'

class Options(usage.Options):
    """
    Provide a --debug option for starting the server in debug mode, and the
    ability to define what to listen on by using a string endpoint description.

    Documentation on how to configure a usage.Options object is provided here:
    http://twistedmatrix.com/documents/current/core/howto/options.html

    Endpoints are documented here in the API documentation:
    http://twistedmatrix.com/documents/current/api/twisted.internet.endpoints.html
    """
    optFlags = [['debug', 'd', 'Emit debug messages']]
    optParameters = [["endpoint", "s", DEFAULT_STRPORT,
                      "string endpoint descriptiont to listen on, defaults to 'tcp:8000'"]]

class ExampleProtocol(Protocol):
    """
    Simple 'hello world' HTTP response
    """
    
    def connectionMade(self):
        response = "HTTP/1.0 200 OK\r\n" \
                   "Content-Type: text/html\r\n" \
                   "Connection: close\r\n" \
                   "\r\n" \
                   "Hello World\n"
                   
        self.transport.write(response + '\r\n')
        
        self.transport.loseConnection()
            

class ExampleFactory(protocol.ServerFactory):
    """
    Your factory would replace this placeholder. Note that there is a debug
    option passed to __init__, this comes from the commandline when the command
    "twistd example --debug" is used.
    """
    protocol = ExampleProtocol

    def __init__(self, debug=False):
        self.debug = debug

    def connectionMade(self):
        """
        Small example of how to do switch on the debug flag.
        """
        if self.debug:
            log.msg("Connection Made")

def makeService(options):
    """
    Generate and return a definition for all the services that this package
    needs to run. Will return a 'MultiService' object with two children.
    One is a ExampleFactory listening on the configured endpoint, and the
    other is an example custom Service that will do some set-up.
    """
    from twisted.internet import reactor

    debug = options['debug']

    f = ExampleFactory(debug=debug)
    endpoint = endpoints.serverFromString(reactor, options['endpoint'])
    server_service = internet.StreamServerEndpointService(endpoint, f)
    server_service.setName('Example Server')

    return server_service
