from django import forms

from .models import BlogComment

class BlogCommentForm(forms.Form):
	name = forms.CharField(required=True)
	comment = forms.CharField(required=True)
	email = forms.EmailField(required=True)
	tick = forms.BooleanField(required=False, label="Remember me.")

	def clean_email():
		pass


"""class BlogComment(models.Model):
	blog = models.ForeignKey(Blog)
	name = models.CharField(max_length=100)
	comment = models.TextField()
	timestamp = models.DateTimeField"""

def validate_length(value):
	if len(value) < 10:
		raise forms.ValidationError("Too short.")

class BlogCommentNewForm(forms.ModelForm):
	name = forms.CharField()
	email = forms.EmailField(validators=[validate_length])

	def clean_name(self):
		pass

	class Meta:
		model = BlogComment
		exclude = ['blog', 'timestamp']