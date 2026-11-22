from reservation import Reservation


def test_checking_in_before_paying_is_refused():
    maya = Reservation(1001, 'Maya Rodriguez')

    maya.check_in()                         # called from the wrong status

    assert maya.status == 'reserved'        # the refusal changed nothing


def test_checking_in_after_paying_is_allowed():
    maya = Reservation(1001, 'Maya Rodriguez')
    maya.pay()

    maya.check_in()                         # called from the right status

    assert maya.status == 'checked_in'      # the guard let the call through
