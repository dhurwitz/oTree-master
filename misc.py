MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATIC_URL = '/static/'

#STATICFILES_DIRS = (
#    os.path.join(BASE_DIR, 'staticfiles'),
#)



urls


from django.conf import settings
from django.conf.urls.static import static

#urlpatterns = [
    # ... the rest of your URLconf goes here ...
#] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



Here is an example of Bootstrap:

<div class="alert alert-success">Great job!</div>

This makes a green box that says great job!


This line made a form field for purchasing albums

    {% formrow form.album_purchase with label="Put 1 if you want to Purchase this Album" %}


    Currently replaced with buttons


javascript create Button

    var btn = document.createElement("BUTTON");
    document.body.appendChild(btn);

    java script create paragraph

var para = document.createElement("P");                       // Create a <p> element
var t = document.createTextNode("This is a paragraph");       // Create a text node
para.appendChild(t);                                          // Append the text to <p>
document.body.appendChild(para);



HTML:

<p style ="color:red;text-align:center;" > Total Budget: {{Constants.consumer_budget}} </p>

    <p style ="color:red;text-align:center;"> Cost of Each Album: {{Constants.album_own_cost}}</p>

    <span style ="color:red;margin-left:125px;">Remaining Budget: </span> <span id="budget" style ="color:red;margin-left:127px;">  </span> <br>




consumer_purchase = models.PositiveIntegerField(
        min=0,
        max=(Constants.consumer_budget/Constants.album_own_cost),
        doc="""
        Description of this field, for documentation
        """
    )

    album_purchase = models.PositiveIntegerField(
        min = 0,
        max = 1,
        doc = """ Binary album purchase
        """
    )


