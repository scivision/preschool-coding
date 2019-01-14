project('preschool coding', 'fortran', default_options : ['default_library=static'])

fc = meson.get_compiler('fortran')
if fc.get_id() == 'gcc'
  add_global_arguments('-fimplicit-none', '-Wall', '-Wextra', '-Wpedantic', language : 'fortran')
endif

num = library('numerical', 'numerical.f90')

executable('number_guess', 'number_guess.f90',
  link_with: num)
  
prime = executable('prime_test', 'prime_test.f90',
  link_with: num)

test('Prime number test', prime)
