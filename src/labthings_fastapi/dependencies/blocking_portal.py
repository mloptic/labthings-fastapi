"""FastAPI dependency for a blocking portal

This allows dependencies that are called by threaded code to send things back
to the async event loop.
"""
from __future__ import annotations
import uuid
from typing import Annotated
from fastapi import Depends, Request
from anyio.from_thread import BlockingPortal as RealBlockingPortal
from ..thing_server import find_thing_server, ThingServer


def blocking_portal_from_thing_server(request: Request) -> RealBlockingPortal:
    """Return a UUID for an action invocation
    
    This is for use as a FastAPI dependency, to allow other dependencies to
    access the invocation ID. Useful for e.g. file management.
    """
    return find_thing_server(request.app).blocking_portal


BlockingPortal = Annotated[RealBlockingPortal, Depends(blocking_portal_from_thing_server)]