from collections import namedtuple
import requests
import json

RoboconStats = namedtuple('RoboconStats', [
    'total_teams', 'total_users', 'total_resources',
    'total_progress_submissions', 'pending_submissions_count',
    'reviewed_submissions_count', 'approved_submissions_count',
    'rejected_submissions_count', 'total_points_awarded'
])


def getmyroboconstats():
    url = "https://my.roboconoxon.org.uk/api/v1/dashboard/stats"
    payload = {}
    headers = {
        'Authorization': 'Bearer robocon_sk_0hs7u17aoceknbwc'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)
    data = json.loads(response.text)

    return RoboconStats(
        total_teams=data.get('totalTeams', 0),
        total_users=data.get('totalUsers', 0),
        total_resources=data.get('totalResources', 0),
        total_progress_submissions=data.get('totalProgressSubmissions', 0),
        pending_submissions_count=data.get('pendingSubmissionsCount', 0),
        reviewed_submissions_count=data.get('reviewedSubmissionsCount', 0),
        approved_submissions_count=data.get('approvedSubmissionsCount', 0),
        rejected_submissions_count=data.get('rejectedSubmissionsCount', 0),
        total_points_awarded=data.get('totalPointsAwarded', 0)
    )

