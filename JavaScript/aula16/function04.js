function fatorial(n=0) {
    let f = 1
    for (let c = n; c >= 1; c -= 1) {
        f *= c
    }
    return f
}

let res = fatorial(7)
console.log(res)