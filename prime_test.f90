!! test correctness of primality detection
use, intrinsic :: iso_fortran_env, only: int64, dp=>real64
use numerical, only: isprime
implicit none

integer, allocatable :: M(:)
integer :: N, i, j
integer(int64) :: tic, toc, rate
character(10) :: argv

call system_clock(count_rate=rate)

N = 100
call get_command_argument(1,argv, status=i)
if(i==0) read(argv,*) N

allocate(M(N))
j=1
i=2
print *,'finding first ',N, 'primes'

call system_clock(tic)
do while(j<=N)
  if (isprime(i)) then
    M(j) = i
    j = j + 1
  endif
  i = i + 1
enddo
call system_clock(toc)

print '(A,ES10.2,A)',' in ',(toc-tic) / real(rate,dp),' seconds.'
print '(10000I12)', M

!! TODO show logrithmic growth rate (increasing prime sparsity)

end program
