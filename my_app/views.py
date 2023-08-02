from django.shortcuts import render


def example_view(request):
    # my_app/templates/my_app/example.html
    return render(request,'my_app/example.html')

def variable_view(request):
    my_var = {'first_name': 'John', 'last_name': 'Franklin',
              'some_list': [1,2,3], 'some_dict': {'inside_key': 'inside_value'}}
    return render(request,'my_app/variable.html', context=my_var)

    #domain.com/first_app/num1/num2 --> num1+num2
    add_result = num1 + num2
    result = f"{num1} + {num2} = {add_result}"
    return HttpResponse(str(result))