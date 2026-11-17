from datetime import date

from events import Concert, Screening, Workshop


def test_a_concert_adds_the_service_fee():
    jazz = Concert('Friday Night Jazz', date(2026, 12, 5), capacity=40, base_price=25, performer='The Blue Notes')
    assert jazz.ticket_price() == 30


def test_a_workshop_adds_the_materials_fee():
    pottery = Workshop('Intro to Pottery', date(2026, 12, 9), capacity=12, base_price=25, materials_fee=10)
    assert pottery.ticket_price() == 35


def test_a_screening_charges_the_base_price():
    coco = Screening('Movie Night: Coco', date(2026, 12, 18), capacity=30, base_price=25)
    assert coco.ticket_price() == 25
