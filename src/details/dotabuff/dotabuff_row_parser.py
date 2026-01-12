from datetime import datetime

class DotabuffRowParser:
    def parse_row(self, row):
        hero = self._get_hero(row)
        is_win = self._get_match_result(row)
        kda = self._get_kda(row)
        duration = self._get_duration(row)
        date_timestamp = self._get_date(row)
        
        return {
            'is_win': is_win,
            'hero': hero,
            'duration': duration,
            'kda': kda,
            'date': date_timestamp,
        }

    def _get_hero(self, row):
        hero_cell = row.find('td', class_='cell-large')
        hero_link = hero_cell.find('a')
        return hero_link.text.strip()

    def _get_match_result(self, row):
        result_link = row.find('a', class_=lambda x: x and ('lost' in x or 'won' in x or 'abandoned' in x))
        if not result_link: # если матч покинут
            return False
        classes = result_link.get('class')
        if 'won' in classes:
            return True
        if 'lost' in classes:
            return False

    def _get_kda(self, row):
        kda_span = row.find('span', class_='kda-record')
        return kda_span.get_text(strip=True)

    def _get_duration(self, row):
        for td in row.find_all('td'):
            if not td.contents:
                continue
            first_content = td.contents[0]
            if not isinstance(first_content, str):
                continue
            text = first_content.strip()
            time_part = text.split(':')[0:2]
            if len(time_part) != 2:
                continue
            minutes, seconds = time_part
            return int(minutes) * 60 + int(seconds)

    def _get_date(self, row):
        time_tag = row.find('time')
        dt_str = time_tag['datetime']
        dt_str = dt_str.replace('Z', '+00:00')
        dt = datetime.fromisoformat(dt_str)
        return int(dt.timestamp())
