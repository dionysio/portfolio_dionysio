#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import logging

from django.core.management import BaseCommand
from django.conf import settings
from django.core.cache import cache

from upwork import Client


logger = logging.getLogger(__name__)


class Command(BaseCommand):
    # Show this when the user types help

    # A command must define handle()
    def handle(self, retries=3, *args, **options):
        upwork_data = cache.get('upwork_data')
        now = time.time()
        if not upwork_data or now - upwork_data['time'] > settings.UPWORK_DATA_TIMEOUT:
            try:
                upwork = Client(**settings.UPWORK_KEYS)
                upwork_data = upwork.provider.get_provider(settings.UPWORK_PROFILE_ID)
                if upwork_data:
                    upwork_data['time'] = now
                    cache.set('upwork_data', upwork_data)
            except (SystemExit, KeyboardInterrupt):
                raise
            except:
                logger.exception('Exception occurred while getting the upwork data')
                if retries > 0:
                    logger.info('Retrying _get_upwork_data method')
                    return self.handle(retries - 1)
