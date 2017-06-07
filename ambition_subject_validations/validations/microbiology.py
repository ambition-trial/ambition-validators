from edc_base.modelform_mixins import RequiredFieldValidationMixin
from edc_constants.constants import POS, YES, OTHER


class Microbiology(RequiredFieldValidationMixin):

    def __init__(self, cleaned_data=None):
        self.cleaned_data = cleaned_data

    def clean(self):
        self.required_if(
            YES,
            field='urine_culture_performed',
            field_required='urine_culture_results',
            cleaned_data=self.cleaned_data)

        self.required_if(
            POS,
            field='urine_culture_results',
            field_required='urine_culture_organism',
            cleaned_data=self.cleaned_data)

        self.required_if(
            OTHER,
            field='urine_culture_results',
            field_required='urine_culture_organism_other',
            cleaned_data=self.cleaned_data)

        self.required_if(
            YES,
            field='blood_culture_performed',
            field_required='blood_culture_results',
            cleaned_data=self.cleaned_data)

        self.required_if(
            POS,
            field='blood_culture_results',
            field_required='date_blood_taken',
            cleaned_data=self.cleaned_data)

        self.required_if(
            POS,
            field='blood_culture_results',
            field_required='blood_culture_organism',
            cleaned_data=self.cleaned_data)

        self.required_if(
            OTHER,
            field='blood_culture_organism',
            field_required='blood_culture_organism_other',
            cleaned_data=self.cleaned_data)

        self.required_if(
            'BACTERIA',
            field='blood_culture_organism',
            field_required='bacteria_identified',
            cleaned_data=self.cleaned_data)

        self.required_if(
            OTHER,
            field='bacteria_identified',
            field_required='bacteria_identified_other',
            cleaned_data=self.cleaned_data)

        self.required_if(
            POS,
            field='sputum_results_culture',
            field_required='sputum_results_positive',
            cleaned_data=self.cleaned_data)

        self.required_if(
            YES,
            field='tissue_biopsy_taken',
            field_required='tissue_biopsy_results',
            cleaned_data=self.cleaned_data)

        self.required_if(
            POS,
            field='tissue_biopsy_results',
            field_required='date_biopsy_taken',
            cleaned_data=self.cleaned_data)

        self.required_if(
            POS,
            field='tissue_biopsy_results',
            field_required='tissue_biopsy_organism',
            cleaned_data=self.cleaned_data)

        self.required_if(
            OTHER,
            field='tissue_biopsy_organism',
            field_required='tissue_biopsy_organism_other',
            cleaned_data=self.cleaned_data)

        return self.cleaned_data