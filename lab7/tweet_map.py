import sys
import os
import pandas as pd
import folium
from tweetutilities import get_geocodes


def load_trends(csv_name, limit=None):
    file_path = os.path.join('archive', csv_name)

    df = pd.read_csv(file_path)

    needed = [
        'trend_name',
        'tweet_volume',
        'searched_at_datetime',
        'searched_in_country'
    ]

    df = df[needed].copy()

    df = df.dropna(subset=['searched_in_country'])
    df['searched_in_country'] = df['searched_in_country'].astype(str).str.strip()
    df = df[df['searched_in_country'] != '']

    if limit is not None:
        df = df.head(limit)

    return df.to_dict(orient='records')


def build_map(records, output_file='tweet_map.html'):
    world_map = folium.Map(location=[20, 0], tiles='OpenStreetMap', zoom_start=2)

    for record in records:
        if 'latitude' not in record or 'longitude' not in record:
            continue

        popup_text = (
            f"Trend: {record['trend_name']}<br>"
            f"Country: {record['searched_in_country']}<br>"
            f"Tweet Volume: {record['tweet_volume']}<br>"
            f"Searched At: {record['searched_at_datetime']}"
        )

        folium.Marker(
            [record['latitude'], record['longitude']],
            popup=folium.Popup(popup_text, max_width=300)
        ).add_to(world_map)

    world_map.save(output_file)


def main():
    if len(sys.argv) < 2:
        print('Usage: python tweet_map.py <csv_name> [limit]')
        return

    csv_name = sys.argv[1]
    limit = int(sys.argv[2]) if len(sys.argv) > 2 else 100

    records = load_trends(csv_name, limit)
    bad_locations = get_geocodes(records)
    print(f'Could not geocode {bad_locations} locations.')

    valid_records = [r for r in records if 'latitude' in r and 'longitude' in r]
    if not valid_records:
        print('No valid geocoded locations were found.')
        return

    build_map(valid_records)
    print('Saved tweet_map.html')


if __name__ == '__main__':
    main()
