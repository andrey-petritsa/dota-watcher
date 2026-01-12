import cloudscraper
import logging
import time
from bs4 import BeautifulSoup

from .dotabuff_html_fetcher import DotabuffHtmlFetcher
from .dotabuff_row_parser import DotabuffRowParser

class DotabuffWatcher:
    def __init__(self, ):
        self.row_parser = DotabuffRowParser()
        self.html_fetcher = DotabuffHtmlFetcher()
        self.logger = logging.getLogger(__name__)

    def get_events(self, player_id):
        self.player_id = player_id
        html_content = self.html_fetcher.fetch(player_id)
        rows = self._extract_table(html_content)
        events = self._parse_rows_to_events(rows)
        return events


    def _extract_table(self, html_content):
        soup = BeautifulSoup(html_content, 'html.parser')
        table = soup.find('table')

        tbody = table.find('tbody')
        rows = tbody.find_all('tr')

        return rows

    def _parse_rows_to_events(self, rows):
        events = []
        for row in rows:
            event = self.row_parser.parse_row(row)
            event['player_id'] = str(self.player_id)
            event['id'] = self.get_event_id(event)
            events.append(event)
        return events

    def get_event_id(self, event):
        player_id = event['player_id']
        timestamp = event['date']
        return f"{player_id}:{timestamp}"
