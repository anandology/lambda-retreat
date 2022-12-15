(import "builtins")
(define python builtins)

(define (eval exp env)
;;   (python.print "eval" exp (repr-env env))
  (cond ((self-evaluating? exp) 
         exp)
        ((variable? exp) 
         (lookup-variable-value exp env))
        ((quoted? exp)
         (text-of-quotation exp))
        ((definition? exp)
         (eval-definition exp env))
        ((if? exp)
         (eval-if exp env))
        ((lambda? exp)
         (make-procedure
          (lambda-parameters exp)
          (lambda-body exp)
          env))
        ((application? exp)
         (xapply (eval (operator exp) env)
                 (list-of-values (operands exp) env)))
        (else 
         (error "EVAL - unknown expression type" exp))))
        
(define (xapply proc arguments)
  (cond ((primitive-procedure? proc)
         (apply-primitive-procedure proc arguments))
        ((compound-procedure? proc)
         (eval-sequence
          (procedure-body proc)
          (extend-env
           (procedure-parameters proc)
           arguments
           (procedure-env proc))))
        (else
         (error "APPLY - unknown procedure type" proc))))

; predicates
(define (self-evaluating? e) (number? e))
(define (variable? e) (symbol? e))
(define (quoted? e) (tagged-list? e 'quote ))
(define (definition? e) (tagged-list? e 'define))
(define (if? e) (tagged-list? e 'if))
(define (lambda? e) (tagged-list? e 'lambda))
(define (application? e) (pair? e))


(define (primitive-procedure? e) (tagged-list? e 'primitive))
(define (compound-procedure? e) (tagged-list? e 'compound-procedure))

(define (tagged-list? exp tag)
  (and (pair? exp) 
       (eq? (car exp) tag)))
; quote

(define (text-of-quotation e)
  (cadr e))

;; define

(define (eval-definition exp env)
  (add-binding-to-frame! 
   (definition-variable exp)
   (eval (definition-value exp) env)
   (top-frame env)))

(define (definition-variable exp) (cadr exp))
(define (definition-value exp) (caddr exp))

;; if

(define (eval-if exp env)
  (if (eval (if-predicate exp) env)
      (eval (if-consequent exp) env)
      (eval (if-alternative exp) env)))

(define (if-predicate exp) (cadr exp))
(define (if-consequent exp) (caddr exp))
(define (if-alternative exp) (cadddr exp))

;; apply

(define (operator exp) (car exp))
(define (operands exp) (cdr exp))

(define (apply-primitive-procedure proc args)
  (apply (primitive-procedure-value proc) args))

(define (primitive-procedure-value proc) (cadr proc))

;; lambda

(define (lambda-parameters exp) (cadr exp))
(define (lambda-body exp) (cddr exp))

(define (make-procedure params body env)
  (list 'compound-procedure params body env))

(define (procedure-parameters proc) (cadr proc))
(define (procedure-body proc) (caddr proc))
(define (procedure-env proc) (cadddr proc))

; frame

(define (make-frame vars vals)
  (cons vars vals))

(define frame-vars car)
(define frame-vals cdr)

(define (lookup-frame var frame)
  (define (scan vars vals)
    (cond [(null? vars) '<notfound>]
          [(eq? (car vars) var)
           (car vals)]
          [else (scan (cdr vars) (cdr vals))]))
  (scan (frame-vars frame)
        (frame-vals frame)))

(define (add-binding-to-frame! var val frame)
  (define (append-var!)
      (set-car! frame (cons var (car frame)))
      (set-cdr! frame (cons val (cdr frame))))
  (define (scan vars vals)
    (cond ((null? vars) (append-var!))
          ((eq? (car vars) var) (set-car! vals val))
          (else (scan (cdr vars) (cdr vals)))))
  (scan (car frame) (cdr frame)))

;; eval sequence

(define (eval-sequence exps env)
  (if (null? (cdr exps))
      (eval (car exps) env)
      (begin
       (eval (car exps) env)
       (eval-sequence (cdr exps) env))))


; env

(define primitives
  (list
   (list 'x 10)
   (list '+ +)
   (list '- -)   
   (list '* *)
   (list '= =)
   (list '> >)
   (list '< <)))

(define primitive-variables (map car primitives))
(define primitive-values 
  (map (lambda (p) 
         (list 'primitive (cadr p))) 
       primitives))

(define initial-env '())
(define (setup-env)
  (cons (make-frame 
         primitive-variables
         primitive-values)
        initial-env))

(define (top-frame env) (car env))
(define (enclosing-env env) (cdr env))
(define empty-env? null?)


(define (extend-env vars vals env)
  (let [(frame (make-frame vars vals))]
    (cons frame env)))

(define (lookup-variable-value var env)
;;   (python.print "lookup-variable-value" var (repr-env env))
  (if (empty-env? env)
      (error "Unbound variable" (symbol->string var))
      (let [(frame (top-frame env))]
        (let [(val (lookup-frame var frame))]
          (if (eq? val '<notfound>)
              (lookup-variable-value var (enclosing-env env))
              val)))))
      
(define (list-of-values exps env)
  (map (lambda (e) (eval e env)) exps))
        
(define env (setup-env))
(define (try-eval expr)
  (python.print ">" expr)
  (let ((val (eval expr env)))
    (if (not (eq? val '<void>))
        (python.print val)))) 

(define (repr-env env)
  (map repr-frame env))

(define (repr-frame frame)
  (car frame))

;; (try-eval '1)
;; (try-eval 'x)
;; (try-eval '(quote x))
;; (try-eval '(define a 10))
;; (try-eval 'a)
;; (try-eval '(if #t 10 20))
;; (try-eval '(if #f 10 20))
;; (try-eval '(+ 4 5))
;; (try-eval '(lambda () 4))
;; (try-eval '(lambda (x) (+ x 1)))
;; (try-eval '(define f (lambda (x) (+ x 1))))
;; (try-eval '(f 4))
(try-eval '(define fact (lambda (n) (if (= n 0) 1 (* n (fact (- n 1)))))))
(try-eval '(fact 5))