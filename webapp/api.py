class CertificationAPI:
    """
    Method names and properties to describe and map directly
    onto the Certification API
    (at the time of writing, this API is available at
    https://certification.canonical.com/api/v1)
    """

    def __init__(self, base_url, session):
        self.base_url = base_url
        self.session = session

    def _get(self, path, params={}):
        # Remove "None" values from params
        params = {
            key: value for key, value in params.items() if value is not None
        }

        # Get the JSON data
        response = self.session.get(
            f"{self.base_url}/{path.strip('/')}/?format=json", params=params
        )

        # Raise any HTTP errors
        response.raise_for_status()

        return response

    def certifiedmakes(
        self,
        limit=None,
        offset=None,
        desktops__gte=None,
        laptops__gte=None,
        smart_core__gte=None,
        soc__gte=None,
    ):
        return self._get(
            "certifiedmakes",
            params={
                "limit": limit,
                "offset": offset,
                "desktops__gte": desktops__gte,
                "laptops__gte": laptops__gte,
                "smart_core__gte": smart_core__gte,
                "soc__gte": soc__gte,
            },
        ).json()

    def certifiedmodels(self, limit=None, offset=None):
        return self._get(
            "certifiedmodels", params={"limit": limit, "offset": offset}
        ).json()

    def certifiedmodel(self, id):
        return self._get(f"certifiedmodels/{id}").json()

    def certifiedmodeldetails(
        self, limit=None, offset=None, canonical_id=None
    ):
        return self._get(
            "certifiedmodeldetails",
            params={
                "limit": limit,
                "offset": offset,
                "canonical_id": canonical_id,
            },
        ).json()

    def certifiedmodeldevices(
        self, limit=None, offset=None, canonical_id=None
    ):
        return self._get(
            "certifiedmodeldevices",
            params={
                "limit": limit,
                "offset": offset,
                "canonical_id": canonical_id,
            },
        ).json()

    def certifiedreleases(
        self, limit=None, offset=None, smart_core__gte=None, soc__gte=None
    ):
        return self._get(
            "certifiedreleases",
            params={
                "limit": limit,
                "offset": offset,
                "smart_core__gte": smart_core__gte,
                "soc__gte": soc__gte,
            },
        ).json()

    def componentsummaries(self, limit=None, offset=None):
        return self._get(
            "componentsummaries", params={"limit": limit, "offset": offset}
        ).json()

    def devicecategories(self, limit=None, offset=None):
        return self._get(
            "devicecategories", params={"limit": limit, "offset": offset}
        ).json()

    def releases(self, limit=None, offset=None):
        return self._get(
            "releases", params={"limit": limit, "offset": offset}
        ).json()

    def vendorsummaries_server(self, limit=None, offset=None):
        return self._get(
            "vendorsummaries/server", params={"limit": limit, "offset": offset}
        ).json()