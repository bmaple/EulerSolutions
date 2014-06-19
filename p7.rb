include Math
def sieve(num, nprime)
    iter = 1 
    nums = Array.new(num){ |i| true } 
    for i in (2..num)
        if nums[i] == true
            if iter == nprime
                return i
            end
            iter = iter+1
            (i**2..num).step(i) do |s|
                nums[s] = false
            end
        end
    end
    return nil
end
if __FILE__ == $PROGRAM_NAME
    primes = sieve(900_000, 10_001)
    puts primes
end
