function solve(a, b)
    while b != 0
        a, b = b, a % b
    end
    a
end

println(solve(0, 0))
println(solve(0, 7))
println(solve(7, 0))
println(solve(48, 18))
println(solve(17, 13))
println(solve(270, 192))
