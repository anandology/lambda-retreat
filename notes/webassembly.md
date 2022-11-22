# Introduction to WebAssembly

WebAssembly is an instruction format for a stack-based virtual machine,
that runs with near-native performance and supported by all modern browsers.

## Example: add

Here is an example of webassembly program to implement a function `add`.


```{.wast .feather .multi-file}
=== main.wast
(module
  (func $add (param $left i32) (param $right i32) (result i32)
        local.get $left
        local.get $right
        i32.add)
  (export "add" (func $add)))
=== main.js
const fs = require('fs');

const buf = fs.readFileSync("main.wasm");
WebAssembly.instantiate(buf).then(mod => {
  const exports = mod.instance.exports;
  const result = exports.add(3, 4);
  console.log(result);
});
```

The module exports the `add` function and the javascript code in `main.js` loads the wasm library and calls that function.

WebAssembly is a stack-machine and arguments are loaded onto the stack before calling the function/operator.

For example, the following three insructions are required to compute `left + right`.

```
local.get $left
local.get $right
i32.add
```

Writing instructions like this is called the _block-instructions_.

There is another way write the instructions called the _folded form_. The _folded form_ is just a syntactic-sugar of the _block-instructions_.

The _folded form_, feels a lot like scheme.

```
(i32.add
    (local.get $left)
    (local.get $right))
```

Let's look at the complete example in the folded form.

```{.wast .feather .multi-file}
=== main.wast
(module
  (func $add (param $left i32) (param $right i32) (result i32)
    (i32.add
        (local.get $left)
        (local.get $right)))
  (export "add" (func $add)))
=== main.js
const fs = require('fs');

const buf = fs.readFileSync("main.wasm");
WebAssembly.instantiate(buf).then(mod => {
  const exports = mod.instance.exports;
  const result = exports.add(3, 4);
  console.log(result);
});
```

For rest of this article, we are going to stick to the folded form.

## Example: Sum of Squares

```{.wast .feather .multi-file}
=== main.wast
(module
  (func $square (param $n i32) (result i32)
    (i32.mul
        (local.get $n)
        (local.get $n)))

  (func $sum_of_squares (param $x i32) (param $y i32) (result i32)
    (i32.add
        (call $square (local.get $x))
        (call $square (local.get $y))))
  (export "square" (func $square))
  (export "sum_of_squares" (func $sum_of_squares)))
=== main.js
const fs = require('fs');

const buf = fs.readFileSync("main.wasm");
WebAssembly.instantiate(buf).then(mod => {
  const exports = mod.instance.exports;
  const result = exports.sum_of_squares(3, 4);
  console.log(result);
});
```

As you can see the WebAssembly Text representation is very similar to Scheme.

## Example: Factorial

Let's now try a recursive function.

```{.wast .feather .multi-file}
=== main.wast
(module
  (func $factorial (param $n i32) (result i32)
    (if (result i32)
        (i32.eq (local.get $n) (i32.const 0))
        (then (i32.const 1))
        (else
            (i32.mul
                (local.get $n)
                (call $factorial (i32.sub (local.get $n) (i32.const 1)))))))
  (export "factorial" (func $factorial)))
=== main.js
const fs = require('fs');

const buf = fs.readFileSync("main.wasm");
WebAssembly.instantiate(buf).then(mod => {
  const exports = mod.instance.exports;
  const result = exports.factorial(5);
  console.log(result);
});
```


## References

* [WebAssembly / Text Format / Instructions](https://webassembly.github.io/spec/core/text/instructions.html)