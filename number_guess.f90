!! not every compiler inits  arandom seed (Gfortran yes, flang no)
use, intrinsic:: iso_fortran_env, only: stdin=>input_unit, stdout=>output_unit
use numerical, only: isprime

implicit none

integer :: secret, guess, i
real :: r
character(20) :: msg, buf

call random_number(r)
secret = int((r*99+1))

msg = 'guess my number  '

main: do
  write(stdout,'(A)', advance='no') msg
  read(stdin,*, iostat=i) buf
  if (i/=0) stop 'goodbye'
  
  if (buf == 'h' .or. buf == 'hint' .or. buf == 'help') then
    if (isprime(secret)) then
      print *,'my secret number is prime'
    else
      print *,'my secret number is NOT prime'
    endif
  else
    read(buf,*, iostat=i) guess
    if (i/=0) stop 'goodbye'
  endif

  if(guess < secret) then
    msg = 'try bigger  '
  elseif(guess > secret) then
    msg = 'try smaller  '
  elseif(guess == secret) then
    print *,'you guessed my secret number -- hooray!'
    exit main
  else
    error stop 'impossible'
  endif

enddo main

end program
