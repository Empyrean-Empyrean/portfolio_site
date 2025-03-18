# from django import forms
# from .models import FinancialProject

# class FinancialProjectForm(forms.ModelForm):
#     class Meta:
#         model = FinancialProject
#         fields = ['name', 'slug', 'main_technology', 'technologies', 'thumbnail', 'explanation', 'code_snippet', 'other_info']
from django import forms
from .models import FinancialProject
from projects.models import Technology  # Assuming Technology model is shared

class FinancialProjectForm(forms.ModelForm):
    # Field for selecting existing technologies
    technologies = forms.ModelMultipleChoiceField(
        queryset=Technology.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Select Existing Technologies"
    )
    # Extra field for entering new technology names (comma-separated)
    new_technologies = forms.CharField(
        required=False,
        label="Other Technologies (comma-separated)",
        help_text="Enter new technology names separated by commas"
    )
    
    class Meta:
        model = FinancialProject
        fields = [
            'name', 'slug', 'main_technology', 'technologies',
            'new_technologies',  # extra field for new entries
            'explanation', 'code_snippet', 'other_info', 'thumbnail'
        ]

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
        self.save_m2m()  # Save the many-to-many relationships
        
        # Handle new technologies entered as a comma-separated string
        new_techs = self.cleaned_data.get("new_technologies")
        if new_techs:
            tech_names = [name.strip() for name in new_techs.split(",") if name.strip()]
            for tech_name in tech_names:
                tech, created = Technology.objects.get_or_create(name=tech_name)
                instance.technologies.add(tech)
        return instance
