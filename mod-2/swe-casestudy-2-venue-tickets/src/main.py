"""The main entry point for the application."""

from datetime import date

from menu import show_menu
from sample_data import build_sample_venue


def start_app():
    venue = build_sample_venue(date.today())
    print(f'Welcome to {venue.name}!')
    show_menu(venue)
    print('Goodbye!')


if __name__ == "__main__":
    start_app()
