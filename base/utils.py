#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import time
import logging

from django.conf import settings
from django.core.cache import cache

from upwork import Client

logger = logging.getLogger(__name__)


pretty_names = {'amazon-web-services': 'Amazon Web Services', 'api-development': 'API Development',
                'django-framework': 'Django', 'elasticsearch': 'Elasticsearch', 'flask': 'Flask', 'html5': 'HTML5',
                'jquery': 'jQuery', 'python': 'Python', 'sql': 'SQL', 'web-scraping': 'Web Scraping'}


def _get_upwork_data(retries=3):
    upwork_data = cache.get('upwork_data')
    now = time.time()
    if not upwork_data or now - upwork_data['time'] > settings.UPWORK_DATA_TIMEOUT:
        try:
            upwork = Client(**settings.UPWORK_KEYS)
            upwork_data = upwork.provider.get_provider(settings.UPWORK_PROFILE_ID)
            upwork_data['time'] = now
            cache.set('upwork_data', upwork_data)
        except (SystemExit, KeyboardInterrupt):
            raise
        except Exception:
            logger.exception('Exception occurred while getting the upwork data')
            if retries > 0:
                logger.info('Retrying _get_upwork_data method')
                return _get_upwork_data(retries-1)

    return upwork_data


def _to_date(date_string):
    try:
        result = datetime.datetime.strptime(date_string, '%m/%d/%Y')
    except ValueError:
        result = datetime.datetime.now()
    return result.date()


def get_upwork_data(min_feedback=4.0, min_comment_length=40, date_format='%d/%m/%Y', mappings=('dev_adj_score_recent', 'dev_last_activity',
                                                                        'dev_total_hours', 'dev_billed_assignments',
                                                                        'dev_profile_title', 'dev_blurb', 'education')):
    data = _get_upwork_data()

    result = {}
    for mapping in mappings:
        value = data[mapping]
        try:
            value = float(value)
        except (ValueError, TypeError):
            pass

        result[mapping] = value

    result['dev_last_activity'] = _to_date(result['dev_last_activity'])

    skills = []
    sorted_skills = sorted(data['skills']['skill'], key=lambda x: int(x['skl_rank']))
    for skill in sorted_skills:
        try:
            pretty_name = pretty_names[skill['skl_name']]
        except KeyError:
            pretty_name = skill['skl_name'].replace('-', ' ').title()
        skills.append(pretty_name)
    result['skills'] = skills

    assignments = []
    for assignment in (data['assignments']['hr']['job'] + data['assignments']['fp']['job']):
        if 'feedback' in assignment and assignment['feedback']['comment']:
            score = float(assignment['feedback']['score'])
            if score > min_feedback and len(assignment['feedback']['comment']) > min_comment_length:
                assignments.append({'feedback': assignment['feedback']['comment'],
                                    'score': score,
                                    'date': _to_date(assignment['as_to_full']),
                                    'title': assignment['as_opening_title']})
    result['assignments'] = sorted(assignments, key=lambda x: x['date'], reverse=True)

    exams = []
    sorted_exams = reversed(sorted(data['tsexams']['tsexam'], key=lambda x: float(x['ts_percentile'])))
    for exam in sorted_exams:
        exams.append((exam['ts_name_raw'], float(exam['ts_percentile'])))
    result['exams'] = exams

    return result
