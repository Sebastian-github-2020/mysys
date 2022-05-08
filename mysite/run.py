def data(status, data, **kwargs):
    return {
        "status": status,
        "data": data,
        **kwargs
    }


a = data(200, 123, msg="msg")
print(a)
