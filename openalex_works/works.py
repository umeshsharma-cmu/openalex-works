import requests


class OpenAlexWorks:
    def __init__(self, doi):
        self.doi = doi

    def get_bibtex(self):
        doi_url = f"https://doi.org/{self.doi}"
        headers = {"Accept": "application/x-bibtex"}
        response = requests.get(doi_url, headers=headers)
        return response.text

    def get_ris(self):
        doi_url = f"https://doi.org/{self.doi}"
        headers = {"Accept": "application/x-research-info-systems"}
        response = requests.get(doi_url, headers=headers)
        return response.text
