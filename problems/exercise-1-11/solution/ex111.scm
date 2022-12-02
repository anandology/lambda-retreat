(define (f n)
    (define (iter i a b c)
        (if (= i n)
            c
            (iter (+ i 1) (+ a (* 2 b) (* 3 c)) a b)))
    (iter 0 2 1 0))
