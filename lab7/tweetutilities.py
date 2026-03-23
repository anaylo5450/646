def get_geocodes(records):
    """Add latitude/longitude using hardcoded coordinates for countries
    found in the Kaggle trends dataset."""

    country_coords = {
        "Australia": (-25.2744, 133.7751),
        "Brazil": (-14.2350, -51.9253),
        "Canada": (56.1304, -106.3468),
        "France": (46.2276, 2.2137),
        "Germany": (51.1657, 10.4515),
        "India": (20.5937, 78.9629),
        "Italy": (41.8719, 12.5674),
        "Mexico": (23.6345, -102.5528),
        "Ukraine": (48.3794, 31.1656),
        "United States": (37.0902, -95.7129),
    }

    bad_locations = 0

    for record in records:
        country = str(record.get('searched_in_country', '')).strip()

        if country in country_coords:
            latitude, longitude = country_coords[country]
            record['latitude'] = latitude
            record['longitude'] = longitude
        else:
            bad_locations += 1

    return bad_locations
