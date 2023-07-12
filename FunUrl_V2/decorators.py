from datetime import datetime


def check(model):
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            format = "%d/%m/%Y, %H:%M:%S"
            urls = model.objects.all()
            for i in urls:
                now = datetime.now()
                update = i.expiry_at
                # prev = i.created_at
                datetime_object2 = datetime.strptime(update, format)
                # datetime_object1 = datetime.strptime(prev, format)
                if datetime_object2 <= now:
                    obj = model.objects.get(rurl=i.rurl)
                    obj.delete()
            return view_func(request, *args, **kwargs)

        return wrapper

    return decorator
