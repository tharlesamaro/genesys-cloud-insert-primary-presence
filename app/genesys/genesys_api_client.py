import math

import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.api_client import ApiClient
from PureCloudPlatformClientV2.apis.users_api import UsersApi
from PureCloudPlatformClientV2.models import (
    AnalyticsUserDetail,
    PagingSpec,
    UserDetailsQuery,
)
from PureCloudPlatformClientV2.rest import ApiException

from app.config import get_settings


class GenesysApiClient:
    def __init__(self):
        settings = get_settings()
        self.client_id = settings.genesys_client_id
        self.client_secret = settings.genesys_client_secret
        self.region = PureCloudPlatformClientV2.PureCloudRegionHosts.sa_east_1
        PureCloudPlatformClientV2.configuration.host = self.region.get_api_host()
        self.api_client = self._get_authenticated_client()
        self.users_api = UsersApi(self.api_client)

    def _get_authenticated_client(self) -> ApiClient:
        return ApiClient().get_client_credentials_token(
            self.client_id, self.client_secret
        )

    def get_analytics_users_details(
        self, interval: str, page_size: int = 100
    ) -> list[AnalyticsUserDetail]:
        body = UserDetailsQuery()
        body.interval = interval

        try:
            initial_response = self.users_api.post_analytics_users_details_query(body)
            total_pages = math.ceil(initial_response.total_hits / page_size)

            users_details = initial_response.user_details

            for page_number in range(2, total_pages + 1):
                body.paging = PagingSpec()
                body.paging.page_size = page_size
                body.paging.page_number = page_number
                response = self.users_api.post_analytics_users_details_query(body)
                users_details.extend(response.user_details)

            return users_details

        except ApiException as e:
            self._handle_api_exception(e)
            return []

    @staticmethod
    def _handle_api_exception(e: ApiException) -> None:
        error_message = (
            f"Error calling UsersApi->post_analytics_users_details_query: {e}\n"
            f"Status code: {e.status}\n"
            f"Reason: {e.reason}\n"
            f"Headers: {e.headers}"
        )

        print(error_message)
