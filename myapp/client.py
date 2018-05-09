import requests


class GenomeLinkError(Exception):
    pass

class Report(object):
    @staticmethod
    def fetch(client_secret='', token=''):
        headers = {'Authorization': 'Bearer {}'.format(client_secret)}
        url = 'https://genomelink.io/v1/enterprise/reports/'
        response = requests.post(url, headers=headers, data={'token': token})
        if response.status_code != requests.codes.ok:
            raise GenomeLinkError('Invalid token.')
        return response.json()
