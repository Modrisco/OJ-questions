(define (function a b c)
  (cond 
    ((and (>= a c) (>= b c)) (+ (* a a) (* b b)))
    ((and (>= a b) (>= c b)) (+ (* a a) (* c c)))
    (else (+ (* b b) (* c c)))
  )
)