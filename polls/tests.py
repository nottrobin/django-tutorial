import datetime

from django.utils import timezone
from django.test import TestCase

from polls.models import Poll

class PollMethodTests(TestCase):
    def test_was_published_recently_with_future_poll(self):
        """
        was_published_recently() should return False for polls whose
        pub_date is in the future
        """
        future_poll = Poll(pub_date=timezone.now() + datetime.timedelta(days=30))
        self.assertEqual(future_poll.was_published_recently(), False)

    def test_was_published_recently_with_old_poll(self):
        """
        was_published_recently() should return False for old polls
        """
        past_poll = Poll(pub_date=timezone.now() - datetime.timedelta(days=1, microseconds=1))
        self.assertEqual(past_poll.was_published_recently(), False)

    def test_was_published_recently_with_new_poll(self):
        """
        was_published_recently() should return True for polls whose
        pub_date is now
        """
        new_poll = Poll(pub_date=timezone.now())
        self.assertEqual(new_poll.was_published_recently(), True)

    def test_was_published_recently_with_recent_poll(self):
        """
        was_published_recently() should return True for polls
        published within the last day
        """
        recent_poll = Poll(pub_date=timezone.now() - datetime.timedelta(days=1, seconds=-1))
        self.assertEqual(recent_poll.was_published_recently(), True)