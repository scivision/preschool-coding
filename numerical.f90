module numerical

implicit none

contains

elemental logical function isprime(i)

integer, intent(in) :: i
integer :: j

isprime = .false.

!! trivial tests

if (i<=1) return

if (i==2 .or. i==3) then
  isprime = .true.
  return
endif

if (modulo(i,2) == 0 .or. modulo(i,3) == 0) return

!! 6k+1 test

do j = 5, int(sqrt(real(i))), 6
  if (modulo(i,j) == 0 .or. modulo(i,j+2) == 0) return
enddo

isprime = .true.

end function isprime

end module numerical
