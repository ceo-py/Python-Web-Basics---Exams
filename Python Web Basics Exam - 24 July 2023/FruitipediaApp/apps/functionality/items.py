def get_all_items(model_data=""):
    return model_data.objects.all().order_by("pk")


def find_item(collection: object = "", pk: object = "") -> object:
    return collection.objects.filter(pk=pk).get()
