import logging

from zope import interface
from zope import component
from five import grok

from plone.jsonapi import router
from plone.jsonapi.interfaces import IRouter
from plone.jsonapi.interfaces import IRouteProvider

logger = logging.getLogger("plone.jsonapidemo")


class ExampleRoutes(object):

    def __init__(self):
        logger.info("ExampleRoutes::__init__")

    @property
    def routes(self):
        return (
            ("/hello/<string:name>", "hello", self.json_hello, dict(methods=['GET'])),
            ("/foo", "foo", self.json_foo, dict(methods=['POST'])),
            ("/bar", "bar", self.json_bar, dict(methods=['DELETE'])),
        )

    def json_hello(self, context, request, name="world"):
        return {"hello": name, "context": repr(context), "request": repr(request)}

    def json_foo(self, context, request):
        return {"context": repr(context), "request": repr(request)}

    def json_bar(self, context, request):
        return {"context": repr(context), "request": repr(request)}

grok.global_utility(ExampleRoutes, provides=IRouteProvider, name="my_routes", direct=False)


@router.add_route("/baz/<arg>", "baz", methods=["POST"])
def foo(context, request, arg):
    return {"arg": arg, "request": repr(request)}
