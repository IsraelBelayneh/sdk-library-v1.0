from sdk.api_client import APIClient
from sdk.config import Config
from sdk.models.transaction_model import STKPushRequest, STKPushResponse
from sdk.utils.logger import logger
from sdk.errors.base_error import STKPush

class STKPushService:
    def __init__(self):
        self.client = APIClient()

    def initiate_stk_push(self, request: STKPushRequest) -> STKPushResponse:
        endpoint = Config.STK_PUSH
        headers = {
            "Authorization": f"Bearer {Config.TOKEN}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

        try:
            logger.info("Initiating STK push...")
            response = self.client.post(endpoint, data=request, headers=headers)
            logger.info("STK push initiated successfully.")
            return STKPushResponse(**response)

        except STKPush as e:
            logger.exception("An error occurred while initiating STK push: %s", e)
            raise
