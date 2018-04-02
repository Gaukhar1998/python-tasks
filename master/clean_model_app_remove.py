from django.contrib.contenttypes.models import ContentType

# List of deleted apps
# List of deleted models (that are not in the app deleted) In lowercase!
DEL_MODELS = ["Album"]

ct = ContentType.objects.all().order_by("app_label", "model")

for c in ct:
    if c.model in DEL_MODELS:
        print("Deleting Content Type %s" % (c.model))
        c.delete()