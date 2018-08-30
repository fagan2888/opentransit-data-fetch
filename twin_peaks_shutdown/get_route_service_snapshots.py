import datetime

def run_for_date_range(start_date, end_date):
    """Get trip starts occuring within the date range

    :param start_date: starting date, inclusive
    :type start_date: string YYYY-MM-DD

    :param end_date: ending date, inclusive
    :type end_date: string YYYY-MM-DD
    """


"""
Generates file for each day where
{
  'date': '2018-05-25',
  'route_id': '5R',
  'snapshots': [
    'hour': 0,
    'minute': 15,
    'num_vehicles': 4,
  ]
}

We can then graph what we want in Jupyter, described in twinpeaks.txt
"""

def form_api_query(date_hour):
    """Returns GraphQL query for getting the states of all routes in the given date/hour.

    :param date_hour: date and hour to query on
    :type date_hour: datetime.datetime

    :return api_query: GraphQL query
    :rtype api_query: string
    """
    start_time_epoch = date_hour.replace(tzinfo=datetime.timezone.utc).timestamp() * 1000
    # add an hour minus one second
    end_time_epoch = (date_hour.replace(tzinfo=datetime.timezone.utc).timestamp() + 3599) * 1000
    # query all routes for every hour of every day
    api_query = """query {
      trynState(agency: "muni", startTime: "{start_time_epoch_ms}", endTime: "{end_time_epoch_ms}", routes: ["14", "14R", "49"]) {
        agency
        startTime
        routes {
          rid
          routeStates {
            vtime
            vehicles {
              vid
            }
          }
        }
      }
    }""".format(
      start_time_epoch_ms=start_time_epoch_ms,
      end_time_epoch_ms=end_time_epoch_ms,
    )