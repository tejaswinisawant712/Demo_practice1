def outer_funtion(outer):
    def inner_function(inner):
        return outer + inner
    inner_result = inner_function(10)
    print(inner_result)

outer_funtion(40)    