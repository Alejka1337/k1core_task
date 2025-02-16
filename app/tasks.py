import logging

import requests
from django.conf import settings

from app.dal.blocks import create_block
from core.celery import celery_app

logger = logging.getLogger(__name__)

@celery_app.task
def fetch_btc_block_data():
    url = settings.COINMARKETCAP_URL
    headers = {
        "X-CMC_PRO_API_KEY": settings.COINMARKETCAP_API_KEY,
        "Accept": "application/json"
    }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            results = response.json()
            block_number = results["data"]["BTC"]["total_blocks"] - 1

            result = create_block(
                currency_name="BTC",
                provider_name="CoinMarketCap",
                block_number=block_number
            )
            if result:
                logger.info(f"Block {block_number} has been added")

            logger.info(f"Block {block_number} hasn't been added")

        else:
            logger.error(f"Unexpected status code: {response.status_code}")
    except requests.RequestException as e:
        logger.error(f"Error fetching BTC data: {e}")


@celery_app.task
def fetch_eth_block_data():
    url = settings.BLOCKCHAIR_URL
    headers = {
        "Accept": "application/json"
    }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            results = response.json()

            block_number = results["data"]["blocks"] - 1
            result = create_block(
                currency_name="ETH",
                provider_name="Blockchair",
                block_number=block_number
            )
            if result:
                logger.info(f"Block {block_number} has been added")

            logger.info(f"Block {block_number} hasn't been added")

        else:
            logger.error(f"Unexpected status code: {response.status_code}")

    except requests.RequestException as e:
        logger.error(f"Error fetching ETH data: {e}")
