from edc_form_validators import FormValidator
from edc_constants.constants import YES, NO


class PkPdCrfFormValidator(FormValidator):

    def clean(self):

        self.required_if(
            YES,
            field='flucytosine_doses_missed',
            field_required='flucytosine_dose_missed')

        self.required_if(
            YES,
            field='fluconazole_dose_missed',
            field_required='reason_fluconazole_dose_missed')

        self.required_if(
            YES,
            field='fluconazole_dose_missed',
            field_required='reason_fluconazole_dose_missed')

        self.required_if(
            YES,
            field='any_day_one_sample_missed',
            field_required='reason_day_one_missed')

        self.required_if(
            YES,
            field='any_day_seven_sample_missed',
            field_required='reason_day_seven_missed')

        self.required_if(
            NO,
            field='pre_dose_lp',
            field_required='post_dose_lp')