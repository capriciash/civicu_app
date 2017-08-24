import os
import datetime

from django.test import TestCase
from django.utils import timezone
# from django.core.urlresolvers import reverse

import civicu_app.settings
from .models import Image
from django.contrib.auth.models import User
# from .forms import FileUploadForm

MEDIA_ROOT = civicu_app.settings.MEDIA_ROOT


class ImageModelTest(TestCase):
    fixtures = ['labelgame_test_data.json', 'labelgame_test_user_data.json']
    caption = "This is only a test ... image taken 2.5 years ago."

    def create_image(self, caption=caption):
        return Image.objects.create(caption=caption,
                                    date_taken=timezone.now() - datetime.timedelta(365.25 * 2.5),
                                    img_file=os.path.join(
                                        MEDIA_ROOT, 'images', 'test_image.png'),
                                    updated_date=timezone.now() - datetime.timedelta(8),
                                    created_date=timezone.now(),
                                    # uploaded_by=1
                                    )

    def test_image_creation(self):
        image = self.create_image()
        self.assertTrue(isinstance(image, Image))
        # self.assertEqual(image.__unicode__(), image.caption)
        self.assertEqual(self.caption, image.caption)
