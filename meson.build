project('preschool coding', 'fortran',
  default_options : ['default_library=static', 'buildtype=release', 'warning_level=3'])

num = library('numerical', 'numerical.f90')

executable('number_guess', 'number_guess.f90',
  link_with: num)

prime = executable('prime_test', 'prime_test.f90',
  link_with: num)

test('Prime number test', prime)
