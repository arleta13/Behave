import os

@given(u'I am logged in')
def step_impl(context):
#   raise NotImplementedError(u'STEP: Given I am logged in')
    context.os = os

@when(u'Check the number of processors')
def step_impl(context):
#   raise NotImplementedError(u'STEP: When Check the number of processors')
    context.os = os
    com = "cat /proc/cpuinfo | grep proces | wc -l"
    context.wynik = os.popen(com).read().strip()

@then(u'Behave gave me a number!')
def step_impl(context):
#   raise NotImplementedError(u'STEP: Then Behave gave me a number!')
    assert context.wynik == '2' 
  #  print(context.wynik)
