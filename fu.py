from datetime import datetime
import pytz

time_zone_mappings = {
    'Zulu': 'Etc/UTC'
}

def parse_date_in_time_zone(date_string, time_zone_label):
    time_zone = time_zone_mappings.get(time_zone_label, time_zone_label)
    tz = pytz.timezone(time_zone)
    return datetime.strptime(date_string, '%Y-%m-%dT%H:%M:%S').replace(tzinfo=tz)

date = parse_date_in_time_zone('2024-06-22T12:00:00', 'Zulu')
print(date)  # Outputs the datetime object with UTC timezone
