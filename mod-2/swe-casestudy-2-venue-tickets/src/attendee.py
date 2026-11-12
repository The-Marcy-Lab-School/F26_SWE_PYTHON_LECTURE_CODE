"""A person who books tickets."""

from dataclasses import dataclass


# @dataclass writes __init__, __repr__, and __eq__ for this class, using the
# attributes listed below. An Attendee only carries data, so it needs no methods.
# The ": str" after each name is a type annotation, which @dataclass requires.
@dataclass
class Attendee:
    name: str
    email: str
