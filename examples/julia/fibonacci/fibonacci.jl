function solve(n)
    a, b = 0, 1
    for i in 1:n
        a, b = b, a+b
    end
    a
end

println(solve(0))
println(solve(1))
println(solve(2))
println(solve(3))
println(solve(10))
println(solve(20))
println(solve(30))
