def get_all_items(model_data=''):
    return sorted(model_data.objects.all(), key=lambda x: x.pk)


def find_item(collection='', pk=''):
    return collection.objects.filter(pk=pk).get()