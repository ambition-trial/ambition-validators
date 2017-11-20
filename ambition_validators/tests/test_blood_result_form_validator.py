from django.core.exceptions import ValidationError
from django.test import TestCase
from edc_constants.constants import YES, NO

from ..form_validators import BloodResultFormValidator
from .models import SubjectVisit, SubjectConsent
import uuid


class TestBloodResultFormValidator(TestCase):

    def setUp(self):
        self.subject_consent = SubjectConsent.objects.create(
            subject_identifier='11111111',
            gender='M')
        self.subject_visit = SubjectVisit.objects.create(
            subject_identifier='11111111',
            appointment_id=uuid.uuid4())

    def test_haemoglobin_units_male_invalid(self):
        cleaned_data = {
            'subject_visit': self.subject_visit,
            'haemoglobin': 12.5,
            'are_results_normal': YES
        }
        form_validator = BloodResultFormValidator(
            cleaned_data=cleaned_data
        )
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('are_results_normal', form_validator._errors)

    def test_haemoglobin_units_female_invalid(self):
        self.subject_consent.gender = 'F'
        self.subject_consent.save()
        cleaned_data = {
            'subject_visit': self.subject_visit,
            'haemoglobin': 16.5,
            'are_results_normal': YES
        }
        form_validator = BloodResultFormValidator(
            cleaned_data=cleaned_data
        )
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('are_results_normal', form_validator._errors)

    def test_haemoglobin_units_male_valid(self):
        cleaned_data = {
            'subject_visit': self.subject_visit,
            'haemoglobin': 14,
            'are_results_normal': YES
        }
        form_validator = BloodResultFormValidator(
            cleaned_data=cleaned_data
        )
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_no_creatinine_mg_invalid(self):
        cleaned_data = {
            'creatinine': 0.3,
            'creatinine_unit': None,
            'are_results_normal': YES
        }
        form_validator = BloodResultFormValidator(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_creatinine_mg_invalid(self):
        cleaned_data = {
            'creatinine': 0.3,
            'creatinine_unit': 'mg/dL',
            'are_results_normal': YES
        }
        form_validator = BloodResultFormValidator(
            cleaned_data=cleaned_data
        )
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('are_results_normal', form_validator._errors)

    def test_creatinine_mg(self):

        cleaned_data = {
            'creatinine': 1.3,
            'creatinine_unit': 'mg/dL',
            'are_results_normal': NO,
            'abnormal_results_in_ae_range': YES
        }
        form_validator = BloodResultFormValidator(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_creatinine_umol_invalid(self):
        cleaned_data = {
            'creatinine': 43,
            'creatinine_unit': 'umol/L',
            'are_results_normal': YES
        }
        form_validator = BloodResultFormValidator(
            cleaned_data=cleaned_data
        )
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('are_results_normal', form_validator._errors)

    def test_creatinine_umol(self):

        cleaned_data = {
            'creatinine': 100,
            'creatinine_unit': 'mg/dL',
            'are_results_normal': NO,
            'abnormal_results_in_ae_range': YES
        }
        form_validator = BloodResultFormValidator(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_magnesium_invalid(self):
        cleaned_data = {
            'magnesium': 0.01,
            'are_results_normal': YES
        }
        form_validator = BloodResultFormValidator(
            cleaned_data=cleaned_data
        )
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('are_results_normal', form_validator._errors)

    def test_magnesium(self):

        cleaned_data = {
            'magnesium': 1.0,
            'are_results_normal': NO,
            'abnormal_results_in_ae_range': YES}
        form_validator = BloodResultFormValidator(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_potassium_invalid(self):
        cleaned_data = {
            'potassium': 1.0,
            'are_results_normal': YES
        }
        form_validator = BloodResultFormValidator(
            cleaned_data=cleaned_data
        )
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('are_results_normal', form_validator._errors)

    def test_potassium(self):

        cleaned_data = {
            'potassium': 5.0,
            'are_results_normal': NO,
            'abnormal_results_in_ae_range': YES}
        form_validator = BloodResultFormValidator(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_sodium_invalid(self):
        cleaned_data = {
            'sodium': 100,
            'are_results_normal': YES
        }
        form_validator = BloodResultFormValidator(
            cleaned_data=cleaned_data
        )
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('are_results_normal', form_validator._errors)

    def test_sodium(self):

        cleaned_data = {
            'sodium': 135,
            'are_results_normal': NO,
            'abnormal_results_in_ae_range': YES
        }
        form_validator = BloodResultFormValidator(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_alt_invalid(self):
        cleaned_data = {
            'alt': 100,
            'are_results_normal': YES
        }
        form_validator = BloodResultFormValidator(
            cleaned_data=cleaned_data
        )
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('are_results_normal', form_validator._errors)

    def test_alt(self):

        cleaned_data = {
            'alt': 10,
            'are_results_normal': YES,
        }
        form_validator = BloodResultFormValidator(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_platelets_invalid(self):
        cleaned_data = {
            'platelets': 500,
            'are_results_normal': YES
        }
        form_validator = BloodResultFormValidator(
            cleaned_data=cleaned_data
        )
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('are_results_normal', form_validator._errors)

    def test_platelets(self):

        cleaned_data = {
            'platelets': 450,
            'are_results_normal': YES,
        }
        form_validator = BloodResultFormValidator(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_absolute_neutrophil_invalid(self):
        cleaned_data = {
            'absolute_neutrophil': 1,
            'are_results_normal': YES
        }
        form_validator = BloodResultFormValidator(
            cleaned_data=cleaned_data
        )
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('are_results_normal', form_validator._errors)

    def test_absolute_neutrophil(self):

        cleaned_data = {
            'absolute_neutrophil': 4,
            'are_results_normal': YES,
        }
        form_validator = BloodResultFormValidator(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_abnormal_results_in_ae_range_invalid(self):
        cleaned_data = {
            'sodium': 1000,
            'are_results_normal': NO,
            'abnormal_results_in_ae_range': NO
        }
        form_validator = BloodResultFormValidator(
            cleaned_data=cleaned_data
        )
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('abnormal_results_in_ae_range', form_validator._errors)
