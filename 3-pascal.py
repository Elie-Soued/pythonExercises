# write a function that takes an integer n as an argument
#  and prints the n first lines of a Pascal Triangle



def pascal(n):
    for i in range(n) :
        print( " ".join(str(pascal_line(i))))
        


def pascal_line(n):
    arr = []
    if n == 0:
        n = 1
    for i in range(n):
        arr.append(pascal_cell(i, n))   
    return arr



def pascal_cell(i,j):
    return (
        factorial(j)/ factorial(i) * factorial(j -i)
    )


def factorial(n):
    if(n < 2):
        return 1
    else:
        return  n * factorial(n-1)


print (pascal_cell(1,3))


# JS Solution

# function pascal(n) {
#   for (let i = 0; i < n; i++) {
#     console.log(pascal_line(i).join(" "));
#   }
# }

# function pascal_line(n) {
#   let arr = new Array();
#   for (let i = 0; i <= n; i++) {
#     arr.push(pascal_cell(i, n));
#   }
#   return arr;
# }

# const factorial_recursive = function fac(n) {
#   return n < 2 ? 1 : n * fac(n - 1);
# };

# function pascal_cell(i, j) {
#   return (
#     factorial_recursive(j) /
#     (factorial_recursive(i) * factorial_recursive(j - i))
#   );
# }

# // const factorial_iterative = function (n) {
# //   let result = 1;
# //   for (let i = n; i > 1; i--) {
# //     result = i * result;
# //   }

# //   return result;
# // };

# //Tests
# console.assert(pascal_cell(0, 0) == 1);
# console.assert(pascal_cell(3, 3) == 1);
# console.assert(pascal_cell(2, 3) == 3);

# console.assert(pascal_line(5).join(" ") == "1 5 10 10 5 1");
# console.assert(pascal_line(0).join(" ") == "1");
# console.assert(pascal_line(2).join(" ") == "1 2 1");

# console.assert(factorial_iterative(3) == 6);
# console.assert(factorial_iterative(5) == 120);
# console.assert(factorial_iterative(8) == 40320);